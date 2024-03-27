import allure
import pytest

from Ahalogist_pages.campaign_price import Campprice
from Config.config import TestData
from Config.test_order import Order


@pytest.fixture(params=TestData.camp_price)
def test_data(request):
    return request.param
class Test_Camprice:
    def price(self, ses_init):
        self.pric = Campprice(ses_init)
        return self.pric

    @allure.feature("Campaign Price")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Campaign_price)
    def test_price(self, ses_init, test_data,request):
        camp = self.price(ses_init)
        status = camp.price(test_data)
        if status:
            assert True
        else:
            assert False

