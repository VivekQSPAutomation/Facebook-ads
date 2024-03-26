import datetime
import os
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Application(Basepage):
    Create_button = (By.XPATH, "//div[@class='createNew']")
    Application_link = (
        By.XPATH,
        "//div[@class='wrapper applicationDashCreateNewPopover']/a[@href='/applications/edit/general/0']",
    )
    Connected_to_Campaign = (
        By.XPATH,
        "//p[contains(text(),'Connected To Campaign')]/..//div[@class='selectContent text text--uppercase text--bold']",
    )
    Search_to_campaign = (By.XPATH, "//div[@class='searchContainer']//input")
    Campaign_name = (
        By.XPATH,
        f"//div[@class='chooseCampaign fancyScroll']/div[contains(text(),'{os.environ.get('Campaign_name')}')]",
    )

    Choose_a_template = (
        By.XPATH,
        "//p[contains(text(),'Choose A Template')]/../div[@class='selectPopover']",
    )
    Short_form_video = (
        By.XPATH,
        "//div[@class='wrapper application-generic-dropdown']/div[contains(text(),'Short Form Video')]",
    )
    Deadline_date = (By.XPATH, "//input[@id='calendar-input-deadline']")
    Decision_date = (By.XPATH, "//input[@id='calendar-input-decisionDate']")
    Draft_due_date = (By.XPATH, "//input[@id='calendar-input-draftDueDate']")
    publish_due_date = (By.XPATH, "//input[@id='calendar-input-publishDate']")
    Turn_off = (By.XPATH, "//input[@value='false']")
    Brand = (By.XPATH, "//div[@id='editor']/div/ul/li[1]")
    Product = (By.XPATH, "//div[@id='editor']/div/ul/li[2]")
    Retail = (By.XPATH, "//div[@id='editor']/div/ul/li[3]")
    Continue = (By.XPATH, "//button[@label='Continue']")
    Select_and_continue = (
        By.XPATH,
        "//a[@class='btn btn--emptyBorder btn--full text text--uppercase text--bold']",
    )
    Saveandclose = (By.XPATH, "//button[contains(text(),'Save A')]")
    Click_yes = (
        By.XPATH,
        "//div[@class='banner banner-choice ']//span[contains(text(),'Yes')]",
    )
    Image_upload_click = (By.XPATH, "//button[@id='upload_widget_opener']")
    Image_iframe = (
        By.XPATH,
        "//iframe[@src='https://widget.cloudinary.com/n/ahalogydev/169/index.html?cloud_name=ahalogydev']",
    )
    Image_div_holder = (By.XPATH, "//div[@class='upload_button_holder']")
    Image_upload_button = (By.XPATH, "//div[@class='upload_cropped_holder']")

    search_influencers = (By.XPATH, "//input[@id='search-influencers']")
    Selected_influ = (By.XPATH, "//i[@class='fa fa-star-o star']")

    def __init__(self, ses_init):
        super().__init__(ses_init)
        self.driver.get(
            f"{TestData.env_setup(self)}/applications/edit/general/0"
        )

    def Create_application(self):
        count = 1
        while True:
            try:
                self.do_click(self.Connected_to_Campaign)
                if 'staging' in TestData.env_setup(self):
                    self.do_send_keys(self.Search_to_campaign, TestData.Campaign_name)
                else:
                    self.do_send_keys(self.Search_to_campaign, TestData.Campaign_prod_name)
                self.do_click(
                    (
                        By.XPATH,
                        f"//div[contains(text(),'Test')]",
                    )
                )
                self.do_click(self.Choose_a_template)
                Short_form = self.get_elements(self.Short_form_video)
                Short_form[0].click()
                self.do_send_keys(
                    self.Deadline_date,
                    (datetime.date.today() + datetime.timedelta(weeks=2)).strftime(
                        "%m/%d/%Y"
                    ),
                )
                self.do_send_keys(
                    self.Decision_date,
                    (datetime.date.today() + datetime.timedelta(days=3)).strftime(
                        "%m/%d/%Y"
                    ),
                )
                self.do_send_keys(
                    self.Draft_due_date,
                    (datetime.date.today() + datetime.timedelta(weeks=1)).strftime(
                        "%m/%d/%Y"
                    ),
                )
                self.do_send_keys(
                    self.publish_due_date,
                    (datetime.date.today() + datetime.timedelta(weeks=3)).strftime(
                        "%m/%d/%Y"
                    ),
                )
                self.do_click(self.Image_upload_click)
                self.driver.switch_to.frame(self.get_element(self.Image_iframe))
                self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
                    f"{os.getcwd()}/image0.jpg"
                )
                self.do_click(self.Image_upload_button)
                self.driver.switch_to.default_content()
                script = """
                       let elements = document.querySelectorAll('input[value="true"]');
                       elements.forEach(element => element.click());
                       """

                self.driver.execute_script(script)

                # First li
                li_element = self.get_element(self.Brand)
                string_to_append = " Coca-Cola"
                self.driver.execute_script(
                    "arguments[0].innerText += arguments[1];",
                    li_element,
                    string_to_append,
                )

                # Second li
                li_element = self.get_element(self.Product)
                string_to_append = " Beverages"
                self.driver.execute_script(
                    "arguments[0].innerText += arguments[1];",
                    li_element,
                    string_to_append,
                )

                # Third li

                li_element = self.get_element(self.Retail)
                string_to_append = " Ahold"
                self.driver.execute_script(
                    "arguments[0].innerText += arguments[1];",
                    li_element,
                    string_to_append,
                )
                time.sleep(4)
                self.do_click(self.Continue)
                time.sleep(5)
                self.do_click(self.Continue)
                time.sleep(3)
                if os.environ.get("Email"):
                    self.do_send_keys(self.search_influencers, os.environ.get("Email"))
                else:
                    self.do_send_keys(self.search_influencers, os.environ.get("Emai"))
                self.driver.find_element(
                    By.XPATH, "//input[@id='search-influencers']"
                ).send_keys(Keys.ENTER)
                time.sleep(1)
                self.do_click(self.Selected_influ)
                time.sleep(3)
                self.do_click(self.Select_and_continue)
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((self.Click_yes))
                ).click()
                msg_value = (
                    WebDriverWait(self.driver, 20)
                    .until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//div[@class ='banner banner-success ']")
                        )
                    )
                    .text
                )
                if msg_value == TestData.Applicaiton_msg:
                    self.do_click(self.Saveandclose)
                    time.sleep(5)
                    return True
            except TimeoutException:
                self.driver.refresh()
                if count < 3:
                    return False
                count = count + 1

