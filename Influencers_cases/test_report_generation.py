import os

import pytest

from Config.test_order import Order
from Influncers_pages.reportCreation import ReportCreation


class Test_report_generate:
    @pytest.mark.run(order=Order.Report_generate)
    def test_report_generate(self):
        json_directory = f"{os.getcwd()}/Report/"
        output_path = f"{os.getcwd()}/allure-report/"
        self.report = ReportCreation()
        self.report.run_allure_generate(json_directory, output_path)
