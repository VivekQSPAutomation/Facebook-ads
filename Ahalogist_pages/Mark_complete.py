import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class MarkComplete(Basepage):
    search_influence = (By.XPATH, "//input[@id='searchInput']")
    Dots = (By.XPATH, "//div[@class='container    ']//div[@class='dots']")
    Mark_Draft = (By.XPATH, "//button[contains(text(),'Mark Draft Complete')]")
    completed_comment = (
        By.XPATH,
        "//textarea[@placeholder='add a custom message to the email...']",
    )
    mark_completed = (
        By.XPATH,
        "//button[contains(text(),'Mark Complete')]",
    )
    Workspace_click = (By.XPATH, "//button[contains(text(),'WorkSpace')]")
    Edits = (
        By.XPATH,
        "//button[@class='text text--uppercase text--bold btn btn--emptyBorder']",
    )
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Workspace_dashboard = (By.XPATH, "//div[@class ='gridRow rowHover ']")
    all_draft = (
        By.XPATH,
        "//div[contains(text(),'Draft Locked')]/..//div[contains(., 'Type')]/following-sibling::div[@class='text']/span",
    )
    review_draft_tab = (By.XPATH, "(//div[@class='workspace-tabs']//div)[4]")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def search(self):
        if os.environ.get("Email"):
            search = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.search_influence)
            )
            search.send_keys(os.environ.get("Email"), Keys.ENTER)
        else:
            search = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.search_influence)
            )
            search.send_keys(os.environ.get("Emai"), Keys.ENTER)

    def mark_complete(self):
        locatar, xpath = self.all_draft
        time.sleep(2)
        print(len(self.get_window_count()))
        if len(self.get_window_count()) < 4:
            self.get_window(2)
        else:
            self.get_window(3)
        self.driver.refresh()
        time.sleep(5)
        self.do_click(self.review_draft_tab)
        time.sleep(4)
        self.do_click(self.Dots)
        self.do_click(self.Mark_Draft)
        self.do_send_keys(self.completed_comment, "Testing QA", Keys.TAB, Keys.ENTER)
        time.sleep(15)
        return True


