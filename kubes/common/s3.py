""" Connector and methods to access S3 resource """


import logging
import os

import boto3
import pandas as pd


class S3BucketConnector:
    """
    Class for interacting with S3 Buckets
    """

    def __init__(self, access_key: str, secret_key: str, bucket: str):
        """
        Constructor for S3BucketConnector

        :param access_key: access key for accessing S3
        :param secret_key: secret key for accessing S3
        :param endpoint_url: endpoint url to S3
        :param bucket: S3 bucket name
        """

        self._logger = logging.getLogger(__name__)
        self.session = boto3.Session(
            aws_access_key_id=os.environ[access_key],
            aws_secret_access_key=os.environ[secret_key],
        )
        self._s3 = self.session.resource(service_name="s3")
        self._bucket = self._s3.Bucket(bucket)

    def get_file(self):
        """
        Get csv file from s3 bucket and return a string
        """
        self._logger.debug("connected to database")

        df = pd.read_csv(
            self._bucket.Object(key="data/results-20230311-125822.csv")
            .get()
            .get("Body")
        ).to_string()

        return df
