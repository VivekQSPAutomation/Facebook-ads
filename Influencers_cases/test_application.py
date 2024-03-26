import allure
import pytest

from Influncers_pages.Influencers_application import Influence_Application


class Test_Application:
    @allure.feature("Application Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=22)
    def test_application(self, ses_init, request):
        obj = Influence_Application(ses_init)
        status = obj.apply_application()
        assert status
