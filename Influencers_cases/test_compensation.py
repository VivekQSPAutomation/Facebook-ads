import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Compensation import Compensation_pages


class Test_Compensation:
    @allure.feature("Compensation Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.compensation)
    def test_compensation_details(self, ses_init,request):

        obj = Compensation_pages(ses_init)
        status =obj.get_compensation_details()
        assert status

