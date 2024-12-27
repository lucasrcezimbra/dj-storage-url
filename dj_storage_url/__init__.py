from urllib.parse import parse_qs, urlparse, urlsplit


def strtobool(value):
    value = value.lower()
    if value in ("t", "true", "1"):
        return True
    elif value in ("f", "false", "0"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (value,))


def file_system_storage(url):
    parsed_url = urlparse(url)
    return {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": parsed_url.path,
        },
    }


def memory_storage(_):
    return {"BACKEND": "django.core.files.storage.MemoryStorage", "OPTIONS": {}}


def s3_storage(url):
    parsed_url = urlparse(url)
    querystring = parse_qs(parsed_url.query)
    return {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": parsed_url.netloc,
            **({"location": parsed_url.path} if parsed_url.path else {}),
            **(
                {"gzip": strtobool(querystring["gzip"][0])}
                if "gzip" in querystring
                else {}
            ),
        },
    }


def unknown_storage(url):
    scheme, _ = url.split("://")
    return {"BACKEND": scheme, "OPTIONS": {}}


SCHEME_TO_CONFIG = {
    "file": file_system_storage,
    "memory": memory_storage,
    "s3": s3_storage,
}


def parse(url):
    scheme, *_ = urlsplit(url)
    return SCHEME_TO_CONFIG.get(scheme, unknown_storage)(url)
