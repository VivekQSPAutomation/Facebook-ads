import os

import allure
import pytest

from Ahalogist_pages.AhalogistLogin import Welcome_session
from Ahalogist_pages.Corrected_Draft import Corrected_draft
from Config.test_order import Order


class Test_CorrectionDraft:
    def Correction_draft(self, ses_init):
        self.correct = Corrected_draft(ses_init)
        return self.correct

    def welcome_object(self, ses_init):
        self.wel_login = Welcome_session(ses_init)
        return self.wel_login

    @allure.feature("Correction Draft")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Correction_draft)
    def test_Correction_details(self, ses_init, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        correct = self.Correction_draft(ses_init)
        status = correct.draft_correction()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)
        if status is None:
            assert True
        else:
            assert False

