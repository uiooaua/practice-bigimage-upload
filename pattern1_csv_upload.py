import csv
import os
from google.cloud import storage
from google.oauth2 import service_account

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json',  # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)

def upload_blob_from_file(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client(
        credentials=credentials,
        project=credentials.project_id,
    )

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"{destination_blob_name} uploaded from {source_file_name}.")

# 座標リストをローカルに保存し、アップロードする
try:
    result = [[123, 456], [111, 222], [333, 444], [999, 999]]
    local_csv_file = 'result.csv'
    
    # リストをCSV形式のファイルに保存
    with open(local_csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(result)

    destination_blob_name = 'result_pattern1.csv'
    bucket_name = 'test-iterra'
    
    # ローカルのCSVファイルをGoogle Cloud Storageにアップロード
    upload_blob_from_file(bucket_name, local_csv_file, destination_blob_name)

    # アップロード後にローカルファイルを削除（オプション）
    os.remove(local_csv_file)

except Exception as e:
    print(f"Error: {e}")
