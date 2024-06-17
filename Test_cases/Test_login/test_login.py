import pytest

from Fragments.login_fragments import Login_Fragments
from Pages.Search.Search import generate_class_and_function


@pytest.mark.usefixtures('session')
class Test_Login:

    def test_login_content(self, session):
        class_name = "Login"
        function_name = "Validate"
        parameters = []
        function_content = ["send", "send", "click"]
        value = ["student","Password123"]
        url = "https://practicetestautomation.com/practice-test-login/"
        generated_code = generate_class_and_function(class_name, function_name, parameters, function_content, value,
                                                     url, Login_Fragments.locators)
        search = generated_code()
        search.Validate(session)

    def test_search_content(self, session):
        class_name = "Search"
        function_name = "search_content"
        parameters = []
        function_content = ["send"]
        value = "Vivek"
        url = "https://google.com"
        generated_code = generate_class_and_function(class_name, function_name, parameters, function_content, value,
                                                     url, Login_Fragments.locators)
        search = generated_code()
        search.search_content(session)

    def test_header_content(self, session):
        class_name = "Header"
        function_name = "header_check"
        parameters = []
        function_content = []
        value = "Vivek"
        url = "https://practicetestautomation.com/practice/"
        generated_code = generate_class_and_function(class_name, function_name, parameters, function_content, value,
                                                     url, Login_Fragments.locators)
        search = generated_code()
        search.header_check(session)

