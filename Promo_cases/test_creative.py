import allure
import pytest

from Promo_pages.Promo_creative import Promocreative


class Test_Creative:
    def creative_object(self, ses_init):
        self.creative= Promocreative(ses_init)
        return self.creative

    @allure.feature("Creative Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=4)
    def test_creative_page(self, ses_init, request):
        enable = self.creative_object(ses_init)
        status = enable.creative()
        assert status
