import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Login import Welcome_session


class Test_login:
    def welcome_object(self, ses_init):
        self.wel_login = Welcome_session(ses_init)
        return self.wel_login

    @allure.feature("Login Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.influ_login)
    def test_login_page(self, ses_init, request):
        wel_obj = self.welcome_object(ses_init)
        status = wel_obj.login_url_redirect_session()
        assert status
