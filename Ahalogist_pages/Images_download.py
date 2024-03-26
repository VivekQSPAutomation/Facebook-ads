import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Images(Basepage):
    Images_click = (By.XPATH, "//div[contains(text(),'Images')]")
    Select = (By.XPATH, "//div[@class='send-to-client-wrapper']//label")
    Download_button = (By.XPATH, "//a[contains(text(),'DOWNLOAD')]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/asset-library")

    def imagedownload(self):
        try:
            self.do_click(self.Images_click)
            self.do_click(self.Select)
            for _ in range(3, 7):
                self.do_click((By.XPATH,
                               f"(//div[@class='text text--uppercase text--bold select-checkbox-container']//label)[{_}]"))
            self.do_click(self.Download_button)
            time.sleep(8)
        except StaleElementReferenceException:
            self.driver.refresh()
