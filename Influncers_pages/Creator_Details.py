import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class CreatorPages(Basepages):
    Save_button = (By.XPATH, "//button[@default='Save']")
    Next_Button = (By.XPATH, "//a[contains(text(),'Next')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(
            f"{TestData.env_setup(self)}/partners/settings/blog-details"
        )

    def get_form_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.TAG_NAME, "input")

    def get_creator_details(self):
        try:
            time.sleep(2)
            form_child = self.get_form_child()
            time.sleep(2)
            for child in form_child:
                if "mainUrl" in child.get_attribute("id"):
                    self.get_clear((By.ID,child.get_attribute("id")))
                    self.do_send_keys(
                        (By.ID, child.get_attribute("id")), "https://google.com"
                    )

                elif "blogUrl" in child.get_attribute(
                    "id"
                ) or "blogName" in child.get_attribute("id"):
                    pass
                else:
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f"//input[@id='{child.get_attribute('id')}']/..")
                        )
                    ).click()
                    # time.sleep(1)

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
            if msg_value == TestData.USER_INFORM:
                self.do_click(self.Next_Button)
                return True
        except TimeoutException:
            return False

