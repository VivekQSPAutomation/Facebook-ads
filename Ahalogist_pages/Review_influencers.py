import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Ahalogist_pages.Basepage import Basepage


class ReviewInflu(Basepage):
    search_influence = (By.XPATH, "//input[@id='searchInput']")
    Dots = (By.XPATH, "//div[@class='container    ']//div[@class='dots']")
    finished_tab = (By.XPATH, "(//div[@class='workspace-tabs']//div)[6]")
    review_button = (
        By.XPATH,
        "//div[@class='container    ']//button[contains(text(),'Review')]",
    )
    rating = (By.XPATH, "//div[@class='rating']//div[@class='star-rating-widget']")
    Submit = (
        By.XPATH,
        "//div[@class='buttonContainer']//button[contains(text(),'Submit')]",
    )

    def __init__(self, ses_init):
        super().__init__(ses_init)

    def review_influencer(self):
        self.driver.refresh()
        if len(self.get_window_count()) < 4:
            self.get_window(2)
        else:
            self.get_window(3)
        self.do_click(self.finished_tab)
        time.sleep(5)
        self.scroll_to(self.get_element(self.review_button), 200)
        self.do_click(self.review_button)
        rate = self.get_elements(self.rating)
        count = 1
        for rate_element in rate:
            base_xpath = f"(//div[@class='rating']//div[@class='star-rating-widget'])"
            element = self.get_element((By.XPATH, f"({base_xpath}//div[3])[{count}]"))
            ActionChains(self.driver).move_to_element(element).click().perform()
            count += 1
        self.do_click(self.Submit)
        time.sleep(8)
        assert True
