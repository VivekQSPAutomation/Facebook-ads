import os

import allure
import pytest

from Ahalogist_pages.Add_to_queue import AddtoQueue
from Influncers_pages.DirectoryRefresh import remove_files_in_directory


class Test_onboard:
    def add_queue_object(self, ses_init):
        self.add_queue = AddtoQueue(ses_init)
        return self.add_queue

    @allure.feature("Onboarding Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=21)
    def test_add_queue_influence(self, ses_init,request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        add_queue = self.add_queue_object(ses_init)
        add_queue.add_to_queue_influence()
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)





