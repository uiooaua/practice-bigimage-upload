import os
from google.cloud import storage
from google.oauth2 import service_account
from concurrent.futures import ThreadPoolExecutor

# ストレージクライアントの取得
credentials = service_account.Credentials.from_service_account_file(
    'banana-ojt-d74de788e054.json',  # サービスアカウントキー名の指定
    scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
)

storage_client = storage.Client(
    credentials=credentials,
    project=credentials.project_id,
)

def download_chunks_concurrently(bucket_name, blob_name, file_path, chunk_size=5242880):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    # 各チャンクの範囲を計算
    blob.reload()
    total_size = blob.size
    ranges = [(start, min(start + chunk_size - 1, total_size - 1))
              for start in range(0, total_size, chunk_size)]
    
    def download_range(start, end):
        return blob.download_as_bytes(start=start, end=end)
    
    # 並行してチャンクをダウンロード
    with ThreadPoolExecutor() as executor:
        chunks = list(executor.map(lambda r: download_range(*r), ranges))
    
    # チャンクを結合してファイルに保存
    with open(file_path, 'wb') as f:
        for chunk in chunks:
            f.write(chunk)
    
    return file_path

# main
if __name__ == "__main__":
    # バケット名とファイル名の指定
    bucket_name = 'test-iterra'
    blob_name = '20230911_0945_50m_TADECO_MAP1.tif'

    # ダウンロード先のファイルパス
    output_file_path = 'joined_20230911_0945_50m_TADECO_MAP1.tif'
    
    # download_chunks_concurrentlyメソッドを使用してダウンロード
    download_chunks_concurrently(bucket_name, blob_name, output_file_path)

    print(f"File {blob_name} was downloaded and saved as {output_file_path}.")
