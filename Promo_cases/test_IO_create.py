import allure
import pytest

from Promo_pages.IOcreation import IOcreation


class Test_IO:
    def IO_object(self, ses_init):
        self.io = IOcreation(ses_init)
        return self.io

    @allure.feature("Promo IO Functionality")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=2)
    def test_iocreate_page(self, ses_init, request):
        io = self.IO_object(ses_init)
        status = io.IOcreate()
        assert status
