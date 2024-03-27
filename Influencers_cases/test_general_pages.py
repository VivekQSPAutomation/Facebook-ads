import allure
import pytest

from Config.test_order import Order
from Influncers_pages.General_page import Homepages


class Test_Home:
    @allure.feature("General Pages Influences")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.general_pages)
    def test_influences_profile_setting(self, ses_init,request):

        obj = Homepages(ses_init)
        status  = obj.influence_profile_setting()
        assert status



