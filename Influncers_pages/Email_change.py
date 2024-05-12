from selenium.webdriver.common.by import By

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class AccountEmailChange(Basepages):
    Account_Button = (By.XPATH, "//a[contains(text(),'Account Settings')]")
    Change_button = (By.XPATH, "//span[contains(text(),'Change')]/..")
    alert_check = (By.XPATH, "//button[@class='pure-button pure-button-primary']")
    New_Email = (By.ID, "i-email")
    Email_change_button = (By.XPATH, "//button[contains(text(),'Change Email')]")
    Current_pass = (By.XPATH, "//input[@name='current-password']")
    New_Email_input = (By.XPATH, "//input[@name='new-email']")
    Confirm_Email_input = (By.XPATH, "//input[@name='confirm-email']")
    Update_button = (
        By.XPATH,
        "//button[@class ='btn btn--emptyBorder btn--full text text--uppercase text--bold ']",
    )

    def __init__(self, driver):
        super().__init__(driver)

    def account_email_button(self):
        self.do_click(self.Account_Button)

    def Email_button_click(self):
        self.do_click(self.Email_change_button)

    def get_email_copy(self):
        self.get_window(0)
        self.do_click(self.Change_button)
        self.do_click(self.alert_check)
        return self.get_element_value(self.New_Email)

    def get_email_change(self):
        Email = self.get_email_copy()
        self.get_window(1)
        self.do_send_keys(self.Current_pass, TestData.LOGIN_PASSWORD)
        self.do_send_keys(self.New_Email_input, Email)
        self.do_send_keys(self.Confirm_Email_input, Email)
        self.do_click(self.Update_button)
        self.get_window(0)
