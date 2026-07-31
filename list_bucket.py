"""
list_bucket.py — List top-level prefixes and files in gs://lcm-data-lime-fintech.

Auth is provided automatically via GOOGLE_APPLICATION_CREDENTIALS (ADC).
No data is downloaded.
"""
import os
from google.cloud import storage

BUCKET_NAME = os.environ.get("GCS_BUCKET", "lcm-data-lime-fintech")


def list_top_level():
    client = storage.Client()
    it = client.list_blobs(BUCKET_NAME, prefix="", delimiter="/")
    files = list(it)              # objects at root level (consumes the iterator)
    prefixes = sorted(it.prefixes)  # "folder" prefixes one level down
    return files, prefixes


def main():
    files, prefixes = list_top_level()

    print("=== Top-level folders (prefixes) ===")
    if prefixes:
        for p in prefixes:
            print(f"  {p}")
    else:
        print("  (none)")

    print("\n=== Top-level files ===")
    if files:
        for f in files:
            print(f"  {f.name}  ({f.size} bytes)")
    else:
        print("  (none)")

    print("\nGCS_TEST_OK")


if __name__ == "__main__":
    main()
