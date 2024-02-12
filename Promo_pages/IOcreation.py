import datetime
import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Promo_pages.BasePages import Basepages


class IOcreation(Basepages):
    Search = (By.XPATH, "//input[@placeholder='Search']")
    Click_on =(By.XPATH,"//div[@title='Promo QA']/parent::a")
    IOs = (By.XPATH,"//a[@title='IOs']")
    New_IO = (By.XPATH,"//qbc-icon-button[@title='New IO']//a")
    IOName=(By.XPATH,"//qbc-form-field[@label='Name']//input")
    date_check = datetime.date.today()
    format_date =date_check.strftime('%-m/%d/%y')
    new_date = date_check + datetime.timedelta(days=10)
    formatted_end_date = new_date.strftime('%-m/%d/%y')
    Calender= (By.XPATH,"(//qbc-form-field//span[@class='textual-field__icon-proj']//ubs-svg-icon)[1]")
    day_selection_start = (By.XPATH,f"//div[@class='calendar-field-frame__calendar-wrapper ng-star-inserted']//following-sibling::div[@class='k-days']//span[@data-date='{format_date}'  and @class='k-selected k-range-start k-in-month k-active k-today']")
    day_selection_end = (By.XPATH,f"//div[@class='calendar-field-frame__calendar-wrapper ng-star-inserted']//following-sibling::div[@class='k-days']//span[@data-date='{formatted_end_date}'and @class='k-in-month k-active']")
    Budget =(By.XPATH,"//qbc-form-field[@label = 'Budget ($)']//input")
    Save = (By.XPATH,"//div[@class='form-header__right-section']//button")


    def __init__(self, ses_init):
        super().__init__(ses_init)

    def IOcreate(self):
        try:
            self.do_send_keys(self.Search, "Promo QA")
            self.do_click(self.Click_on)
            self.do_click(self.IOs)
            self.do_click(self.New_IO)
            self.get_clear(self.IOName)
            self.do_send_keys(self.IOName,TestData.IO_name)
            self.do_click(self.Calender)
            print(self.day_selection_start)
            print(self.day_selection_end)
            self.do_click(self.day_selection_start)
            self.do_click(self.day_selection_end)
            if os.environ.get('exc') == "--headless":
                time.sleep(3)
                self.do_click(self.IOName)
            else:
                self.do_click(self.Budget)

            self.do_send_keys(self.Budget,"1")
            self.do_click(self.Save)
            return True
        except TimeoutException:
            return False
