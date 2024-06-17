from selenium.webdriver.common.by import By


class Login_Fragments:
    locators = [(By.XPATH, "//input[@id='username']"), (By.XPATH, "//input[@id='password']"),
                (By.XPATH, "//button[@id ='submit']")]
