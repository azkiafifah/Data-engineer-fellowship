from google.cloud import storage
"""Uploads a file to the bucket."""
# The ID of your GCS bucket
bucket_name = "datafellow-7"

# The path to your file to upload
source_file_name = "file 2.txt"

# The ID of your GCS object
destination_blob_name = "file 2.txt"

# The ProjectID
project_id = 'data-fellowship-7'

# Initialise a client
storage_client = storage.Client(project_id)
# Create a bucket object for our bucket
bucket = storage_client.bucket(bucket_name)
# Create a blob object from the filepath
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)

print(
    "File {} uploaded to {}.".format(
        source_file_name, destination_blob_name
    )
)