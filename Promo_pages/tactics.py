import datetime
import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Promo_pages.BasePages import Basepages


class Tactics(Basepages):
    Tactics_button =(By.XPATH, "//a[@title='Tactics']")
    Plus_sign = (By.XPATH, "//qbc-icon-button[@title='New Tactic']")
    Tactics_name = (By.XPATH,"//qbc-form-field[@label='Name']//input")
    Tactics_imp  =(By.XPATH,"//qbc-label[contains(text(),'Target impressions')]/..//input")
    Save = (By.XPATH, "(//div[contains(text(),'Save')])")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def tactics(self):
        self.do_click(self.Tactics_button)
        self.do_click(self.Plus_sign)
        self.get_clear(self.Tactics_name)
        self.do_send_keys(self.Tactics_name,TestData.Tactics_name)
        self.do_send_keys(self.Tactics_imp,TestData.Tactics_imp)
        self.do_click(self.Save)
        time.sleep(10)
