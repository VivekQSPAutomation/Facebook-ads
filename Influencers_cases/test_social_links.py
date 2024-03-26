import allure
import pytest

from Influncers_pages.social_links import Socialinks


class Test_Social_links:
    @allure.feature("Draft Pages Influencers")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=29)
    def test_social_links(self, ses_init,request):
        # remove_files_in_directory(f"{os.getcwd()}/screenshots")
        # screen = recording_and_capturing_screen(ses_init, request.node.name)
        obj = Socialinks(ses_init)
        obj.social_links()



