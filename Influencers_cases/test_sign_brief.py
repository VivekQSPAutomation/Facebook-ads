import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Sign_brief import SignBrief


@pytest.fixture(params=["SOCIAL POST"])
def test_data(request):
    return request.param


class Test_Sign_brief:
    @allure.feature("Sign Brief Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Sign_brief)
    def test_sign_brief(self, ses_init, test_data, request):
        obj = SignBrief(ses_init)
        status = obj.sign_brief(test_data)
        if status is None:
            assert True
        else:
            assert False
