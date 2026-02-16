import pytest

from dj_storage_url import parse


class TestInMemoryStorage:
    def test_parse(self):
        assert parse("memory://") == {
            "BACKEND": "django.core.files.storage.InMemoryStorage",
            "OPTIONS": {},
        }


class TestFileSystemStorage:
    def test_parse(self):
        assert parse("file:///tmp/files") == {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
            "OPTIONS": {
                "location": "/tmp/files",
            },
        }

    def test_relative_location(self):
        parsed = parse("file://tmp/media")
        assert parsed["OPTIONS"]["location"] == "tmp/media"

    @pytest.mark.skip(reason="TODO")
    def test_with_optional_options(self):
        url = "file:///tmp/files?base_url=/my/base/url&file_permissions_mode=0o644&directory_permissions_mode=0o644"
        assert parse(url) == {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
            "OPTIONS": {
                "location": "/tmp/files",
                "base_url": "/my/base/url",
                "file_permissions_mode": 0o644,
                "directory_permissions_mode": 0o644,
            },
        }


class TestS3Storage:
    def test_parse(self):
        assert parse("s3://my-bucket") == {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "bucket_name": "my-bucket",
            },
        }

    def test_with_location(self):
        assert parse("s3://my-bucket/my-folder") == {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "bucket_name": "my-bucket",
                "location": "/my-folder",
            },
        }

    @pytest.mark.parametrize("gzip", ["True", "true", "1"])
    def test_gzip_true(self, gzip):
        assert parse(f"s3://my-bucket?gzip={gzip}") == {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "bucket_name": "my-bucket",
                "gzip": True,
            },
        }

    @pytest.mark.parametrize("gzip", ["False", "false", "0"])
    def test_gzip_false(self, gzip):
        assert parse(f"s3://my-bucket?gzip={gzip}") == {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "bucket_name": "my-bucket",
                "gzip": False,
            },
        }


class TestCustomStorage:
    def test_parse(self):
        assert parse("myproject.myapp.MyCustomStorage://") == {
            "BACKEND": "myproject.myapp.MyCustomStorage",
            "OPTIONS": {},
        }

    @pytest.mark.skip(reason="TODO")
    def test_with_options(self):
        assert parse("myproject.myapp.MyCustomStorage://?foo=bar") == {
            "BACKEND": "myproject.myapp.MyCustomStorage",
            "OPTIONS": {"foo": "bar"},
        }
