import allure
import pytest

from Ahalogist_pages.Job_tracker import Job_tracker
from Config.config import TestData
from Config.test_order import Order


@pytest.fixture(params=[TestData.Campaign_name])
def test_data(request):
    return request.param


class Test_Jobtracker:
    def jobtracker_object(self, ses_init):
        self.job_track = Job_tracker(ses_init)
        return self.job_track

    @allure.feature("Campaign  Creation Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Job_tracker)
    def test_job_tracker_page(self, ses_init, test_data, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        job_track = self.jobtracker_object(ses_init)
        status = job_track.create_campaign(test_data)
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)
        assert status
