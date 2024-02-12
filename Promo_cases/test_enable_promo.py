import allure
import pytest

from Promo_pages.enable_promo import Enable


class Test_Enable:
    def enable_object(self, ses_init):
        self. enable= Enable(ses_init)
        return self.enable

    @allure.feature("Enable Promo AMP Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=3)
    def test_enable_promo_page(self, ses_init, request):
        enable = self.enable_object(ses_init)
        status = enable.Enablepromo()
        assert status
