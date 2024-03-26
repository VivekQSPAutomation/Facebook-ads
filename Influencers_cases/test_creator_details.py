import allure
import pytest

from Influncers_pages.Creator_Details import CreatorPages


class Test_Creator:
    @allure.feature("Creator Details Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.high
    @pytest.mark.run(order=11)
    def test_creator_details(self, ses_init,request):

        obj = CreatorPages(ses_init)
        status =obj.get_creator_details()
        assert status

