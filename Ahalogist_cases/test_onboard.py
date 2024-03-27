import allure
import pytest

from Ahalogist_pages.Onbaording_influencers import onboardInfluencers
from Config.test_order import Order


#
@pytest.fixture(params=["Social"])
def test_data(request):
    return request.param


class Test_onboard:
    def onboard_object(self, ses_init):
        self.onboard = onboardInfluencers(ses_init)
        return self.onboard

    @allure.feature("Onboarding Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=Order.Influ_onboard)
    def test_onboard_influncers(self, ses_init, test_data, request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = aha_recording_and_capturing_screen(ses_init, request.node.name)
        onboard = self.onboard_object(ses_init)
        status = onboard.Onboard_influencers(test_data)
        # aha_stop_screen_record(screen)
        # aha_video_creation_from_screenshots(request.node.name)

        if status is None:
            assert True
        else:
            assert False


