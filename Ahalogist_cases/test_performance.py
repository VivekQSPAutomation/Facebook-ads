import allure
import pytest

from Ahalogist_pages.Performance import Performance
from Config.test_order import Order


class Test_performance:
    def performance_object(self, ses_init):
        self.performance = Performance(ses_init)
        return self.performance

    @allure.feature("Onboarding Influence")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Performance_dash)
    def test_performance_influence(self, ses_init, request):
        performance = self.performance_object(ses_init)
        performance.peformance_dashboard()
