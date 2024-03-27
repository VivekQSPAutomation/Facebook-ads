import datetime
import os
import secrets
import string
import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class Dycall(Basepages):
    DRC_name = (By.XPATH, "//input[@placeholder ='DRC Name']")
    Callout_button = (By.XPATH, "//button[contains(text(),'Create New')]")
    DRC_table_name = (By.XPATH, "(//tbody/tr/td)[1]")
    Csv_file = (By.XPATH, "//input[@type='file' and @accept='.csv']")
    Zip_file = (By.XPATH, "//input[@type='file' and @accept='.zip']")
    link_url = (
        By.XPATH,
        "//label[contains(text(),'In-line DRC Text')]/following-sibling::input",
    )
    Download_image = (By.XPATH, "//button[contains(text(),'Download Image')]")
    Download_inline = (
        By.XPATH,
        "//button[contains(text(),'Download In-Line Snippet')]",
    )

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/dynamiccallout")

    def dynamic_callout(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d %b")
        self.do_send_keys(
            self.DRC_name,
            f"Test-check_{''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))}_{formatted_datetime}",
        )
        self.do_click(self.Callout_button)
        time.sleep(3)
        self.do_click(self.DRC_table_name)
        self.do_send_keys(self.Csv_file, f"{os.getcwd()}/testing.csv")
        self.do_send_keys(self.Zip_file, f"{os.getcwd()}/testing.zip")
        self.do_send_keys(self.link_url, "https://google.com")
        time.sleep(5)
        self.do_click(self.Download_image)
        time.sleep(5)
        self.do_click(self.Download_inline)
