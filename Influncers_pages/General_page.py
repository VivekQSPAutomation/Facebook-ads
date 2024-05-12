import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Homepages(Basepages):
    Save_button = (By.XPATH, "//button[@type='submit']")
    image_button = (By.XPATH, "//button[@id='upload_widget_opener']")
    Next_button = (By.XPATH, "//a[contains(text(),'Next')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{TestData.env_setup(self)}/partners/settings/general")

    def influence_profile_setting(self):
        try:
            time.sleep(3)
            form_data = self.driver.find_element(By.TAG_NAME, "form")
            child_input = form_data.find_elements(By.TAG_NAME, "input")
            time.sleep(3)
            country_select = Select(form_data.find_element(By.TAG_NAME, "select"))
            country_select.select_by_value("USA")
            if country_select.first_selected_option:
                form_select = self.driver.find_element(By.TAG_NAME, "form")
                child_select = form_select.find_elements(By.TAG_NAME, "select")[1]
                Select(child_select).select_by_value("Alabama")
                after_form_select = self.driver.find_element(By.TAG_NAME, "form")
                after_child_select = after_form_select.find_elements(
                    By.TAG_NAME, "input"
                )[6]
                self.get_clear((By.ID, after_child_select.get_attribute("id")))
                self.driver.find_element(
                    By.ID, after_child_select.get_attribute("id")
                ).send_keys("12345")
            for child in child_input:
                if "Pronunciation" in child.get_attribute("id"):
                    self.get_clear((By.ID, child.get_attribute("id")))
                    self.driver.find_element(
                        By.ID, child.get_attribute("id")
                    ).send_keys("please fill your Pronunciation")
                elif "zip" in child.get_attribute("id"):

                    pass
                elif child.get_attribute("value") == "true":

                    WebDriverWait(self.driver, 2).until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                "//label[contains(text(), 'Do you have an agent/representation? *')]/../div",
                            )
                        )
                    ).click()
                    form_data = self.driver.find_element(By.TAG_NAME, "form")
                    checked_input = form_data.find_elements(By.TAG_NAME, "input")
                    for checked_child in checked_input[-2:]:
                        self.get_clear((By.ID, checked_child.get_attribute("id")))
                        self.driver.find_element(
                            By.ID, checked_child.get_attribute("id")
                        ).send_keys("Testing QA")
                elif child.get_attribute("type") == "tel":
                    self.get_clear((By.ID, child.get_attribute("id")))
                    self.driver.find_element(
                        By.ID, child.get_attribute("id")
                    ).send_keys("1234")
                elif child.get_attribute("value") == "false":
                    pass
                else:
                    self.get_clear((By.ID, child.get_attribute("id")))
                    self.driver.find_element(
                        By.ID, child.get_attribute("id")
                    ).send_keys("Testing")

            self.driver.find_element(By.XPATH, "//button[@default='Save']").send_keys(
                Keys.RETURN
            )
            msg_value = (
                WebDriverWait(self.driver, 8)
                .until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//div[@class='alert-dialog js-login-alert alert-dialog--success showAlertDialog']",
                        )
                    )
                )
                .text
            )
            if msg_value == TestData.USER_INFORM:
                self.do_click(self.Next_button)
                return True
            else:
                return False
        except TimeoutException:
            return False
