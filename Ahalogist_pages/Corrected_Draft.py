import os
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Corrected_draft(Basepage):
    search_influence = (By.XPATH, "//input[@id='searchInput']")
    Dots = (By.XPATH, "//div[@class='dots']")
    View_draft = (
        By.XPATH,
        "//div[@class='wrapper ahalogistWorkspaceCardPopover fixedWidth']//button[contains(text(),'View Draft')]",
    )
    select_text = (By.XPATH, "//div[@id='editor']//p[contains(text(),'Testing')]")
    add_comment = (By.XPATH, "//textarea[@placeholder='Attach a comment...']")
    send_comment = (By.XPATH, "//button[contains(text(),'Attach Comment')]")
    Save_draft = (By.XPATH, "//span[contains(text(),'Save')]")
    Send_edits = (By.XPATH, "//button[contains(text(),'Send')]")
    Edit_comments = (
        By.XPATH,
        "//textarea[@placeholder = 'add a custom message to the email...']",
    )
    Search_item = (By.XPATH, "//input[@id='jobTrackerSearchInput']")
    Workspace_dashboard = (By.XPATH, "//div[@class ='gridRow rowHover ']")
    Workspace_click = (By.XPATH, "//button[contains(text(),'WorkSpace')]")
    Edits = (
        By.XPATH,
        "//button[@class='text text--uppercase text--bold btn btn--emptyBorder']",
    )
    Msg = (By.XPATH, "//div[@class='bannerMessage ']")

    Success_msg = (By.XPATH, "//div[@class='banner banner-success ']")
    all_draft = (
        By.XPATH,
        "//div[contains(text(),'Draft Locked')]/..//div[contains(., 'Type')]/following-sibling::div[@class='text']/span",
    )
    review_draft_tab = (By.XPATH, "(//div[@class='workspace-tabs']//div)[4]")
    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

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

    def draft_correction(self):
        try:
            locatar, xpath = self.all_draft
            Add = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.Search_item)
            )
            if "staging" in self.driver.current_url:
                Add.send_keys(f"{TestData.Campaign_name}")
                Add.send_keys(Keys.ENTER)
                time.sleep(5)

            else:
                Add.send_keys(f"{TestData.Campaign_prod_name}")
                time.sleep(3)
                Add.send_keys(Keys.ENTER)
                time.sleep(5)

            time.sleep(2)
            actions = ActionChains(self.driver)
            Hovering_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.Workspace_dashboard)
            )
            actions.move_to_element(Hovering_element).perform()
            self.do_click(self.Workspace_click)
            time.sleep(4)
            if len(self.get_window_count()) < 4:
                self.get_window(2)
            else:
                self.get_window(3)

            self.do_click(self.review_draft_tab)
            time.sleep(8)
            ### improved code
            self.do_click(self.Dots)
            self.do_click(self.View_draft)
            element = self.get_element(self.select_text)
            element.click()
            element.send_keys(Keys.HOME)
            text_length = len("Testing")
            for _ in range(text_length):
                element.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
                time.sleep(0.1)
            time.sleep(2)
            elements = self.get_elements(self.add_comment)
            elements[0].send_keys("Correct this stuff")
            self.do_click(self.send_comment)
            time.sleep(1)
            self.do_click(self.Save_draft)
            msg = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.Msg)
            )
            if msg.text == TestData.Draft_saved:
                self.driver.refresh()
                self.do_click(self.review_draft_tab)
                time.sleep(2)
                self.do_click(self.Dots)
                self.do_click(self.Send_edits)
                Edits = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(self.Edit_comments)
                )
                Edits.send_keys("Resolved this", Keys.TAB, Keys.TAB, Keys.ENTER)
                banner_msg = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.Success_msg)
                )
                if banner_msg == TestData.DRAFT_MSG:
                    assert True

            else:
                assert False

            ###ends
        #     social_draft_location = self.get_elements(self.all_draft)
        #     self.driver.save_screenshot('headless_screenshot.png')
        #     for draft in social_draft_location:
        #         if draft.text == "Social":
        #             print(count)
        #             child = self.get_element(
        #                 (By.XPATH, f"(//div[contains(text(),'Draft Locked')]/ancestor::div[@class='item'])[{count}]//button")
        #             )
        #             self.scroll_to(child, 100)
        #             time.sleep(2)
        #             child.click()
        #             element = self.get_element(self.select_text)
        #             element.click()
        #             element.send_keys(Keys.HOME)
        #             text_length = len("Testing")
        #             for _ in range(text_length):
        #                 element.send_keys(Keys.SHIFT + Keys.ARROW_RIGHT)
        #                 time.sleep(0.1)
        #             time.sleep(2)
        #             elements = self.get_elements(self.add_comment)
        #             elements[0].send_keys("Correct this stuff")
        #             self.do_click(self.send_comment)
        #             time.sleep(1)
        #             self.do_click(self.Save_draft)
        #             msg = WebDriverWait(self.driver, 30).until(
        #                 EC.visibility_of_element_located(self.Msg)
        #             )
        #             self.driver.refresh()
        #             self.search()
        #             time.sleep(8)
        #             dots = self.get_element(
        #                 (
        #                     By.XPATH,
        #                     f"((//div[contains(text(),'Draft Locked')]/ancestor::div[@class='item']))[{count}]//div[@class='dots']",
        #                 )
        #             )
        #             self.scroll_to(dots, 400)
        #             time.sleep(4)
        #             dots.click()
        #             self.do_click(self.Send_edits)
        #             Edits = WebDriverWait(self.driver, 20).until(
        #                 EC.visibility_of_element_located(self.Edit_comments)
        #             )
        #             Edits.send_keys("Resolved this", Keys.TAB, Keys.TAB, Keys.ENTER)
        #             banner_msg = self.get_element_text(self.Success_msg)
        #             print(banner_msg)
        #             assert  banner_msg == TestData.EDIT_MSG
        #         count += 1
        except StaleElementReferenceException:
            self.driver.refresh()
