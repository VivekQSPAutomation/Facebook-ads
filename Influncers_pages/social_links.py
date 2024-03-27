import time

from selenium.common import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Socialinks(Basepages):
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
    container_div = "(//div[@class='field-container'])[1]"
    saveandclose = (By.XPATH, "//button[contains(text(),'Save')]")
    dots = (By.XPATH, "//div[@class='dots']")
    socail_link = (
        By.XPATH,
        "(//div[@class='wrapper influencerApplicationCardPopover']//button)[3]",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{TestData.env_setup(self)}/workspace")

    def social_links(self):
        time.sleep(3)
        sign_type = self.get_elements(self.Type)
        self.click_element_with_js(sign_type[2])
        time.sleep(4)
        self.driver.save_screenshot(f"screenshots/{time.time()}.png")
        self.do_click(self.dots)
        time.sleep(2)
        self.do_click(self.socail_link)
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='top']//input[@type='checkbox']")
            )
        )
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)

            self.do_send_keys(
                (By.XPATH, "//div[@class='field-container']//input[@type='text']"),
                "https://facebook.com",
            )
            break
        self.do_click(self.saveandclose)
        time.sleep(5)
