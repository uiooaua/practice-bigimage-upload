import io
from google.cloud import storage
from google.oauth2 import service_account
import csv

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json', # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)

#メモリからオブジェクトをアップロードする（公式より）
def upload_blob_from_memory(bucket_name, contents, destination_blob_name):

    storage_client = storage.Client(
        credentials = credentials,
        project = credentials.project_id,
    )
    bucket = storage_client.bucket(bucket_name)

    # create blob object
    blob = bucket.blob(destination_blob_name)
    # upload binary data
    blob.upload_from_string(contents)

    print(f"{destination_blob_name} uploaded.")

#座標リストをアップロードする
try:
    result = [[123, 456], [111, 222], [333, 444], [999, 999]]

    # リストをCSV形式の文字列に変換
    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerows(result)
    csv_data = output.getvalue()
    output.close()

    destination_blob_name = 'result.csv'
    bucket_name = 'test-iterra'
    upload_blob_from_memory(bucket_name, csv_data, destination_blob_name)

except Exception as e:
    print(f"Error: {e}")