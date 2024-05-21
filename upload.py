import google.cloud
import os
from google.cloud import storage
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("xxxx.json")

print(os.path.abspath(__file__))

"""Uploads a file to the bucket."""
# The ID of your GCS bucket
# bucket_name = "your-bucket-name"
# The path to your file to upload
# source_file_name = "local/path/to/file"
# The ID of your GCS object
# destination_blob_name = "storage-object-name"
"""Downloads a blob from the bucket."""
# The ID of your GCS bucket
# bucket_name = "your-bucket-name"

# The ID of your GCS object
# source_blob_name = "storage-object-name"

# The path to which the file should be downloaded
# destination_file_name = "local/path/to/file"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    purl = blob.public_url
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    print(purl)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


upload_blob("<<bucket_name>>","<<source_file_name>>","<<destination_blob_name>>")


# download_blob("<<bucket_name>>","<<source_blob_name>>","<<destination_file_name>>")
