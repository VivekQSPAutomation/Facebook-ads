import datetime
import os
import time
from datetime import date

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData
from Influncers_pages.DirectoryRefresh import remove_files_in_directory


class onboardInfluencers(Basepage):
    Application_selection = (By.XPATH, '//h3[contains(text(),"Short")]')
    Dots = (By.XPATH, "//div[@class='dots']")
    View_workspace = (By.XPATH, "//button[contains(text(),'View Workspace')]")
    Onboard_inf = (By.XPATH, "//button[@id='addPost']")
    Influncer_email = (By.ID, "influencer-email")
    Content_type = (By.XPATH, "//div[@class='brandableType']//span")

    line_item = (By.XPATH, "//div[@class='lineItem ']//span")
    line_item_type = (
        By.XPATH,
        "//div[@class = 'wrapper ahalogistWorkspaceCardPopoverEditField']//button",
    )
    upload_brief = (By.XPATH, "//input[@id='newPostBrief']")
    draft_date = (By.XPATH, "//input[@id='calendar-input-draftDueDateNew']")
    publish_date = (By.XPATH, '//input[@id="calendar-input-publishDateNew"]')
    content_cost = (By.XPATH, "//input[@id ='content-cost']")
    Onboard_button = (
        By.XPATH,
        "//button[@class ='text text--uppercase text--bold border']",
    )

    Onboard_msg = (By.XPATH, "//div[@class='onboarded']")
    error_Onboard_msg = (By.XPATH, "//div[@class='banner banner-error ']")

    # Scroll_to_element = (By.XPATH, "//input[@id='influencer-email']/../../..")
    Scroll_to_element = (By.XPATH, "//div[@class='item']")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(
            f"{TestData.env_setup(self)}/applications/dashboard?message=&messageType="
        )

    def Onboard_influencers(self, data):
        global check
        lis = []
        line_count = 1
        count = 1
        if self.get_element(self.Application_selection):
            time.sleep(3)
            self.do_click(self.Dots)
            self.do_click(self.View_workspace)
        while True:
            try:
                if line_count > len(lis) and line_count != 1:
                    break
                else:
                    if os.environ.get("Email"):
                        self.do_click(self.Onboard_inf)
                        time.sleep(2)
                        self.do_send_keys(self.Influncer_email, os.environ.get("Email"))
                        time.sleep(2)
                        self.do_click(self.Content_type)
                        self.scroll_to_line(self.get_element(self.Scroll_to_element))
                        self.do_click(
                            (By.XPATH, f"//button[contains(text(),'{data}')]")
                        )
                        self.do_click(self.line_item)
                        if not lis:
                            lis = [
                                line for line in self.get_elements(self.line_item_type)
                            ]
                        # self.scroll_to_line(self.get_element(self.Scroll_to_element))
                        self.do_click(
                            (
                                By.XPATH,
                                f"//div[@class = 'wrapper ahalogistWorkspaceCardPopoverEditField']//button[{line_count}]",
                            )
                        )

                        self.driver.find_element(
                            By.XPATH, "//input[@id='newPostBrief']"
                        ).send_keys(f"{os.getcwd()}/Testing.pdf")
                        self.do_send_keys(
                            self.draft_date, date.today().strftime("%m/%d/%Y")
                        )
                        self.get_clear(self.publish_date)
                        self.do_send_keys(
                            self.publish_date,
                            (
                                datetime.date.today() + datetime.timedelta(weeks=3)
                            ).strftime("%m/%d/%Y"),
                        )
                        time.sleep(2)
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys("12")
                        time.sleep(1)
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
                        # if line_count == 1:
                        #     check = self.error_check()
                        #     if check:
                        #         return False
                        #     else:
                        #         pass
                        # else:
                        #     pass
                        msg = (
                            WebDriverWait(self.driver, 50)
                            .until(EC.visibility_of_element_located(self.Onboard_msg))
                            .text
                        )

                        if msg == TestData.Onboarded_MSG:
                            line_count += 1
                            self.driver.refresh()
                    elif os.environ.get("Emai"):
                        self.do_click(self.Onboard_inf)
                        time.sleep(2)
                        self.do_send_keys(self.Influncer_email, os.environ.get("Emai"))
                        time.sleep(2)
                        self.do_click(self.Content_type)
                        self.scroll_to_line(self.get_element(self.Scroll_to_element))
                        self.do_click(
                            (By.XPATH, f"//button[contains(text(),'{data}')]")
                        )
                        self.do_click(self.line_item)
                        if not lis:
                            lis = [
                                line for line in self.get_elements(self.line_item_type)
                            ]

                        # self.scroll_to_line(self.get_element(self.Scroll_to_element))
                        self.do_click(
                            (
                                By.XPATH,
                                f"//div[@class = 'wrapper ahalogistWorkspaceCardPopoverEditField']//button[{line_count}]",
                            )
                        )

                        self.driver.find_element(
                            By.XPATH, "//input[@id='newPostBrief']"
                        ).send_keys(f"{os.getcwd()}/Testing.pdf")
                        self.do_send_keys(
                            self.draft_date, date.today().strftime("%m/%d/%Y")
                        )
                        self.get_clear(self.publish_date)
                        self.do_send_keys(
                            self.publish_date,
                            (
                                datetime.date.today() + datetime.timedelta(weeks=3)
                            ).strftime("%m/%d/%Y"),
                        )
                        time.sleep(2)
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys("12")
                        time.sleep(1)
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys(Keys.TAB, Keys.TAB, Keys.RETURN)
                        # if line_count == 1:
                        #     check = self.error_check()
                        #     if check:
                        #         return False
                        #     else:
                        #         pass
                        # else:
                        #     pass
                        msg = (
                            WebDriverWait(self.driver, 50)
                            .until(EC.visibility_of_element_located(self.Onboard_msg))
                            .text
                        )
                        if msg == TestData.Onboarded_MSG:
                            line_count += 1
                            self.driver.refresh()
            except StaleElementReferenceException:
                continue
            except TimeoutException:
                self.driver.refresh()
                remove_files_in_directory(f"{os.getcwd()}/screenshots")
                count += 1
                if count > 3:
                    return False

    def error_check(self):
        error_msg = (
            WebDriverWait(self.driver, 15)
            .until(EC.visibility_of_element_located(self.error_Onboard_msg))
            .text
        )
        print(error_msg)
        if error_msg:
            return True
        else:
            return False
