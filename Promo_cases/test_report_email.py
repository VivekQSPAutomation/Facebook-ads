import datetime
import os

import pytest

from Config.config import TestData
from Promo_pages.message import Message


class Test_reportemail:
    @pytest.mark.run(order=39)
    def test_sending_email(self):
        # Current date and time
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d-%m-%Y   %H:%M:%S")

        self.report = Message(host=TestData.smtp_host, port=TestData.smtp_port)
        converted_string = "".join([char.lower() for char in os.environ["Report_name"]])
        self.report.send_mail(
            TestData.smtp_email_id,
            ["vigupta@quotient.com", "pvidhyadharan@quotient.com","rasingh@quotient.com"],
            TestData.smtp_password,
            f"QSP Automation Report --- {formatted_datetime}",
            f"""<!DOCTYPE html>
                <html>
                <body>
                  <p>https://{converted_string}--qspautomation.netlify.app</p>
                  <a href='{os.environ.get('preview')}' target='_blank'>Facebook Preview Link</a>
                </body>
                </html>
            """
        )
