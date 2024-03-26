import os
import sys
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class AccountEmailpassword(Basepages):
    Refresh_click = (By.XPATH, "//span[contains(text(),'Refresh')]")
    Save_button = (By.XPATH, "//button[@default='Save']")
    Account_Button = (By.XPATH, "//a[contains(text(),'Account Settings')]")
    Reset_password = (By.XPATH, "//button[contains(text(),'Reset Password')]/..")
    Send_email = (By.XPATH, "//button[(@default = 'Send password reset email')]")
    Click_here = (By.XPATH, "//a[@class='bold-link']")
    New_password = (By.XPATH, "//input[@placeholder ='New Password']")
    Confirm_password = (By.XPATH, "//input[@placeholder ='Confirm Password']")
    Update_password = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_form_child(self):
        parent_form = self.driver.find_element(By.TAG_NAME, "form")
        return parent_form.find_elements(By.TAG_NAME, "input")

    def account_email_button(self):
        self.do_click(self.Account_Button)

    def reset_password(self):
        self.do_click(self.Reset_password)

    def email_verfication(self):
        print(self.get_form_child()[0].get_attribute("id"))
        self.do_send_keys(
            (By.ID, self.get_form_child()[0].get_attribute("id")),
            os.environ.get("Email"),
        )
        self.do_click(self.Send_email)
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
        assert msg_value == TestData.Confirmation_msg
        self.get_window(0)

    #
    def verify_email(self):
        time.sleep(2)
        self.do_click(self.Refresh_click)
        time.sleep(3)
        parent = self.driver.find_element(
            By.XPATH, "//ul[@class='mail-items-list']/li[1]"
        )

        parent.click()
        iframe_value = self.driver.find_element(By.XPATH, "//iframe[@id='fullmessage']")
        self.driver.switch_to.frame(iframe_value)
        self.do_click(self.Click_here)

        time.sleep(15)
        print(len(self.driver.window_handles))

        self.get_window(len(self.driver.window_handles) - 1)

    def new_confirm_password(self):
        try:
            self.do_send_keys(self.New_password, TestData.NEWPASS)
            self.do_send_keys(self.Confirm_password, TestData.CONFIRMPASS)
            self.do_click(self.Update_password)

        except NoSuchElementException:
            assert False
