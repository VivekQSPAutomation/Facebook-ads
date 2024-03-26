import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Union

from pydantic import BaseModel


class Message(BaseModel):
    host: str
    port: int

    def send_mail(
        self,
        sender: str,
        receivers: Union[str, list],
        password: str,
        subject: str,
        messages: str,
    ):
        try:
            email = smtplib.SMTP_SSL(host=self.host, port=self.port)
            email.login(sender, password)

            msg = MIMEMultipart()
            msg["From"] = sender
            msg["To"] = ",".join(receivers) if type(receivers) == list else receivers
            msg["CC"] = ""
            msg["Subject"] = subject
            msg.attach(MIMEText(messages, "html"))
            email.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
            email.close()
        except (smtplib.SMTPRecipientsRefused, Exception) as err:
            logging.error(err)
