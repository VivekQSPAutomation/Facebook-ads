import os
import time
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Performance(Basepages):
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Date_selection = (
        By.XPATH,
        "//div[@class='subheaderWrapper']//div[@class='filter text text--uppercase text--gray text--center text--bold text--p75rem ']",
    )
    start_Date = (By.XPATH, "//input[@id='calendar-input-startDate']")
    end_date = (By.XPATH, "//input[@id='calendar-input-endDate']")
    date_range = (By.XPATH, "//button[contains(text(),'View Date')]")
    campaign_selection = (
        By.XPATH,
        "//div[@class='subheaderWrapper']//div[@class='filter text text--uppercase text--gray text--center text--bold text--p75rem'][2]",
    )
    All_campaign = (By.XPATH, "//a[contains(text(),'All Campaign')]")
    csv_button = (
        By.XPATH,
        "//div[@class='subheaderWrapper']//div[@class='filter text text--uppercase text--gray text--center text--bold text--p75rem'][3]",
    )
    download_button = (By.XPATH, "//a[contains(text(),'Download CSV')]")
    campaign_search = (By.XPATH, "//input[@id='campaignSearchInput']")
    campaign_name = (By.XPATH,"//div[@class='text campaignName']")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

    def peformance_dashboard(self):
        Add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Search_item)
        )
        if os.environ.get('Env') == "Prod":
            Add.send_keys(f"{TestData.Campaign_prod_name}", Keys.ENTER)
        else:
            Add.send_keys(f"{TestData.Campaign_performance_name}", Keys.ENTER)
        time.sleep(5)
        campaign = self.get_element_text(self.campaign_name)
        page_source = self.driver.page_source
        dates_found = []
        for text in page_source.split():
            try:
                date_obj = datetime.strptime(text, "%m/%d/%Y")
                dates_found.append(date_obj.strftime("%m/%d/%Y"))
            except ValueError:
                continue
        print(dates_found)
        self.driver.get(
            f"{TestData.env_setup(self)}/campaigns/dashboard"
        )
        self.do_click(self.Date_selection)
        self.get_clear(self.start_Date)
        self.do_send_keys(self.start_Date, dates_found[1])
        self.get_clear(self.end_date)
        self.do_send_keys(self.end_date, dates_found[2])
        self.do_click(self.date_range)
        # self.do_click(self.campaign_selection)
        # self.do_click(self.All_campaign)
        self.do_send_keys(self.campaign_search, campaign)
        time.sleep(10)
        self.do_click(self.csv_button)
        self.do_click(self.download_button)
        time.sleep(10)
        return True
