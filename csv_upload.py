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
    change_suffix('test-cat.csv', '.csv', '.jpg')

# バケット内へのファイルのアップロード
'''bucket = storage_client.get_bucket('test-iterra') # バケット名の指定
blob = bucket.blob('test-cat-csv') # バケット内のファイル名の指定
blob.upload_from_filename('test-cat.csv') # ローカルファイル名の指定'''