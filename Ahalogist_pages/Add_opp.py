import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class Opp(Basepage):
    new_opp = (By.XPATH, "//li[contains(text(),'+ Add SF Opportunity')]")
    SF_Opportunity_Button = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn enter']",
    )
    Selecting_category = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn']",
    )
    Connect_button = (
        By.XPATH,
        "//button[@class='text text--bold text--uppercase campaignBtn whiteBtn connect ']",
    )
    Savenclose = (By.XPATH, "//button[contains(text(),'Save And Close')]")
    cancel = (By.XPATH, "//button[contains(text(),'Cancel')]")
    campaign_price = (
        By.XPATH,
        "//div[@class='sf-opportunities-details']//p[contains(text(),'Campaign Price')]/..//p[@class='text text--uppercase']",
    )

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def add_opp(self, data):

        self.do_click(self.new_opp)
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
            # self.do_click(self.Savenclose)

            self.do_click(self.cancel)
            time.sleep(3)
            return True
        else:
            return False

    def scroll_to_end(self):
        document_height = self.driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight );"
        )

        self.driver.execute_script(f"window.scrollTo(0, {document_height});")
