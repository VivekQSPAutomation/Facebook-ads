import os
import time
from datetime import date

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Job_tracker(Basepage):
    Create_create_button = (
        By.XPATH,
        "//div[@class='text text--uppercase text--bold btn btn--emptyBorder createCampaignButton']",
    )
    Campaign_name = (By.XPATH, "//input[@id='campaignName']")
    Image_upload_click = (By.XPATH, "//button[@id='upload_widget_opener']")
    Image_iframe = (
        By.XPATH,
        "//iframe[@src='https://widget.cloudinary.com/n/ahalogydev/169/index.html?cloud_name=ahalogydev']",
    )
    Image_div_holder = (By.XPATH, "//div[@class='upload_button_holder']")
    Image_upload_button = (By.XPATH, "//div[@class='upload_cropped_holder']")
    SF_Opportunity_id = (By.XPATH, "//input[@id='opportunityId']")
    SF_Opportunity_Button = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn enter']",
    )
    Selecting_category = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn']",
    )
    FoodnDrink = (By.XPATH, "//input[@id='foodAndDrink']")
    Connect_button = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn connect ']",
    )
    Savenclose = (By.XPATH, "//button[contains(text(),'Save And Close')]")
    SF_ID = "Q263199"

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(f"{TestData.env_setup(self)}/campaigns/editor?state=campaign")

    def create_campaign(self, data):
        time.sleep(5)
        # if data == "Q263199":
        self.do_send_keys(self.Campaign_name, "Test" + "_" + str(date.today()))
        os.environ["Campaign_name"] = "Test" + "_" + str(date.today())
        self.do_click(self.Image_upload_click)
        self.driver.switch_to.frame(self.get_element(self.Image_iframe))
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            f"{os.getcwd()}/image0.jpg"
        )
        self.do_click(self.Image_upload_button)
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='opportunityId']").send_keys(
            data
        )

        self.scroll_to_end()
        actions = ActionChains(self.driver)
        actions.click(self.get_element(self.SF_Opportunity_Button)).perform()
        self.do_click(self.Selecting_category)
        script = """
                   let elements = document.querySelectorAll('input[id="foodAndDrink"]');
                    let firstElement = elements[0];
                    
                    if (firstElement) {
                    firstElement.click();
                    firstElement.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab' }));
                    firstElement.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
                    }
                   """
        self.driver.execute_script(script)
        time.sleep(5)
        self.do_send_keys_tab(self.Selecting_category, "", Keys.TAB, Keys.ENTER)
        msg_value = (
            WebDriverWait(self.driver, 20)
            .until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class ='banner banner-success ']")
                )
            )
            .text
        )
        if msg_value == TestData.Campaign_msg:
            self.do_click(self.Savenclose)
            return True

        # else:
        #     self.do_send_keys(self.Campaign_name, "Test" + "Camp" )
        #
        #     self.do_click(self.Image_upload_click)
        #     self.driver.switch_to.frame(self.get_element(self.Image_iframe))
        #     self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
        #         f"{os.getcwd()}/image0.jpg"
        #     )
        #     self.do_click(self.Image_upload_button)
        #     self.driver.switch_to.default_content()
        #     time.sleep(5)
        #     self.driver.find_element(By.XPATH, "//input[@id='opportunityId']").send_keys(
        #         data
        #     )
        #
        #     self.scroll_to_end()
        #     actions = ActionChains(self.driver)
        #     actions.click(self.get_element(self.SF_Opportunity_Button)).perform()
        #     self.do_click(self.Selecting_category)
        #     script = """
        #                            let elements = document.querySelectorAll('input[id="foodAndDrink"]');
        #                             let firstElement = elements[0];
        #
        #                             if (firstElement) {
        #                             firstElement.click();
        #                             firstElement.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab' }));
        #                             firstElement.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
        #                             }
        #                            """
        #
        #     self.driver.execute_script(script)
        #     time.sleep(5)
        #     self.do_send_keys_tab(self.Selecting_category, "", Keys.TAB, Keys.ENTER)
        #     msg_value = (
        #         WebDriverWait(self.driver, 20)
        #         .until(
        #             EC.visibility_of_element_located(
        #                 (By.XPATH, "//div[@class ='banner banner-success ']")
        #             )
        #         )
        #         .text
        #     )
        #     if msg_value == TestData.Campaign_msg:
        #         self.do_click(self.Savenclose)
        #         return True

    def scroll_to_end(self):
        document_height = self.driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight );"
        )

        self.driver.execute_script(f"window.scrollTo(0, {document_height});")
