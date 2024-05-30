import pathlib
import shutil
from google.cloud import storage
from google.oauth2 import service_account

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json', # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)
storage_client = storage.Client(
        credentials = credentials,
        project = credentials.project_id,
    )
'''
def upload_blob_from_memory(bucket_name, contents, destination_blob_name):

    storage_client = storage.Client(
        credentials = credentials,
        project = credentials.project_id,
    )

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
    )
'''