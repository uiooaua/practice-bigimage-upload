from google.cloud import storage
from PIL import Image
import io

#google cloud storageのクライアントインスタンスを作成
#client = storage.Client()
client = storage.Client.from_service_account_json('banana-ojt-d74de788e054.json')
#バケットのインスタンスを取得
bucket = client.bucket('test-iterra')

#ファイルのblobインスタンスを取得
blob = bucket.blob('test-png.png')

# blobインスタンスをバイナリデータに変えて画像ファイルデータの中身をimgに入れている
# img　の中身はRGBの値でデータを持ってる
img = Image.open(io.BytesIO(blob.download_as_string()))
# ↑これでどんな拡張子のデータでも↓で保存するときに拡張子を選択して保存できる

img.save('sample.png')