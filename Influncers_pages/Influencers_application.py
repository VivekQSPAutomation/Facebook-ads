import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Influence_Application(Basepages):
    click_app = (By.XPATH, "//span[contains(text(),'Applications')]/..")
    first_application = (By.XPATH, "//div[@class='container  ']")
    apply_button = (By.XPATH, "//button[contains(text(),'Apply')]")
    app_application = (
        By.XPATH,
        "//div[@class='buttonsContainer']//a",
    )
    input_yes_value = (By.XPATH, "//input[@type='radio']/../..")
    textarea = (By.TAG_NAME, "textarea")
    send_proposal = (By.XPATH, "//button[contains(text(),'Send Proposal')]")
    brand_name = (By.XPATH,"//div[@class='ql-editor']//ul[1]//li[1]")
    retailer_name = (By.XPATH,"//div[@class='ql-editor']//ul[1]//li[3]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(
            f"{TestData.env_setup(self)}/applications/dashboard"
        )

    def input_with_yes(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.XPATH, "//input[@value='Yes']")

    def apply_application(self):
        try:
            first_application = self.get_elements(self.first_application)
            for element in first_application:
                if element.find_element(
                    By.XPATH, '//h3[contains(text(),"Short Form Video")]'
                ):
                    nested = element.find_element(
                        By.XPATH, "//button[contains(text(),'Apply')]"
                    )
                    nested.click()
                    break
            self.do_click(self.app_application)
            time.sleep(3)
            values = self.input_with_yes()
            for value in values:
                self.driver.execute_script("arguments[0].click();", value)
            text = self.get_elements(self.textarea)
            for area in text:
                area.send_keys("Testing QA")
            self.do_click(self.send_proposal)
            time.sleep(5)
            return True
        except TimeoutException:
            return False
