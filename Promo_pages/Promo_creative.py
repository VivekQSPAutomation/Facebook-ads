import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from Config.config import TestData
from Promo_pages.BasePages import Basepages

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Promocreative(Basepages):
    Creative = (By.XPATH,"//a[@title='Creatives']")
    Add_creative = (By.XPATH,"(//section[@class='creatives-container ng-star-inserted']//qbc-panel/div//div)[3]//button[@class='dropdown-btn']")
    Mobile_creative = (By.XPATH,"(//section[@class='dropdown-container ng-star-inserted']//button)[1]")
    Creative_add = (By.XPATH,"(//div[@class='creative-editor-inner']//button)[4]")
    insert_creative =(By.XPATH,"//div[@class='CodeMirror cm-s-default CodeMirror-wrap']")
    Creative_name = (By.XPATH,"(//div[@class='form-field__content']//qbc-textual-field-frame//input)[1]")
    Size_click =(By.XPATH,"//qbc-form-field[@label='Size']//qbc-select")
    Size_select = (By.XPATH,"//qbc-list-box//span[contains(text(),' 320 x 50 ')]")
    Save=(By.XPATH,"(//qbc-button-frame//div[contains(text(),'Save')])[2]")
    form_enter = (By.XPATH,"//div[@class='CodeMirror-code']//span[@role='presentation']")
    insert_value_creative = (By.XPATH,"//span[@role='presentation']")

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def creative(self):
            self.do_click(self.Creative)
            self.do_click(self.Add_creative)
            self.do_click(self.Mobile_creative)
            self.do_click(self.Creative_add)
            self.do_click(self.insert_creative)
            focused_element = self.driver.switch_to.active_element
            focused_element.send_keys(Keys.TAB)
            focused_element.send_keys(TestData.Creative_string)
            self.do_send_keys(self.Creative_name,TestData.Creative_name)
            self.do_click(self.Size_click)
            self.do_click(self.Size_select)
            self.do_click(self.Save)
            time.sleep(20)
            return True
        # except TimeoutException:
        #     return False
