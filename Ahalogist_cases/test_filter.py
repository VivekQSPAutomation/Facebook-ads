import allure
import pytest

from Ahalogist_pages.Filtered_dash import Filter
from Config.test_order import Order


class Test_filter:
    def filter_object(self, ses_init):
        self.call = Filter(ses_init)
        return self.call

    @allure.feature("Filter dashboard")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Filter_dashboard)
    def test_filter(self, ses_init, request):
        call = self.filter_object(ses_init)
        call.filterdash()
