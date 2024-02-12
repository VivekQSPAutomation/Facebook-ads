import allure
import pytest

from Promo_pages.Login import Login


class Test_login:
    def Login_object(self, ses_init):
        self.wel_login = Login(ses_init)
        return self.wel_login

    @allure.feature("Promo Login Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=1)
    def test_login_page(self, ses_init, request):
        log_obj = self.Login_object(ses_init)
        status = log_obj.login()
        assert status
