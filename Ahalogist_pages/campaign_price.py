import datetime
import os
import time
from datetime import date

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Campprice(Basepage):
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Dots = (By.XPATH, "//div[@class='dots']")
    Edit_campaign = (By.XPATH, "//a[contains(text(),'Archive')]/../a[1]")
    campaign_price = (
        By.XPATH,
        "//div[@class='sf-opportunities-details']//p[contains(text(),'Campaign Price')]/..//p[@class='text text--uppercase']",
    )

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

    def price(self, data):
        Add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Search_item)
        )

        if "staging" in self.driver.current_url:
            Add.send_keys(f"{data}", Keys.ENTER)
        else:
            Add.send_keys(f"{TestData.Campaign_prod_name}", Keys.ENTER)
        time.sleep(10)
        self.do_click(self.Dots)
        self.do_click(self.Edit_campaign)
        self.get_window(-1)
        self.scroll_to(self.get_element(self.campaign_price),100)
        price = self.get_element_text(self.campaign_price)
        camp_price = int(price[1:].replace(",", ""))
        print(camp_price)
        if camp_price > 1:
            return True
        else:
            return False
