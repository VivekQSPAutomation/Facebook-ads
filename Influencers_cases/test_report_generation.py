import os

import pytest

from Influncers_pages.reportCreation import ReportCreation


class Test_report_generate:
    @pytest.mark.run(order=41)
    def test_report_generate(self):
        json_directory = f"{os.getcwd()}/Report/"
        output_path = f"{os.getcwd()}/allure-report/"
        self.report = ReportCreation()
        self.report.run_allure_generate(json_directory, output_path)
