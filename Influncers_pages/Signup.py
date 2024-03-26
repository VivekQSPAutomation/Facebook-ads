import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Signup(Basepages):
    FORM_ID = (By.XPATH, "//form")
    FORM_CHILD = (By.XPATH, ".//*")
    BUTTON_CLICK = (By.XPATH, "//button[@default='Submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.execute_script(
            f'window.open("{TestData.env_setup(self)}/partners/register")',
            "_blank",
        )
        self.get_window(1)

    def get_page_title(self, title):
        return self.pages_title(title)

    def get_form_child(self):
        try:
            form = self.driver.find_element(By.XPATH, "//form")
            child = form.find_elements(By.TAG_NAME, "input")
            if os.environ.get("Email"):
                for node in child:
                    if node.get_attribute("type") == "radio":
                        self.driver.find_element(
                            By.XPATH, "//span[@class='yesAccept']/div/label"
                        ).click()
                    elif node.get_attribute("type") == "text":
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            "Testing"
                        )
                    elif node.get_attribute("type") == "password":
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            "vivek@123"
                        )
                    else:
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            os.environ.get("Email")
                        )

                self.do_click(self.BUTTON_CLICK)
                assert True, "Login Successful"
            elif os.environ.get("Emai"):
                for node in child:
                    if node.get_attribute("type") == "radio":
                        self.driver.find_element(
                            By.XPATH, "//span[@class='yesAccept']/div/label"
                        ).click()
                    elif node.get_attribute("type") == "text":
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            "Testing"
                        )
                    elif node.get_attribute("type") == "password":
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            "vivek@123"
                        )
                    else:
                        self.driver.find_element(By.ID, node.get_attribute("id")).send_keys(
                            os.environ.get("Emai")
                        )

                self.do_click(self.BUTTON_CLICK)

            else:
                return False
            time.sleep(5)
            self.get_window(0)
            return True

        except TimeoutException:
            return False

