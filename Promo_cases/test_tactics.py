import allure
import pytest

from Promo_pages.tactics import Tactics


class Test_Tactics:
    def tactics_object(self, ses_init):
        self.tactics= Tactics(ses_init)
        return self.tactics

    @allure.feature("Tactics Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=7)
    def test_creative_page(self, ses_init, request):
        tacticsname = self.tactics_object(ses_init)
        tacticsname.tactics()

