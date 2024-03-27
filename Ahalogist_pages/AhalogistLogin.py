import time

from selenium.webdriver.common.by import By

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Welcome_session(Basepage):
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUT = (By.ID, "btn-login")
    LOGIN_CLICKABLE = (By.XPATH, "//a[contains(text(), 'Login to Quotient Social')]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/signup")

    def login_url_redirect_session(self):
        self.do_click(self.LOGIN_CLICKABLE)
        time.sleep(1)
        self.do_send_keys(self.EMAIL, TestData.Aha_login_email)
        self.do_send_keys(self.PASSWORD, TestData.Aha_login_password)
        self.do_click(self.SUBMIT_BUT)
        time.sleep(3)
        if self.driver.current_url == f"{TestData.env_setup(self)}/signup":
            return False
        else:
            return True
