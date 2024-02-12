import os
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Config.config import TestData
from Promo_pages.BasePages import Basepages


class Login(Basepages):
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUT = (By.XPATH, "//button[contains(text(),'Sign In')]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/login")

    def login(self):
        try:
            self.do_send_keys(self.EMAIL, TestData.LOGIN_EMAIL)
            self.do_send_keys(self.PASSWORD, TestData.LOGIN_PASSWORD)
            self.do_click(self.SUBMIT_BUT)
            time.sleep(5)
            return True
        except TimeoutException:
            return False

        # try:
        #     if (
        #         self.get_element_value(self.Error_message)
        #         == "Please verify your email address"
        #     ):
        #         self.get_window(0)
        #         Random_Email.validation_email()
        #
        # except TimeoutException:
        #     pass
