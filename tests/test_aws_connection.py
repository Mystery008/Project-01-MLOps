import importlib
import unittest
from unittest.mock import patch


class TestS3ClientEnvironmentLoading(unittest.TestCase):
    def test_s3_client_loads_aws_credentials_from_dotenv_file(self):
        aws_connection = importlib.import_module("src.configuration.aws_connection")
        aws_connection = importlib.reload(aws_connection)

        with patch.object(aws_connection.boto3, "resource") as mock_resource, patch.object(
            aws_connection.boto3, "client"
        ) as mock_client:
            aws_connection.S3Client.s3_resource = None
            aws_connection.S3Client.s3_client = None

            aws_connection.S3Client()

            self.assertIsNotNone(mock_resource.call_args.kwargs["aws_access_key_id"])
            self.assertIsNotNone(mock_resource.call_args.kwargs["aws_secret_access_key"])
            self.assertIsNotNone(mock_client.call_args.kwargs["aws_access_key_id"])
            self.assertIsNotNone(mock_client.call_args.kwargs["aws_secret_access_key"])


if __name__ == "__main__":
    unittest.main()
