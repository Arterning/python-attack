# 搜索引擎爬虫模拟及模拟真实用户
import requests
import time

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    # 模拟用户 Kit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
    # 模拟引擎 Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)
    # 更多爬虫引擎：https://www.cnblogs.com/iack/p/3557371.html
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider-render/2.0;+http://www.baidu.com/search/spider.html)',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'PHPSESSID=99d6a382f03de62bb8f51ba51e51550f',  # 根据当前访问 cookie
}

for paths in open('php_b.txt', encoding='utf-8'):
    url = 'http://192.168.0.109:8890/'
    paths = paths.replace('\n', '')
    urls = url + paths
    # 如需测试加代理，或加入代理池需加代理
    proxy = {
        'http': '127.0.0.1:7777'
    }
    try:
        code = requests.get(urls, headers=headers, verify=False).status_code
        print(urls + '|' + str(code))
        if code == 200 or code == 403:
            print(urls + '|' + str(code))
    except Exception as err:
        print('connecting error')
        # time.sleep(3)模拟用户需延时 引擎可用可不用（根据请求速度
