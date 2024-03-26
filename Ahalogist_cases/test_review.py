import allure
import pytest

from Ahalogist_pages.AhalogistLogin import Welcome_session
from Ahalogist_pages.Review_influencers import ReviewInflu


class Test_Review:
    def review_influ(self, ses_init):
        self.review = ReviewInflu(ses_init)
        return self.review

    @allure.feature("Onboarding Influences")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=30)
    def test_review(self, ses_init):
        review = self.review_influ(ses_init)
        review.review_influencer()
