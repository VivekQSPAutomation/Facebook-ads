import allure
import pytest

from Ahalogist_pages.AhalogistLogin import Welcome_session
from Ahalogist_pages.Mark_complete import MarkComplete


class Test_Mark_Complete:
    def MarkComplete(self, temp_ses_init):
        self.correct = MarkComplete(temp_ses_init)
        return self.correct

    def welcome_object(self, temp_ses_init):
        self.wel_login = Welcome_session(temp_ses_init)
        return self.wel_login

    @allure.feature("Mark Complete")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=28)
    def test_mark_complete(self, ses_init, request):
        # wel_obj = self.welcome_object(ses_init)
        # wel_obj.login_url_redirect_session()
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        mark = self.MarkComplete(ses_init)
        status = mark.mark_complete()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)
        assert status

