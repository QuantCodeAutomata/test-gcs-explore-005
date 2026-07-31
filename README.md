# GCS Bucket Explorer — lcm-data-lime-fintech

Lists the top-level prefixes ("folders") and files in `gs://lcm-data-lime-fintech`
using the `google-cloud-storage` Python client.

## Requirements

```
pip install -r requirements.txt
```

## Usage

```bash
# Credentials are loaded automatically from GOOGLE_APPLICATION_CREDENTIALS
python list_bucket.py
```

Prints discovered top-level prefixes and files, then outputs `GCS_TEST_OK`
on success.
