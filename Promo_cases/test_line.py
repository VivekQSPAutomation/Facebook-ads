import allure
import pytest

from Promo_pages.line_item import Lineitem


class Test_line:
    def line_object(self, ses_init):
        self.line = Lineitem(ses_init)
        return self.line

    @allure.feature("Promo Line Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=6)
    def test_line_page(self, ses_init, request):
        line_check = self.line_object(ses_init)
        line_check.line()

