import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class SignBrief(Basepages):
    Campaign = (By.XPATH, "//a[contains(text(),'Campaigns')]")
    all_sign_brief = (By.XPATH, "//div[@class='container  ']")
    Type = (By.XPATH, "//div[@class='workspace-tabs']/div")
    View_brief = (
        By.XPATH,
        "//button[contains(text(),'View Brief')]",
    )
    Sign_brief = (
        By.XPATH,
        "//button[@class='sign js-login-submit btn btn--emptyBorder btn--full text text--uppercase text--bold']",
    )
    Signature = (By.XPATH, "//canvas[@class='signature-pad']")
    Sign_button = (By.XPATH, "//button[@label='Save & Continue']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{TestData.env_setup(self)}/workspace")

    def sign_brief(self, data):
        # self.do_click(self.Campaign)
        time.sleep(4)
        if self.driver.current_url != f"{TestData.env_setup(self)}/workspace":
            self.driver.get(f"{TestData.env_setup(self)}/workspace")
        else:
            pass
        sign_type = self.get_elements(self.Type)
        self.click_element_with_js(sign_type[0])
        string_found = False
        retry_count = 1
        check = False
        count = 1
        wait = WebDriverWait(self.driver, 10)
        # for count in range(0, len(self.get_elements(self.all_sign_brief))):
        while True:
            sign_type = self.get_elements(self.Type)
            self.click_element_with_js(sign_type[0])
            try:
                lines = wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"(//div[@class='container  '])[{count}]")
                    )
                ).text.split("\n")
                for line in lines:
                    if data in line:
                        print(line, data)
                        element = wait.until(
                            EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    f"(//div[@class='container  '])[{count}]//button[contains(text(),'View Brief')]",
                                )
                            )
                        )
                        self.scroll_to(element)
                        self.click_element_with_js(element)
                        # time.sleep(10)
                        self.do_click(self.Sign_brief)
                        canvas = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//div[@class='denyReason signBox']//canvas")
                            )
                        )

                        start_x, start_y = 100, 100
                        end_x, end_y = 200, 200
                        self.driver.save_screenshot(f"screenshots/{time.time()}.png")
                        time.sleep(20)
                        for _ in range(5):
                            action_chains = ActionChains(self.driver)
                            action_chains.move_to_element_with_offset(
                                canvas, start_x, start_y
                            ).click_and_hold().move_by_offset(
                                end_x - start_x, end_y - start_y
                            ).release().perform()
                        self.driver.save_screenshot(f"screenshots/{time.time()}.png")
                        self.do_click(self.Sign_button)

                        check = True
                        time.sleep(20)
                        break

            except StaleElementReferenceException:
                continue

            except TimeoutException:
                print(retry_count)
                if retry_count > 3:
                    return False
                else:
                    self.driver.get(f"{TestData.env_setup(self)}/workspace")
                retry_count += 1

            if check:
                break

            count = +1
