from selenium import webdriver
import pytest


@pytest.fixture()
def session():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
