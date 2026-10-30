import time

import requests
from dotenv import load_dotenv
import os

load_dotenv()


def upload_file() -> str:
    token = os.getenv("MINERU_TOKEN")

    url = "https://mineru.net/api/v4/file-urls/batch"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "files": [
            {"name": "sample.pdf", "data_id": "abcd"}
        ],
        "model_version": "vlm"
    }
    file_path = ["../assets/sample.pdf"]
    try:
        response = requests.post(url, headers=header, json=data)
        if response.status_code == 200:
            result = response.json()
            print('上传成功:{}'.format(result))
            batch_id = result["data"]["batch_id"]
            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                print('batch_id:{},urls:{}'.format(batch_id, urls))
                for i in range(0, len(urls)):
                    with open(file_path[i], 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{urls[i]} upload success")
                        else:
                            print(f"{urls[i]} upload failed")
            else:
                print('apply upload url failed,reason:{}'.format(result["msg"]))
            return batch_id
        else:
            print('response not success. status:{} ,result:{}'.format(response.status_code, response))
    except Exception as err:
        print(err)

def query_task_process(batch_id: str):
    token = os.getenv("MINERU_TOKEN")
    url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    res = requests.get(url, headers=header)
    while res.json()["data"]["extract_result"][0]["state"] != "done":
        print('当前状态为running，等待3秒后重试')
        time.sleep(3)
        res = requests.get(url, headers=header)
        print(res.status_code)
        print(res.json()["data"]["extract_result"][0]["state"], end="\n\n=================\n\n")
    print("提取结果为：", res.json()["data"]["extract_result"][0]["full_zip_url"])

if __name__ == "__main__":
    batch_id = upload_file()
    print("=================================")
    query_task_process(batch_id)
