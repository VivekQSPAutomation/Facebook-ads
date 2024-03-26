import os

import pandas as pd
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Influncers_pages.BasePages import Basepages


class Random_Email(Basepages):
    Email = (By.ID, "i-email")
    Email_verify = (By.XPATH, "//ul[@class='mail-items-list']")
    verification_button = (By.XPATH, "//a[contains(text(),'Click here')]")
    Email_click = (By.XPATH, "//span[contains(text(),'Refresh')]")
    Iframe_locator = (By.XPATH, "//iframe[@id='fullmessage']")
    Tempmail = (By.XPATH, "//input[@id='mail']")
    tempmail_refresh = (By.XPATH, "//a[@id='click-to-refresh']")
    Mail_click = (By.XPATH, "//span[@class ='inboxSubject subject-title']//a")
    temp_mail = (
        By.XPATH,
        "//span[@id='email']",
    )
    div_click = (
        By.XPATH,
        "//td[contains(text(),'social')]",
    )
    frame = (By.XPATH, "//iframe[@id='iframeMail']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://tempmailo.com/")
        # self.driver.get("https://www.disposablemail.com/")

    def random_email(self):
        try:
            os.environ["Email"] = self.get_element_value(self.Email)
            df = pd.read_csv(f'{os.getcwd()}/influencers.csv')
            Influ = df['Influencer'].iloc[0]
            if Influ == os.environ.get('Email'):
                pass
            else:
                df['Influencer'].iloc[0] = os.environ.get('Email')
                df.to_csv(f'{os.getcwd()}/influencers.csv', index=False)

            # os.environ["Email"] = self.get_element_text(self.temp_mail)
            if not os.environ.get("Email"):
                self.driver.get("https://www.disposablemail.com/")
                os.environ["Emai"] = self.get_element_text(self.temp_mail)
                df['Influencer'].iloc[0] = os.environ.get('Emai')
                df.to_csv(f'{os.getcwd()}/influencers.csv', index=False)
                print(os.environ.get("Emai"))
                return True
            else:
                return True
        except TimeoutException:
            self.driver.get("https://www.disposablemail.com/")
            os.environ["Emai"] = self.get_element_text(self.temp_mail)
            return True

    def validation_email(self):
        while True:
            try:
                if os.environ.get("Email"):
                    self.do_click(self.Email_click)
                    parent = self.driver.find_element(
                        By.XPATH, "//ul[@class='mail-items-list']"
                    )
                    parent_child = parent.find_elements(
                        By.XPATH, "//li/div[contains(text(),'social')]"
                    )
                    for child in parent_child:
                        child.click()
                        iframe_value = self.driver.find_element(
                            By.XPATH, "//iframe[@id='fullmessage']"
                        )
                        self.driver.switch_to.frame(iframe_value)
                        element = self.driver.find_element(
                            By.XPATH, "//a[contains(text(),'Click here')]"
                        )
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView();", element
                        )
                        self.do_click((By.XPATH, "//a[contains(text(),'Click here')]"))
                        self.get_window(1)
                        return True

                else:
                    self.driver.get("https://www.disposablemail.com/")
                    self.do_click(self.div_click)
                    iframe_element = self.get_element(self.frame)
                    self.driver.switch_to.frame(iframe_element)
                    element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//a[contains(text(),'Click here')]")
                        )
                    )
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView();", element
                    )
                    self.driver.execute_script("arguments[0].click();", element)
                    self.get_window(1)
                    return True

            except NoSuchElementException:
                self.driver.refresh()

            except TimeoutException:
                return False

            break
