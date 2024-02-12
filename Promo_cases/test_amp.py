import allure
import pytest

from Promo_pages.enable_promo import Enable

from Promo_pages.Promo_AMP_creation import PromoAMP


class Test_Amp:
    def amp(self, ses_init):
        self.promo= PromoAMP(ses_init)
        return self.promo

    @allure.feature("Amp Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=5)
    def test_amp(self, ses_init, request):
        amp = self.amp(ses_init)
        amp.promoamp()