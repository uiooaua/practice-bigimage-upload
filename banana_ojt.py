import os
import glob
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
'''
# バケット内のファイル一覧の取得
bucket = storage_client.get_bucket('test-iterra')
blobs = bucket.list_blobs()

dst_dir = 'images'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('./images/*.jpg')

for f in files:
    img = Image.open(f) # 画像オブジェクトの生成
    resized = img.resize((256,256))
    root, ext = os.path.splitext(f)
    basename = os.path.basename(root)
    resized.save(os.path.join(dst_dir,basename + '_resize' + ext))


#バケット内からのファイルのダウンロード
bucket = storage_client.get_bucket('test-iterra') # バケット名の指定
blob = storage.Blob('th.jpg', bucket) # バケット内のファイル名の指定 
content = blob.download_as_string() # 画像ファイルデータの中身をcontentに入れている
with open('test-cat.jpg', mode='wb') as f: # ローカルファイル名の指定 
    f.write(content)
'''
# バケット内へのファイルのアップロード
bucket = storage_client.get_bucket('test-iterra') # バケット名の指定
blob = bucket.blob('test-cat.jpg') # バケット内のファイル名の指定
blob.upload_from_filename('./image/test-cat.jpg') # ローカルファイル名の指定
