import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Remove_Influence(Basepage):
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
    Content_type = (By.XPATH, "//div[@class='brandableType']//span")
    Socail_type = (By.XPATH, "//button[contains(text(),'Social')]")
    line_item = (By.XPATH, "//div[@class='lineItem ']//span")
    line_item_type = (
        By.XPATH,
        "//div[@class = 'wrapper ahalogistWorkspaceCardPopoverEditField']",
    )
    queue_selection = (By.XPATH, "//div[@class='workspace-tabs']//div[7]")
    queued_selection = (By.XPATH, "//div[@class='workspace-tabs']//div[1]")
    upload_brief = (By.XPATH, "//input[@id='newPostBrief']")
    draft_date = (By.XPATH, "//input[@id='calendar-input-draftDueDateNew']")
    Onboard_msg = (By.XPATH, "//div[@class='onboarded']")
    influence_all = (
        By.XPATH,
        "//div[@class='container    ']",
    )

    influ_queue = (
        By.XPATH,
        "//div[@class='masonry-grid-custom threeColumns ']//div[@class='container ']",
    )

    Remove_infl = (By.XPATH, "//button[contains(text(),'Remove Influencer')]")
    Click_yes = (
        By.XPATH,
        "//div[@class='banner banner-choice ']//span[contains(text(),'Yes')]",
    )
    Job_tracker_delete = (By.XPATH, "//a[contains(text(),'Delete')]")
    draft_locked = (By.XPATH, "//div[contains(text(),'Draft Locked')]")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/job-tracker")

    def remove_influence(self, data):

        try:
            Add = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.Search_item)
            )
            Add.send_keys(data, Keys.ENTER)
            ## start
            time.sleep(3)
            actions = ActionChains(self.driver)
            Hovering_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.Workspace_dashboard)
            )

            actions.move_to_element(Hovering_element).perform()
            self.do_click(self.Workspace_click)
            self.get_window(1)
            time.sleep(1)
            self.do_click(self.queue_selection)
            time.sleep(1)

            while True:
                ele = self.get_elements(self.influence_all)
                time.sleep(1)
                index = 0
                while index < len(ele):
                    try:
                        time.sleep(1)
                        self.do_click(self.Dots)
                        element = self.get_element(self.Remove_infl)
                        time.sleep(2)
                        element.click()
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(self.Click_yes)
                        ).click()
                        msg_value = (
                            WebDriverWait(self.driver, 10)
                            .until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "//div[@class ='banner banner-success ']",
                                    )
                                )
                            )
                            .text
                        )
                        if msg_value == TestData.remove_msg:
                            pass
                    except StaleElementReferenceException:
                        self.driver.refresh()
                        pass
                    except TimeoutException:
                        pass
                    index += 1

                # Refresh the page
                self.driver.refresh()
                # Check if anything remains
                remaining_elements = self.get_elements(self.influence_all)
                if not remaining_elements:
                    break

            self.get_window(0)
        except TimeoutException as e:
            self.get_window(0)
            if data == TestData.Campaign_name:
                self.do_click(self.Dots)
                self.do_click(self.Job_tracker_delete)
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.Click_yes)
                ).click()
                time.sleep(3)
            return True
            # else:
            #     pass
