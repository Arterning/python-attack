import requests
url = "http://xxx.xxx.xxx.xxx/upload-labs/upload/zoe.php"
while True:
    html = requests.get(url)
    if html.status_code == 200:
        print("OK")
        break
