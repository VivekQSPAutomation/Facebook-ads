import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Social_pages(Basepages):
    Next_button = (By.XPATH, "//a[contains(text(),'Next')]")
    Social_sidebar = (By.XPATH, "//span[contains(text(),'Social Accounts')]")
    facebook = (By.XPATH, "//button[@data-social ='facebook']")
    facebook_Email = (By.XPATH, "//input[@id='email']")
    facebook_password = (By.XPATH, "//input[@id='pass']")
    facebook_button = (By.XPATH, "//input[@type='submit']")

    """Pinterest Login"""

    pinterest = (By.XPATH, "//button[@data-social ='pinterest']")
    pin_allow = (By.XPATH, "//div[contains(text(),'Give access')]")

    """Instagram Login"""

    insta = (By.XPATH, "//button[@data-social ='instagram']")
    insta_login = (
        By.XPATH,
        "//input[@aria-label='Phone number, username or email address']",
    )
    insta_pass = (By.XPATH, "//input[@type='password']")
    insta_button = (By.XPATH, "//button[@type='submit']")
    instagram_facebook = (By.XPATH, "//span[contains(text(),'Allow')]/..")
    instagram_autologin = (
        By.XPATH,
        "//div[contains(text(),'Continue as viveketestmeli')]",
    )
    insta_allow = (By.XPATH, "//div[@aria-label='Allow']")
    pin_email = (By.XPATH, "//input[@id='email']")
    pin_pass = (By.XPATH, "//input[@id='password']")
    Pin_button = (By.XPATH, "//div[contains(text(),'Log in')]/..")
    not_now = (By.XPATH, "//div[contains(text(),'Not')]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        self.driver.get(
            f"{TestData.env_setup(self)}/partners/settings/social"
        )

    def social_pages(self):
        self.do_click(self.Social_sidebar)

    def facebook_author(self):
        try:
            if os.environ.get("Email"):
                self.do_click(self.facebook)
                time.sleep(1)
                if len(self.driver.window_handles) < 3:
                    print(len(self.driver.window_handles))
                    self.get_window(1)
                else:
                    self.get_window(3)
                count = 1
                # self.get_window(3)
                self.do_send_keys(self.facebook_Email, TestData.Facebook_Socail_Email)
                self.do_send_keys(self.facebook_password, TestData.Facebook_SOCIAL_PASS)
                self.do_click(self.facebook_button)
                if len(self.driver.window_handles) > 2:
                    self.get_window(1)
                else:
                    self.get_window(0)
                msg_value = (
                    WebDriverWait(self.driver, 30)
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
                return msg_value == TestData.FACEBOOK_MSG
            else:
                self.do_click(self.facebook)
                # print(len(self.driver.window_handles))
                time.sleep(1)
                self.get_window(3)
                self.do_send_keys(self.facebook_Email, TestData.Facebook_Socail_Email)
                self.do_send_keys(self.facebook_password, TestData.Facebook_SOCIAL_PASS)
                self.do_click(self.facebook_button)
                self.get_window(1)
                msg_value = (
                    WebDriverWait(self.driver, 30)
                    .until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                # "//div[@class='alert-dialog js-login-alert alert-dialog--success showAlertDialog']",
                                "//div[@class='AlertDialogComponent alert-dialog__login ember-view']",
                            )
                        )
                    )
                    .text
                )
                if msg_value == TestData.INSTAGRAM_MSG:
                    return True
                else:
                    return False
        except TimeoutException:
            return False

    def pinterest_author(self):
        self.do_click(self.pinterest)

        while "Pinterest" in self.driver.title:
            self.do_send_keys(self.pin_email, TestData.PIN_EMAIL)
            self.do_send_keys(self.pin_pass, TestData.PIN_PASS)
            self.do_click(self.Pin_button)
            try:
                self.do_click(self.pin_allow)
                break
            except TimeoutException:
                self.driver.get(
                    f"{TestData.env_setup(self)}/partners/settings/social"
                )
                self.do_click(self.pinterest)
                print(
                    WebDriverWait(self.driver, 10)
                    .until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//div[contains(text(),'Give access')]")
                        )
                    )
                    .is_displayed()
                )
                if (
                        WebDriverWait(self.driver, 10)
                                .until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//div[contains(text(),'Give access')]")
                            )
                        )
                                .is_displayed()
                ):
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//div[contains(text(),'Give access')]")
                        )
                    ).click()
                    break

        msg_value = (
            WebDriverWait(self.driver, 30)
            .until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        # "//div[@class='alert-dialog js-login-alert alert-dialog--success showAlertDialog']",
                        "//div[@class='AlertDialogComponent alert-dialog__login ember-view']",
                    )
                )
            )
            .text
        )
        if msg_value == TestData.PINTEREST_MSG:

            return True
        else:
            return False

    def instagram_author(self):
        self.do_click(self.insta)
        try:
            try:
                self.do_send_keys(self.insta_login, TestData.SOCIAL_EMIAL)
                self.do_send_keys(self.insta_pass, TestData.SOCIAL_PASS)
                self.do_click(self.insta_button)
                self.do_click(self.not_now)

            except TimeoutException:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//div[contains(text(),'Continue')]",
                        )
                    )
                ).click()
                # self.do_send_keys(self.insta_login, TestData.SOCIAL_EMIAL)
                # self.do_send_keys(self.insta_pass, TestData.SOCIAL_PASS)
                # self.do_click(self.insta_button)
                # self.do_click(self.not_now)

            self.do_click(self.insta_allow)
            msg_value = (
                WebDriverWait(self.driver, 20)
                .until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//div[@class='AlertDialogComponent alert-dialog__login ember-view']",
                        )
                    )
                )
                .text
            )
            print(msg_value)
            if msg_value == TestData.INSTAGRAM_MSG:
                return True
            else:
                return False
        except TimeoutException:
            return False
        except AssertionError as e:
            self.driver.get(
                f"{TestData.env_setup(self)}/partners/settings/social?"
            )

    def next_button(self):
        self.do_click(self.Next_button)
