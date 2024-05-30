import pathlib
import shutil
from google.cloud import storage
from google.oauth2 import service_account

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json', # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)
'''storage_client = storage.Client(
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

if __name__ == '__main__':
    bucket_name = 'test-iterra'
    contents = 'test-cat.csv'
    destination_blob_name = 'nyanko.jpg'

'''    
def change_suffix(file_name, from_suffix, to_suffix):
    #ファイルの拡張子を得る
    sf = pathlib.PurePath(file_name).suffix

    #変更対象か判断する
    if sf == from_suffix:
        #拡張子を除くファイル名を得る
        st = pathlib.PurePath(file_name).stem

        #変更後のファイル名を得る
        to_name = st + to_suffix

        #ファイル名を変更する
        shutil.move(file_name, to_name)

if __name__ == '__main__':
    change_suffix('./image/test-cat.jpg', '.jpg', '.csv')'''