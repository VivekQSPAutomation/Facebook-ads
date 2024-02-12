import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Promo_pages.BasePages import Basepages


class Enable(Basepages):
    Enable= (By.XPATH,"//div[@class='checkbox-frame__checkbox-container']")
    Save = (By.XPATH,"//div[@class='form-header__right-section']//button")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def Enablepromo(self):
        try:
            self.do_click(self.Enable)
            self.do_click(self.Save)
            time.sleep(5)
            return True
        except TimeoutException:
            return False
