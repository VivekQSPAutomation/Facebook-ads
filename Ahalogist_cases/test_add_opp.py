import allure
import pytest

from Ahalogist_pages.Add_opp import Opp
from Config.config import TestData
from Config.test_order import Order


@pytest.fixture(params=TestData.Add_opp)
def test_data(request):
    return request.param


class Test_add_opp:
    def add_opp_object(self, ses_init):
        self.call = Opp(ses_init)
        return self.call

    @allure.feature("Add Opportunity dashboard")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Add_opps)
    def test_add(self, ses_init, request, test_data):
        call = self.add_opp_object(ses_init)
        if call.add_opp(test_data):
            assert True
        else:
            assert False
