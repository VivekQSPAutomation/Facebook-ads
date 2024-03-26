import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Config.config import TestData
from Influncers_pages.BasePages import Basepages


class NegativeCases(Basepages):
    Save_button = (By.XPATH, "//button[@type='submit']")
    image_button = (By.XPATH, "//button[@id='upload_widget_opener']")
    Next_button = (By.XPATH, "//a[contains(text(),'Next')]")
    testing_values = ["-1", "1/1000", "<img src='javascript:alert('yo')' />"]
    banner_locator = (
        By.XPATH,
        "//div[@class='alert-dialog js-login-alert alert-dialog--success showAlertDialog']",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(
            f"{TestData.env_setup(self)}/partners/settings/general"
        )

    def form_data(self):
        form_data = self.driver.find_element(By.TAG_NAME, "form")
        child_input = form_data.find_elements(By.TAG_NAME, "input")
        return child_input

    def form(self):
        form_data = self.driver.find_element(By.TAG_NAME, "form")
        return form_data

    def general_negative_cases(self, Data):
        time.sleep(3)
        childs = self.form_data()
        time.sleep(3)
        # country_select = Select(self.form().find_element(By.TAG_NAME, "select"))
        # country_select.select_by_value("USA")
        # if country_select.first_selected_option:
        #     child_select = self.form().find_elements(By.TAG_NAME, "select")[1]
        #     Select(child_select).select_by_value("Alabama")
        #     after_child_select = self.form_data()[6]
        #
        #     self.driver.find_element(
        #         By.ID, after_child_select.get_attribute("id")
        #     ).send_keys("1234")
        for child in childs:
            if child.get_attribute("type") == "tel":
                self.get_clear((By.ID, child.get_attribute("id")))
                self.driver.find_element(By.ID, child.get_attribute("id")).send_keys(
                    "1234"
                )
            elif (
                child.get_attribute("value") == "true"
                or child.get_attribute("value") == "false"
            ):
                pass
            elif "zip" in child.get_attribute("id"):
                pass
            else:
                self.get_clear((By.ID, child.get_attribute("id")))
                self.do_send_keys((By.ID, child.get_attribute("id")), Data)
        self.driver.find_element(By.XPATH, "//button[@default='Save']").send_keys(
            Keys.RETURN
        )

        if self.is_displayed(self.banner_locator):
            assert True
        else:
            assert False
