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


class AddtoQueue(Basepage):
    Dots = (By.XPATH, "//div[@class='dots']")
    View_workspace = (By.XPATH, "//button[contains(text(),'View Workspace')]")
    Queue_button = (By.XPATH, "//button[contains(text(),'Add To Queue')]")
    Influencer_email = (By.XPATH, "//input[@id='influencer-email']")
    Dropdown_content = (
        By.XPATH,
        "//span[@class ='text text--gray text--uppercase text--bold ']",
    )
    Selection = (By.XPATH, "//button[contains(text(),'Social')]")
    Cost = (By.XPATH, "//input[@id='content-cost']")
    TextArea = (By.XPATH, "//textarea[@class='fancyScroll']")
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Workspace_dashboard = (By.XPATH, "//div[@class ='gridRow rowHover ']")
    Workspace_click = (By.XPATH, "//button[contains(text(),'WorkSpace')]")
    queueOnboard = (
        By.XPATH,
        "//div[@class='ahalogist-workspace-card ahalogistWorkspaceQueueCard ']//button[contains(text(),'Onboard Influencer')]",
    )
    Content_type = (By.XPATH, "//div[@class='brandableType']//span")
    Socail_type = (By.XPATH, "//button[contains(text(),'Social')]")
    line_item = (By.XPATH, "//div[@class='lineItem ']//span")
    line_item_type = (
        By.XPATH,
        "//div[@class = 'wrapper ahalogistWorkspaceCardPopoverEditField']//button",
    )
    queue_selection = (By.XPATH, "//div[@class ='workspace-tabs']//div[1]")
    upload_brief = (By.XPATH, "//input[@id='newPostBrief']")
    draft_date = (By.XPATH, "//input[@id='calendar-input-draftDueDateNew']")
    publish_date = (By.XPATH, '//input[@id="calendar-input-publishDateNew"]')
    Onboard_msg = (By.XPATH, "//div[@class='onboarded']")
    influncers_queue = (
        By.XPATH,
        "//button[contains(text(),'Onboard Influencer')]",
    )
    Scroll_to_element = (By.XPATH, "//div[@class='item']")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

    def add_to_queue_influence(self):
        Add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Search_item)
        )
        if "staging" in self.driver.current_url:
            Add.send_keys(f"{TestData.Campaign_name}", Keys.ENTER)
        else:
            Add.send_keys(f"{TestData.Campaign_prod_name}", Keys.ENTER)
        time.sleep(5)
        actions = ActionChains(self.driver)
        Hovering_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Workspace_dashboard)
        )
        # Perform the hover action
        actions.move_to_element(Hovering_element).perform()
        self.do_click(self.Workspace_click)
        time.sleep(2)
        if len(self.driver.window_handles) < 3:
            self.get_window(1)
        else:
            self.get_window(2)
        count = 1
        while True:
            if os.environ.get("Email"):
                self.do_click(self.Queue_button)
                time.sleep(2)
                self.do_send_keys(self.Influencer_email, os.environ.get("Email"))
                time.sleep(3)
                self.do_click(self.Dropdown_content)
                self.do_click(self.Selection)
                self.do_send_keys(self.Cost, "12")
                time.sleep(3)
                Element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.TextArea)
                )
                Element.send_keys("TestingQA", Keys.TAB, Keys.TAB, Keys.ENTER)
                msg = self.get_element_text(self.Onboard_msg)
                if msg == TestData.Add_to_queue_msg:
                    Onboard_influ = self.get_elements(self.influncers_queue)
                    try:
                        for element in Onboard_influ:
                            self.driver.execute_script("arguments[0].click();", element)
                            break
                        # time.sleep(2)
                        # self.do_click(self.Content_type)
                        # time.sleep(2)
                        # self.do_click(self.Socail_type)
                        time.sleep(5)
                        self.do_click(self.line_item)
                        time.sleep(2)
                        self.do_click(self.line_item_type)
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
                        time.sleep(3)

                        Onboard = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//button[contains(text(),'Cancel')]")
                            )
                        )
                        self.scroll_to_add(Onboard)
                        time.sleep(2)
                        Onboard.send_keys(Keys.TAB, Keys.ENTER)

                        msg = (
                            WebDriverWait(self.driver, 30)
                            .until(EC.visibility_of_element_located(self.Onboard_msg))
                            .text
                        )
                    except TimeoutException:
                        self.driver.refresh()
                        count += 1
                        if count > 3:
                            assert False
                    return msg == TestData.Onboarded_MSG

            elif os.environ.get("Emai"):
                self.do_click(self.Queue_button)
                time.sleep(2)
                self.do_send_keys(self.Influencer_email, os.environ.get("Emai"))
                self.do_click(self.Dropdown_content)
                self.do_click(self.Selection)
                self.do_send_keys(self.Cost, "12")
                time.sleep(3)
                Element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.TextArea)
                )
                Element.send_keys("TestingQA", Keys.TAB, Keys.TAB, Keys.ENTER)
                msg = self.get_element_text(self.Onboard_msg)
                if msg == TestData.Add_to_queue_msg:
                    Onboard_influ = self.get_elements(self.influncers_queue)
                    try:
                        for element in Onboard_influ:
                            self.driver.execute_script("arguments[0].click();", element)
                            break
                        time.sleep(2)
                        self.do_click(self.Content_type)
                        time.sleep(2)
                        self.scroll_to_line(self.get_element(self.Scroll_to_element))
                        self.do_click(self.Socail_type)
                        time.sleep(2)
                        self.do_click(self.line_item)
                        time.sleep(2)
                        self.do_click(self.line_item_type)
                        self.driver.find_element(
                            By.XPATH, "//input[@id='newPostBrief']"
                        ).send_keys(f"{os.getcwd()}/Testing.pdf")
                        time.sleep(10)
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
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys("12")
                        time.sleep(1)
                        self.driver.find_element(
                            By.XPATH, "//input[@id ='content-cost']"
                        ).send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
                        msg = (
                            WebDriverWait(self.driver, 30)
                            .until(EC.visibility_of_element_located(self.Onboard_msg))
                            .text
                        )
                    except TimeoutException:
                        self.driver.refresh()
                        count += 1
                        if count > 3:
                            return False
                    return msg == TestData.Onboarded_MSG

            break
