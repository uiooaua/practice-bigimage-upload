import os
from google.cloud import storage
from google.oauth2 import service_account

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json', # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)

# CSVに変更 
def change_suffix(file_path, new_suffix):
    # 拡張子を除いたパスの取得
    bese = os.path.splitext(file_path)[0]

    return bese + new_suffix

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

    print(
        f"{destination_blob_name} uploaded."
    )

# ローカルの画像ファイルをバイナリとして読み込む
try:
    file_path = 'test-dog.jpg'
    with open(file_path, 'rb') as image_file:
        # ファイルの中身を読み込み変数に格納している
        binary_data = image_file.read()

    # change to .csv
    destination_blob_name = change_suffix(file_path, '.csv')
    bucket_name = 'test-iterra'
    upload_blob_from_memory(bucket_name, binary_data, destination_blob_name)

except:
    print("Error")