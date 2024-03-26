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


class Filter(Basepage):
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Dots = (By.XPATH, "//div[@class='dots']")
    Edit_campaign = (By.XPATH, "//a[contains(text(),'Archive')]/../a[1]")
    filter = (By.XPATH, "//h3[contains(text(),'Filtered Dashboard')]")
    add_dashboard = (By.XPATH, "//li[contains(text(),'+ Add Dashboard')]")
    dashboard_name = (By.XPATH, "//input[@id='name']")
    mediabudget = (By.XPATH, "//input[@id='mediaBudget']")
    imp_count = (By.XPATH, "//input[@id='impressionGoal']")
    social_influencer = (By.XPATH, "//span[contains(text(),'Social Influencer')]/../input")
    total_enagage = (By.XPATH, "//span[contains(text(),'Total Engagements')]/../input")
    total_click = (By.XPATH, "//span[contains(text(),'Total Clicks')]/../input")
    click_through = (By.XPATH, "//span[contains(text(),'Click Through Rate')]/../input")
    enagage_rate = (By.XPATH, "//span[contains(text(),'Engagement Rate')]/../input")
    Save = (By.XPATH, "(//button[contains(text(),'Save')])[1]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

    def filterdash(self):
        Add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Search_item)
        )

        if "staging" in self.driver.current_url:
            Add.send_keys(f"{TestData.Campaign_name}", Keys.ENTER)
        else:
            Add.send_keys(f"{TestData.Campaign_prod_name}", Keys.ENTER)
        time.sleep(10)
        self.do_click(self.Dots)
        self.do_click(self.Edit_campaign)
        self.get_window(-1)
        time.sleep(20)
        # self.do_element_click(self.filter)
        self.do_click(self.add_dashboard)
        self.get_clear(self.dashboard_name)
        self.do_send_keys(self.dashboard_name, TestData.Filtername)
        self.get_clear(self.mediabudget)
        self.do_send_keys(self.mediabudget, TestData.mediaBudget)
        self.get_clear(self.imp_count)
        self.do_send_keys(self.imp_count, TestData.imp_count)
        social_influencers = self.driver.find_element(By.XPATH,"(//div[contains(@class, 'relative')]//input[@type='checkbox'][1])[1]")
        self.driver.execute_script("arguments[0].click();", social_influencers)
        total_enagagement = self.driver.find_element(By.XPATH,"(//div[contains(@class, 'relative')]//input[@type='checkbox'][1])[3]")
        self.driver.execute_script("arguments[0].click();", total_enagagement)
        total_clicks = self.driver.find_element(By.XPATH,"(//div[contains(@class, 'relative')]//input[@type='checkbox'][1])[4]")
        self.driver.execute_script("arguments[0].click();", total_clicks)
        click_through = self.driver.find_element(By.XPATH,"(//div[contains(@class, 'relative')]//input[@type='checkbox'][1])[5]")
        self.driver.execute_script("arguments[0].click();", click_through)
        enagagement_rate = self.driver.find_element(By.XPATH,"(//div[contains(@class, 'relative')]//input[@type='checkbox'][1])[6]")
        self.driver.execute_script("arguments[0].click();", enagagement_rate)
        self.do_click(self.Save)
        msg_value = (
            WebDriverWait(self.driver, 20)
            .until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class ='banner banner-success ']")
                )
            )
            .text
        )
        if msg_value == TestData.filter_dash:
            assert True
        else:
            assert False
