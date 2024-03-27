import time

import allure
import pytest

from Config.test_order import Order
from Influncers_pages.Social_pages import Social_pages


class Test_Social:
    @allure.feature("Socail Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.facebook_login)
    def test_facebook_author(self, ses_init):
        obj = Social_pages(ses_init)
        status = obj.facebook_author()
        assert status
        time.sleep(5)

    @allure.feature("Social Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.pinterest_login)
    def test_pinterest_author(self, ses_init):
        obj = Social_pages(ses_init)
        status  = obj.pinterest_author()
        assert status


        time.sleep(5)

    @allure.feature("Socail Pages Influencers")
    @allure.story("High Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.Insta_login)
    def test_instagram_author(self, ses_init):
        obj = Social_pages(ses_init)
        status = obj.instagram_author()
        assert status
        time.sleep(5)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.high
    @pytest.mark.run(order=Order.social_button)
    def test_next_button(self, ses_init):
        obj = Social_pages(ses_init)
        obj.next_button()

