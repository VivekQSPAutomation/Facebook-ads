import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class CorrectionDraft(Basepages):
    Campaign = (By.XPATH, "//a[contains(text(),'Campaigns')]")
    Type = (By.XPATH, "//div[@class='workspace-tabs']/div")
    first_application = (
        By.XPATH,
        "//div[@class='masonry-grid-custom  ']//button[contains(text(),'Edit Draft')]",
    )
    Edit_update = (By.XPATH, "//div[@id='editor']//p")
    review_send = (By.XPATH, "//span[contains(text(),'Send')]")
    Select_msg = (By.XPATH, "//span[@class='inlineComment']")
    Resolve_button = (By.XPATH, "//p[contains(text(),'Resolve')]")
    Comment = (By.XPATH, "//textarea[@name='commentBody']")
    Attach_comment = (By.XPATH, "//button[contains(text(),'Attach Reply')]")
    all_draft = (By.XPATH, "//div[@class='container  ']")
    h3_data = (By.XPATH, "//h3[text()]")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(f"{TestData.env_setup(self)}/workspace")

    def selected_text_draft(self):
        sign_type = self.get_elements(self.Type)
        self.click_element_with_js(sign_type[1])
        retry_count = 1
        wait = WebDriverWait(self.driver, 10)
        lines = self.get_elements(self.h3_data)
        count = 1
        for line in lines:
            try:
                if "SOCIAL POST" in line.text:
                    print(count)
                    time.sleep(3)
                    element = wait.until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f"(//h3[text()]/..)[{count}]//button")
                        )
                    )
                    element.click()
                    self.do_click(self.Select_msg)
                    time.sleep(2)
                    self.do_click(self.Resolve_button)
                    self.do_send_keys(self.Comment, "Testing Resolved")
                    self.do_click(self.Attach_comment)
                    time.sleep(3)
                    self.do_click(self.review_send)
                    msg_value = (
                        WebDriverWait(self.driver, 20)
                        .until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//div[@class='bannerMessage ']")
                            )
                        )
                        .text
                    )

                    return msg_value == TestData.DRAFT_MSG

            except StaleElementReferenceException:
                continue

            except TimeoutException:
                print(retry_count)
                if retry_count > 3:
                    return False
                else:
                    self.driver.get(f"{TestData.env_setup(self)}/workspace")
                    retry_count += 1

            count += 1
