from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""This class is the parent of the all pages"""


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def do_get_locator(self, by_locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        )

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        ).click()

    def do_element_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(by_locator)
        ).click()

    def do_send_keys(self, by_locator, text, tab="", enter=""):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text, tab, tab, enter)

    def do_send_keys_tab(self, by_locator, text, tab="", enter=""):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text, tab, enter)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def pages_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def is_link_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(by_locator)
        )
        return bool(element)

    def get_element_value(self, by_locator):
        element = (
            WebDriverWait(self.driver, 30)
            .until(EC.visibility_of_element_located(by_locator))
            .get_attribute("value")
        )
        return element

    def get_window(self, window_value):
        self.driver.switch_to.window(self.driver.window_handles[window_value])

    def get_clear(self, by_locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        ).clear()

    def get_elements(self, by_locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(by_locator)
        )

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element

    def get_window_count(self):
        return self.driver.window_handles

    def scroll_to_line(self, element):
        element_height = element.size["height"]
        scroll_speed = 10
        current_scroll_height = 0

        while current_scroll_height < element_height - 200:
            current_scroll_height += scroll_speed
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
            self.driver.implicitly_wait(0.1)

    def scroll_to(self, element, pos):
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        self.driver.execute_script(f"window.scrollBy(0, +{pos});")

    def scroll_to_add(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # self.driver.execute_script(f"window.scrollBy(0, +{pos});")