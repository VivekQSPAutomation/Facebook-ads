import os
import time

import pandas as pd
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Welcome_session(Basepages):
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUT = (By.ID, "btn-login")
    LOGIN_CLICKABLE = (By.XPATH, "//a[contains(text(), 'Login to Quotient Social')]")
    Error_message = (By.XPATH, "//div[@class='message']")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/signup")

    def login_url_redirect_session(self):
        try:
            df = pd.read_csv(f"{os.getcwd()}/influencers.csv")
            self.do_click(self.LOGIN_CLICKABLE)
            time.sleep(3)
            # if os.environ.get("Email"):
            #     self.do_send_keys(self.EMAIL, os.environ.get("Email"))
            #     self.do_send_keys(self.PASSWORD, TestData.LOGIN_PASSWORD)
            #     self.do_click(self.SUBMIT_BUT)
            # elif os.environ.get("Emai"):
            #     self.do_send_keys(self.EMAIL, os.environ.get("Emai"))
            #     self.do_send_keys(self.PASSWORD, TestData.LOGIN_PASSWORD)
            #     self.do_click(self.SUBMIT_BUT)
            if "staging" in TestData.env_setup(self):
                os.environ["Email"] = df["Influencer"].iloc[0]
                self.do_send_keys(self.EMAIL, os.environ.get("Email"))
            else:
                os.environ["Email"] = df["Influencer"].iloc[1]
                self.do_send_keys(self.EMAIL, os.environ.get("Email"))

            self.do_send_keys(self.PASSWORD, TestData.LOGIN_PASSWORD)

            self.do_click(self.SUBMIT_BUT)

            time.sleep(10)
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
