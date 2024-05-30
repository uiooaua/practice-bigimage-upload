import io
from PIL import Image
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
with open('./image/test-dog.jpg', 'rb') as image_file:
    # ファイルの中身を読み込み変数に格納している
    binary_data = image_file.read()

    bucket_name = 'test-iterra'
    destination_blob_name = 'pattern2-try-sample.csv'
    
    upload_blob_from_memory(bucket_name, binary_data, destination_blob_name)
