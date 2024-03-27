import os

import allure
import pytest

from Ahalogist_pages.Remove_influencers import Remove_Influence
from Config.config import TestData
from Config.test_order import Order


@pytest.fixture(params=[TestData.Campaign_name])
def test_data(request):
    return request.param


@pytest.fixture(params=[TestData.Campaign_prod_name])
def test_prod_data(request):
    return request.param


class Test_remove:
    def remove_object(self, ses_init):
        self.remove = Remove_Influence(ses_init)
        return self.remove

    @allure.feature("Onboarding Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.remove_influ)
    def test_remove_influence(self, ses_init, test_data, test_prod_data, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        remove = self.remove_object(ses_init)
        if os.environ.get("Env") == "Prod":
            status = remove.remove_influence(test_prod_data)
        else:
            status = remove.remove_influence(test_data)

        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)
        if status is None:
            assert True
        elif status:
            assert True
        else:
            assert False
