import allure
import pytest

from Ahalogist_pages.Applications import Application
from Ahalogist_pages.Delete_application import DeleteApplication


class Test_Application:
    def application_object(self, ses_init):
        self.job_track = Application(ses_init)
        return self.job_track

    def delete_application_object(self, ses_init):
        self.delete = DeleteApplication(ses_init)
        return self.delete

    @allure.feature("Application Creation Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=18)
    def test_delete_application_page(self, ses_init, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        app_create = self.delete_application_object(ses_init)
        app_create.delete_application()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)

    @allure.feature("Application Creation Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=19)
    def test_application_page(self, ses_init, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        app_create = self.application_object(ses_init)
        status = app_create.Create_application()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)

