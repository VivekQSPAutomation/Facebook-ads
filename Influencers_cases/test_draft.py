import allure
import pytest

from Influncers_pages.Draft import Draft


@pytest.fixture(params=["SOCIAL POST"])
def test_data(request):
    return request.param


class Test_Draft:
    @allure.feature("Draft Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=24)
    def test_draft(self, ses_init, test_data,request):

        obj = Draft(ses_init)
        status = obj.edit_draft(test_data)
        if status is None:
            assert True
        else:
            assert False

