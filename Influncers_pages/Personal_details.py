import os
import time
from datetime import date

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Personal_pages(Basepages):
    Save_button = (By.XPATH, "//button[@default='Save']")
    Home_Button = (By.XPATH, "//a[contains(text(),'View Homepage')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_form_input_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.TAG_NAME, "input")

    def get_form_textarea_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_element(By.TAG_NAME, "textarea")

    def get_personal_details(self):
        # try:
            time.sleep(3)
            textarea_child = self.get_form_textarea_child()
            self.do_send_keys((By.ID, textarea_child.get_attribute("id")), "Testing_")
            form_child = self.get_form_input_child()
            count =1
            for child in form_child:
                print(child.get_attribute("value"))
                if child.get_attribute("value") == "true":
                    self.do_click(
                        (
                            By.XPATH,
                            "//input[@id = '{}']/..".format(child.get_attribute("id")),
                        )
                    )
                elif "calendar-input-influencer-birthday" in child.get_attribute("id"):
                    self.get_clear((By.ID, child.get_attribute("id")))
                    self.do_send_keys((By.ID, child.get_attribute("id")), "02/10/1999")
                elif child.get_attribute("value") == "Male":
                    self.do_click(
                        (
                            By.XPATH,
                            "//input[@id = '{}']/..".format(child.get_attribute("id")),
                        )
                    )
                elif "DOGS" in child.get_attribute("id"):
                    self.do_click(
                        (
                            By.XPATH,
                            "//input[@id = '{}']/..".format(child.get_attribute("id")),
                        )
                    )
                elif child.get_attribute("type") == "text":
                    pass
                elif child.get_attribute("type") == "checkbox":
                    if "What language(s) do you speak? *" == self.get_element_text((By.XPATH,"//input[@id='{}' ]/../../..//label".format(child.get_attribute("id")))):

                        if child.get_attribute("id")  and child.get_attribute('paramchecked') is not None:
                            self.do_click(
                                (
                                    By.XPATH,
                                    "//input[@id = '{}']/..".format(child.get_attribute("id")),
                                )
                            )
                            break
                        else:
                            self.do_click(
                                (
                                    By.XPATH,
                                    "//input[@id = '{}']/..".format(child.get_attribute("id")),
                                )
                            )

                    else:
                        self.do_click(
                            (
                                By.XPATH,
                                "//input[@id = '{}']/..".format(child.get_attribute("id")),
                            )
                        )

                elif child.get_attribute("value") == "American Indian or Alaska Native":
                    print("//input[@id = '{}']/..".format(child.get_attribute("id")))
                    self.do_click(
                        (
                            By.XPATH,
                            "//input[@id = '{}']/..".format(child.get_attribute("id")),
                        )
                    )

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
            return msg_value == TestData.USER_INFORM
        # except TimeoutException:
        #     return False
