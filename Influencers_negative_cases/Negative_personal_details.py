import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class NegativePersonal_pages(Basepages):
    Save_button = (By.XPATH, "//button[@default='Save']")
    Home_Button = (By.XPATH, "//a[contains(text(),'View Homepage')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(
            f"{TestData.env_setup(self)}/partners/settings/personal-details"
        )

    def get_form_input_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.TAG_NAME, "input")

    def get_form_textarea_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_element(By.TAG_NAME, "textarea")

    def get_personal_details(self, data):
        time.sleep(3)
        textarea_child = self.get_form_textarea_child()
        self.get_clear((By.ID, textarea_child.get_attribute("id")))
        self.do_send_keys((By.ID, textarea_child.get_attribute("id")), data)
        form_child = self.get_form_input_child()
        for child in form_child:
            if "calendar-input-influencer-birthday" in child.get_attribute("id"):
                self.get_clear((By.ID, child.get_attribute("id")))
                time.sleep(1)
                self.do_send_keys((By.ID, child.get_attribute("id")), "02/10/1999")
            else:
                pass
        self.do_click(self.Save_button)
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
        assert msg_value == TestData.USER_INFORM

    def get_personal_date_details(self, date_test):
        time.sleep(3)
        form_child = self.get_form_input_child()
        for child in form_child:
            if "calendar-input-influencer-birthday" in child.get_attribute("id"):
                self.get_clear((By.ID, child.get_attribute("id")))
                self.do_send_keys((By.ID, child.get_attribute("id")), date_test)
            else:
                pass
        self.do_click(self.Save_button)
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
        assert msg_value == TestData.USER_INFORM
