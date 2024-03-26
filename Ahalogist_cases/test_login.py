import allure
import pytest

from Ahalogist_pages.AhalogistLogin import Welcome_session


class TestLogin:

    def welcome_object(self, ses_init):
        self.wel_login = Welcome_session(ses_init)
        return self.wel_login

    @allure.feature("Login functionality Ahalogist")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=15)
    def test_login_page(self, ses_init, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        wel_obj = self.welcome_object(ses_init)
        status = wel_obj.login_url_redirect_session()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)
        assert status
