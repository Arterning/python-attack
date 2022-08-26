import requests
import json
import time


# 通过前期信息搜集得到的大量url地址 之后我们可以配合sqlmap api接口进行批量的sql检测
def sqlmapapi(url):
    headers = {
        'Content-Type': 'application/json'
    }
    scan_url = {
        'url': url
    }
    scan_task_url = 'http://127.0.0.1:8775/task/new'
    scan_task = requests.get(scan_task_url)
    # print(scan_task.json())
    scan_task_id = scan_task.json()['taskid']
    # print(scan_task_id)
    if 'success' in scan_task.content.decode('utf-8'):
        print('sqlmapapi task create success...')
        scan_task_set_url = 'http://127.0.0.1:8775/option/' + scan_task_id + '/set'
        scan_task_set = requests.post(scan_task_set_url, data=json.dumps(scan_url), headers=headers)
        # print(scan_url)
        # print(scan_task_set.content.decode('utf-8'))
        if 'success' in scan_task_set.content.decode('utf-8'):
            print('sqlmapapi taskid set success')
            scan_start_url = 'http://127.0.0.1:8775/scan/' + scan_task_id + '/start'
            scan_start = requests.post(scan_start_url, data=json.dumps(scan_url), headers=headers)
            # print(scan_start.content.decode('utf-8'))
            if 'success' in scan_start.content.decode('utf-8'):
                print('sqlmapapi scan start success')
                while 1:
                    scan_status_url = 'http://127.0.0.1:8775/scan/' + scan_task_id + '/status'
                    scan_status = requests.get(scan_status_url)
                    # print(scan_status.content.decode('utf-8'))
                    if 'running' in scan_status.content.decode('utf-8'):
                        print(url + '->scan running')
                        pass
                    else:
                        print('sqlmapapi scan end')
                        scan_data_url = 'http://127.0.0.1:8775/scan/' + scan_task_id + '/data'
                        scan_data = requests.get(scan_data_url).content.decode('utf-8')
                        with open(r'scan_result.txt', 'a+') as f:
                            f.write(url + '\n')
                            f.write(scan_data + '\n')
                            f.write('==========python sqlmapapi by xiaodi==========' + '\n')
                            f.close()
                        # print('delete taskid')
                        scan_deltask_url = 'http://127.0.0.1:8775/task/' + scan_task_id + '/delete'
                        scan_deltask = requests.get(scan_deltask_url)
                        if 'success' in scan_deltask.content.decode('utf-8'):
                            print('delete taskid success')
                        break
                    time.sleep(3)


if __name__ == '__main__':
    print("scanurl checking ok.....")
    for url in open('url.txt'):
        url = url.replace('\n', '')
        sqlmapapi(url)
