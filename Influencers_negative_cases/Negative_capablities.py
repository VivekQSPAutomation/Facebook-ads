import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class NegativeCapabilities_pages(Basepages):
    Save_button = (By.XPATH, "//button[@default='Save']")
    Next_Button = (By.XPATH, "//a[contains(text(),'Next')]")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(f"{TestData.env_setup(self)}/partners/settings/capablities")

    def get_form_child(self):
        time.sleep(3)
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.TAG_NAME, "input")

    def get_capablities_details(self, data):
        form_child = self.get_form_child()

        if form_child[0].get_attribute("value") == "true":
            self.do_click(
                (
                    By.XPATH,
                    "//input[@id='{}']/..".format(form_child[0].get_attribute("id")),
                )
            )
            sub_parent_child = self.get_form_child()
            time.sleep(4)
            for sub_child in sub_parent_child[2:]:
                if sub_child.get_attribute("type") == "text":
                    self.do_send_keys((By.ID, sub_child.get_attribute("id")), data)
                elif sub_child.get_attribute("value") == "true":
                    self.do_click(
                        (
                            By.XPATH,
                            "//input[@id='{}']/..".format(
                                sub_child.get_attribute("id")
                            ),
                        )
                    )

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
        self.do_click(self.Next_Button)
        time.sleep(3)
