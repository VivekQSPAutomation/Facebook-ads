from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from Fragments.Practice_fragments import Pratice
from Fragments.Search_fragments import Search_fragments
from Fragments.login_fragments import Login_Fragments
from itertools import zip_longest


def generate_class_and_function(class_name, function_name, parameters, function_content, value, url, locators):
    # Generate the class attributes
    class_attributes = {}

    # Define the __init__ method
    def __init__(self, *args):
        for param, val in zip(parameters, args):
            setattr(self, param, value)

    class_attributes["__init__"] = __init__

    #// login functionality
    def generated_function(self, session):
        session.get(url)
        print(list(zip_longest(function_content, value, locators)))
        for content, val, locator in zip_longest(function_content, value, locators):
            if content == "send":
                WebDriverWait(session, 10).until(Ec.visibility_of_element_located(locator)).send_keys(f'{val}')
            elif content == "send_enter":
                WebDriverWait(session, 10).until(Ec.visibility_of_element_located(locator)).send_keys(Keys.ENTER)
            else:
                WebDriverWait(session, 10).until(Ec.visibility_of_element_located(locator)).click()

    class_attributes[function_name] = generated_function

    #//search functionality
    if "search_content" in function_name:
        def generated_search_function(self, session):
            session.get(url)
            element = WebDriverWait(session, 10).until(Ec.visibility_of_element_located(Search_fragments.Search))
            element.send_keys(value)
            element.send_keys(Keys.ENTER)

        class_attributes["search_content"] = generated_search_function
    #//header functionality
    if "header_check" in function_name:
        def generated_header_function(self, session):
            session.get(url)
            element = WebDriverWait(session, 10).until(Ec.visibility_of_element_located(Pratice.header))
            print(element.text)

        class_attributes["header_check"] = generated_header_function

    generated_class = type(class_name, (object,), class_attributes)
    return generated_class
