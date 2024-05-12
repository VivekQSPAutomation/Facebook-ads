import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Correction_draft import CorrectionDraft


class Test_CorrectionDraft:
    @allure.feature("Draft Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Influ_correction_draft)
    def test_Correction_draft(self, ses_init, request):

        obj = CorrectionDraft(ses_init)
        status = obj.selected_text_draft()
        if status:
            assert True
        else:
            assert False
