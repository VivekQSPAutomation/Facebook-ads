import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Capabilities import Capabilities_pages


class Test_Capabilities:
    @allure.feature("Capabalites Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.capabilities)
    def test_capabilities_details(self, ses_init):

        obj = Capabilities_pages(ses_init)
        status = obj.get_capablities_details()
        assert status
