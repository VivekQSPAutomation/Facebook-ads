import datetime
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Config.config import TestData
from Promo_pages.BasePages import Basepages


class Lineitem(Basepages):
    line_button =(By.XPATH, "//a[@title='Line Items']")
    Plus_sign = (By.XPATH, "//qbc-icon-button[@title='New Line Item']")
    line_name = (By.XPATH, "//qbc-form-field[@label='Name']//input")
    retailer_type = (By.XPATH, "//qbc-label[contains(text(),' Retailer type')]/..//qbc-select//qbc-textual-field-frame")
    Select = (By.XPATH, "(//qbc-option)[2]")
    retailer_add  = (By.XPATH,"//div[contains(text(),'Add retailer')]")
    retailer_select = (By.XPATH,"(//ubs-grid-selection-cell)[1]")
    Save_retail = (By.XPATH,"(//div[contains(text(),'Save')])[2]")
    Save_line = (By.XPATH,"(//div[contains(text(),'Save')])[1]")
    target_imp = (By.XPATH,"//qbc-label[contains(text(),'Target impressions')]/..//input")
    Product_family = (By.XPATH,"//qbc-form-field[@label='Product family']//input")
    Retailer_id = (By.XPATH,"//qbc-form-field[@label='Retailer id']//input")
    Retailer_banner_code = (By.XPATH,"//qbc-form-field[@label='Retailer banner code']//input")
    offer_price = (By.XPATH,"//qbc-form-field[@label='Offer price']//input")
    Offer_end_date = (By.XPATH,"//qbc-form-field[@label='Offer end date']//ubs-svg-icon")
    date_check = datetime.date.today()
    new_date = date_check - datetime.timedelta(days=2)
    formatted_end_date = new_date.strftime('%-m/%d/%y')
    day_selection_end = (By.XPATH,
                         f"//div[@class='calendar-field-frame__calendar-wrapper ng-star-inserted']//following-sibling::div[@class='k-days']//span[@data-date='{formatted_end_date}'and @class='k-in-month k-active']")
    cta = (By.XPATH,"//qbc-form-field[@label='Call to action']//input")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def line(self):
        self.do_click(self.line_button)
        self.do_click(self.Plus_sign)
        self.get_clear(self.line_name)
        self.do_send_keys(self.line_name,TestData.Line_name)
        time.sleep(4)
        # retailer_type = "//qbc-label[contains(text(),' Retailer type')]/..//qbc-select//qbc-textual-field-frame"
        # self.driver.execute_script(
        #     "document.evaluate(\"" + retailer_type + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
        #
        self.do_click(self.retailer_type)
        self.do_click(self.Select)
        self.do_click(self.retailer_add)
        self.do_click(self.retailer_select)
        self.do_click(self.Save_retail)
        self.do_send_keys(self.target_imp,TestData.Target)
        self.do_send_keys(self.Product_family,TestData.product)
        self.do_send_keys(self.Retailer_id,TestData.Retailer_id)
        self.do_send_keys(self.Retailer_banner_code,TestData.banner_code)
        self.do_send_keys(self.offer_price,TestData.offer_price)
        self.do_click(self.Offer_end_date)
        self.do_click(self.day_selection_end)
        self.do_send_keys(self.cta,TestData.cta)
        self.do_click(self.Save_line)
        time.sleep(5)




