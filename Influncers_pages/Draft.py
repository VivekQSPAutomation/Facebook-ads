import os
import re
import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Influncers_pages.facebook_ads.Staticads import Static_ads
from Influncers_pages.BasePages import Basepages


class Draft(Basepages):
    all_draft = (By.XPATH, "//div[@class='container  ']")
    Campaign = (By.XPATH, "//a[contains(text(),'Campaigns')]")
    Type = (By.XPATH, "//div[@class='workspace-tabs']/div")
    Edit_draft = (
        By.XPATH,
        "//button[contains(text(),'Edit Draft')]",
    )
    Edit_update = (By.XPATH, "//div[@id='editor']//p")
    photo_click = (
        By.XPATH,
        "//div[@class='thumbImage']",
    )
    review_send = (By.XPATH, "//span[contains(text(),'Send')]")
    video_url = (By.XPATH, "//input[@id='videoUrl']")
    Video_title = (By.XPATH, "//input[@id='title']")
    h3_data = (By.XPATH, "//h3[text()]")
    image_url = (By.XPATH, "//div[@id='editor']//p//img")
    campaign =(By.XPATH,"//div[@class='brandableIconAndTitle']//div[2]//div")
    type =(By.XPATH,"//div[@class='brandableIconAndTitle']//div[2]//h1")
    video_click = (By.XPATH,"(//div[@class='sideBarOptions ']//div)[3]")
    image_click = (By.XPATH,"(//div[@class='sideBarOptions ']//div)[2]")
    Copy_button= (By.XPATH,"//div[@title='Copy video link']")
    Copy_url =( By.XPATH,"//div[contains(text(),' Copy Video Link')]")
    Copied_url =( By.XPATH,"//div[@class='wrapper application-generic-dropdown']//div")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{TestData.env_setup(self)}/workspace")
        self.driver.execute_script("document.body.style.zoom='0.8'")

    def edit_draft(self, data):
        time.sleep(6)
        if "general" in self.driver.current_url:
            self.driver.get(f"{TestData.env_setup(self)}/workspace")
            self.driver.execute_script("document.body.style.zoom='0.8'")
        else:
            pass
        sign_type = self.get_elements(self.Type)
        self.click_element_with_js(sign_type[1])
        time.sleep(3)
        retry_count = 1
        wait = WebDriverWait(self.driver, 10)
        status = False
        count = 1
        while True:
            sign_type = self.get_elements(self.Type)
            self.click_element_with_js(sign_type[1])
            try:
                lines = wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"(//div[@class='container  '])[{count}]")
                    )
                ).text.split("\n")
                for line in lines:
                    if data in line:
                        print(line, data)
                        if "SOCIAL POST" == data:
                            element = wait.until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        f"(//div[@class='container  '])[{count}]//button[contains(text(),'Edit Draft')]",
                                    )
                                )
                            )
                            self.scroll_to(element)
                            self.click_element_with_js(element)
                            self.driver.execute_script("document.body.style.zoom='1'")
                            campaign_name = self.get_element_text(self.campaign)
                            folder_path = os.getcwd()
                            files_in_folder = os.listdir("./images/")
                            file_path = [
                                os.path.join(folder_path, "images", file_name)
                                for file_name in files_in_folder
                            ]
                            file_input = self.driver.find_element(
                                By.XPATH, "//input[@type='file']"
                            )
                            file_input.send_keys("\n".join(file_path))

                            self.do_send_keys(
                                self.Edit_update, "Testing QA using Automation #ad"
                            )
                            self.do_send_keys(self.Edit_update, Keys.ENTER)
                            time.sleep(2)
                            time.sleep(4)
                            self.do_click(self.video_click)
                            time.sleep(4)
                            self.do_click(self.Copy_button)
                            self.do_click(self.Copy_url)
                            text = self.get_element_text(self.Copied_url)
                            self.do_send_keys(self.Edit_update, Keys.ENTER)
                            self.do_send_keys(self.Edit_update, text)
                            self.do_send_keys(self.Edit_update, Keys.ENTER)
                            time.sleep(8)
                            self.driver.execute_script("arguments[0].click();", self.get_element(self.image_click))
                            # self.do_click(self.image_click)
                            self.do_click(self.photo_click)
                            image = self.get_element(self.image_url)
                            image_url = image.get_attribute('src')
                            static = Static_ads()
                            ad_set = static.create_campaignandadset(brandname=campaign_name)
                            preview = static.create_Ads(ad_set, brandname=campaign_name,image_url=image_url)
                            src_match = re.search(r'src="(.*?)"', preview)
                            if src_match:
                                os.environ['preview'] = src_match.group(1)

                            else:
                                print("No 'src' attribute found in the iframe.")
                            self.do_click(self.review_send)
                            time.sleep(8)
                            print(os.environ.get('preview'))
                            status = True
                            break

            except StaleElementReferenceException:
                continue

            except TimeoutException:
                print(retry_count)
                if retry_count > 4:
                    assert False
                else:
                    self.driver.get(f"{TestData.env_setup(self)}/workspace")
                    self.driver.execute_script("document.body.style.zoom='0.8'")
                retry_count += 1
            if status:
                break
            count += 1
