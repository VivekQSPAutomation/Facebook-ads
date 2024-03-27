import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Personal_details import Personal_pages


class Test_Personal:
    @allure.feature("Personal Details Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.personal_details)
    def test_personal_details(self, ses_init, request):

        obj = Personal_pages(ses_init)
        status = obj.get_personal_details()
        assert status
