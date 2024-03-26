import allure
import pytest

from Ahalogist_pages.Dyanmiccallout import Dycall


class Test_Dynamic:
    def dynamic_object(self, ses_init):
        self.call = Dycall(ses_init)
        return self.call

    @allure.feature("Dynamic Callout")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.skip
    @pytest.mark.run(order=36)
    def test_dynamic(self, ses_init, request):
        call = self.dynamic_object(ses_init)
        call.dynamic_callout()
