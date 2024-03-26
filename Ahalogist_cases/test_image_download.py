import allure
import pytest

from Ahalogist_pages.Images_download import Images


class Test_Download:
    def download_object(self, ses_init):
        self.call = Images(ses_init)
        return self.call

    @allure.feature("Dynamic Callout")
    @allure.story("Critical Tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.run(order=37)
    def test_download(self, ses_init, request):
        call = self.download_object(ses_init)
        call.imagedownload()
