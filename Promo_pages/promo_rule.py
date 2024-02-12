import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Promo_pages.BasePages import Basepages


class PromoRule(Basepages):
    Promo_button = (By.XPATH,"//a[@title='Promo Amp']")
    Add_rule = (By.XPATH,"//qbc-icon-button[@title='New Promo Amp Product Family']")
    Rule_name =(By.XPATH,"//qbc-form-field[@label='Name']//input")
    Select =  (By.XPATH,"//qbc-form-field[@label='Retailer']//qbc-select")
    value_select  =(By.XPATH,"//qbc-list-box//span[2]")
    Save = (By.XPATH,"//div[@class='form-header__right-section']//button")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def Rule(self):
        try:
            self.do_click(self.Promo_button)
            self.do_click(self.Save)
            time.sleep(5)
            return True
        except TimeoutException:
            return False
