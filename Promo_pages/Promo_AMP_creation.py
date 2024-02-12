import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Promo_pages.BasePages import Basepages


class PromoAMP(Basepages):
    enable_promo =(By.XPATH,"//qbc-form-field[@label='Enabled']//button//ubs-svg-icon")
    Promo_amp = (By.XPATH, "//a[@title='Promo Amp']")
    Plus_sign = (By.XPATH, "//qbc-icon-button[@iconname='plus']")
    Promo_name = (By.XPATH, "//qbc-form-field[@label='Name']//input")
    Retailer_select = (By.XPATH, "//qbc-select")
    # Click_retailer = (By.XPATH,"//qbc-option")
    produts = (By.XPATH, "//qbc-textarea//textarea")
    validate = (By.XPATH, "//div[contains(text(),'Validate')]/../../..")
    Search_audiences = (By.XPATH, "(//qbc-search-list//input)[1]")
    Select = (By.XPATH, "(//qbc-option)[1]")
    All_shoppers = (By.XPATH, "(//button[@class='qbc-button__button --large --link ng-star-inserted'])[1]")
    Store_visit = (By.XPATH, "//div[contains(text(),'Include')]")
    trans_local = (By.XPATH, "(//div[@class='checkbox-frame__checkbox-container'])[3]")
    impression_value = (By.XPATH, "//qbc-form-field[@label ='Target impressions']//input")
    cpm = (By.XPATH, "//qbc-form-field[@label ='Max CPM ($)']//input")
    Banner_add = (By.XPATH, "//div[contains(text(),'Add New')]")
    select_banner = (By.XPATH, "//promo-amp-banner-list//qbc-fields-row//qbc-select")
    week_count = (By.XPATH, "//promo-amp-banner-list//qbc-fields-row//input")
    Creative_select = (By.XPATH, "//qbc-label[contains(text(),' IO creatives (320X50)')]/..//qbc-textual-field-frame")
    cta = (By.XPATH, "//qbc-label[contains(text(),'Giant Food Stores')]/..//input")
    Save = (By.XPATH, "(//div[contains(text(),'Save')])[2]")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def promoamp(self):
        self.do_click(self.Promo_amp)
        self.do_click(self.Plus_sign)
        self.do_send_keys(self.Promo_name, TestData.Promoname)
        self.do_click(self.Retailer_select)
        self.do_click(self.Select)
        self.do_send_keys(self.produts, TestData.Pro)
        time.sleep(4)
        self.do_click(self.validate)
        time.sleep(4)
        self.do_send_keys(self.Search_audiences, TestData.audi)
        self.do_click(self.Select)
        self.do_click(self.All_shoppers)
        time.sleep(2)
        self.do_click(self.Store_visit)
        self.do_click(self.trans_local)
        self.do_send_keys(self.impression_value, TestData.imp)
        self.do_send_keys(self.cpm, TestData.cpm)
        self.do_click(self.Banner_add)
        self.do_click(self.select_banner)
        self.do_click(self.Select)
        self.do_send_keys(self.week_count, TestData.Week)
        self.do_click(self.Creative_select)
        self.do_click(self.Creative_select)
        self.do_click(self.Select)
        self.do_send_keys(self.cta, TestData.cta)
        self.do_click(self.enable_promo)
        time.sleep(5)
        self.do_click(self.Save)
        time.sleep(10)
