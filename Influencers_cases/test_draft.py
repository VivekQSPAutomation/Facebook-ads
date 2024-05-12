import allure
import pytest

from Config.config import TestData
from Config.test_order import Order
from Influncers_pages.Draft import Draft


@pytest.fixture(params=TestData.draft_type)
def test_data(request):
    return request.param


class Test_Draft:
    @allure.feature("Draft Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Draft)
    def test_draft(self, ses_init, test_data, request):

        obj = Draft(ses_init)
        status = obj.edit_draft(test_data)
        if status is None:
            assert True
        else:
            assert False
