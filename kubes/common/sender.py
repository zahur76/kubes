""" Connector and methods to send mail """


import logging
import os
import smtplib


class SendMail:
    """
    Class for creating STMP Email Connection
    """

    def __init__(self, email_host: str, email_user: str, port: int, email_pwd: str):
        """
        Constructor for Sending Mail
        :param email host:  email host
        :param email host user: email user
        :param port: Email Port
        """

        self._logger = logging.getLogger(__name__)
        self.smtpObj = smtplib.SMTP(email_host, port)
        self.smtpObj.login(email_user, os.environ[email_pwd])
        self.email_user = email_user

    def send_mail(self, message, receiver):
        try:
            self.smtpObj.sendmail(self.email_user, receiver, message)
            self._logger.debug("Mail Sent")
        except SMTPException as e:
            self._logger.warning(f"Error: {e}")
