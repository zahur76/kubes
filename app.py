"""
App to Run main program
"""

import logging
import logging.config

import yaml
from yaml.loader import SafeLoader

from kubes.common.s3 import S3BucketConnector
from kubes.common.sender import SendMail


def main():
    # Open and parsing YAML file
    with open("config/config.yml") as f:
        config = yaml.load(f, Loader=SafeLoader)

    # configure logging
    log_config = config["logging"]
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)

    # reading s3 configuration
    s3_config = config["s3"]

    # creating the S3BucketConnector class instances for source and target

    s3_bucket_src = S3BucketConnector(
        access_key=s3_config["access_key"],
        secret_key=s3_config["secret_key"],
        bucket=s3_config["src_bucket"],
    )

    text_message = s3_bucket_src.get_file()

    logger.debug("Messaged Received")

    # email configuration
    email_config = config["email"]
    mail_con = SendMail(
        email_config["email_host"],
        email_config["email_user"],
        email_config["email_port"],
        email_config["email_pwd"],
    )

    mail_con.send_mail(text_message, "zahurmeerun@hotmail.com")


if __name__ == "__main__":
    main()
