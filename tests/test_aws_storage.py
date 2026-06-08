import unittest

from src.cloud_storage.aws_storage import SimpleStorageService


class FakeS3Object:
    def __init__(self, key):
        self.key = key


class FakeObjectCollection:
    def __init__(self, objects):
        self._objects = objects

    def filter(self, Prefix):
        return [obj for obj in self._objects if obj.key.startswith(Prefix)]


class FakeBucket:
    def __init__(self, objects):
        self.objects = FakeObjectCollection(objects)


class TestSimpleStorageServiceFileLookup(unittest.TestCase):
    def setUp(self):
        self.storage = SimpleStorageService.__new__(SimpleStorageService)

    def test_get_file_object_prefers_exact_key_over_prefix_matches(self):
        exact_model = FakeS3Object("model.pkl")
        self.storage.get_bucket = lambda _: FakeBucket(
            [FakeS3Object("model.pkl.backup"), exact_model]
        )

        result = self.storage.get_file_object("model.pkl", "test-bucket")

        self.assertIs(result, exact_model)

    def test_get_file_object_reports_missing_key(self):
        self.storage.get_bucket = lambda _: FakeBucket([])

        with self.assertRaises(Exception) as context:
            self.storage.get_file_object("model.pkl", "test-bucket")

        self.assertIn(
            "S3 object 'model.pkl' was not found in bucket 'test-bucket'",
            str(context.exception),
        )


if __name__ == "__main__":
    unittest.main()
