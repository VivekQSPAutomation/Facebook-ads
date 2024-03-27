import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Ahalogist_pages.Basepage import Basepage
from Config.config import TestData


class DeleteApplication(Basepage):
    Application_selection = (By.XPATH, '//h3[contains(text(),"Short Form Video")]')
    Dots = (By.XPATH, "//div[@class='dots']")
    Delete_app = (By.XPATH, "//button[contains(text(),'Delete')]")
    Click_yes = (
        By.XPATH,
        "//div[@class='bannerMessage confirm']//span[contains(text(),'Yes')]",
    )

    def __init__(self, ses_init):
        super().__init__(ses_init)
        ses_init.get(
            f"{TestData.env_setup(self)}/applications/dashboard?message=&messageType="
        )

    def delete_application(self):
        for _ in self.get_elements(self.Application_selection):
            if "ABSCO" in _.text:
                pass
            else:
                self.do_click(self.Dots)
                self.do_click(self.Delete_app)
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.Click_yes)
                ).click()
                time.sleep(10)
