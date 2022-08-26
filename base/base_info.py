import socket, os
import time
from whois import whois
import sys


# 域名反查IP地址
def ip_check(url):
    ip = socket.gethostbyname(url)
    print(ip)


# 识别目标是否存在CDN
# 采用nslookup执行结果进行返回IP解析数据判断
# 利用python调用nslookup
# cdn_data = os.system('nslookup www.xiaodi8.com')   实验室system可以执行命令，但是没有ip解析结果
# print(cdn_data)
def cdn_check(url):
    cdn_data = os.popen('nslookup ' + url).read()
    print(cdn_data)
    # 由于ip地址是由x.x.x.x构造，那么就可以通过点数来判断是否存在cdn，>10就存在cdn
    # 为什么是10呢？因为nslookip还显示域名信息存在“点”，当然这种判定并不准确
    print(cdn_data.count('.'))
    # 也可以加分支来直接显示是否存在cdn
    if (cdn_data.count('.') > 10):
        print('存在CDN')
    else:
        print('不存在CDN')


# 端口扫描
# 1、原生自写socket协议tcp，udp扫描
# 2、调用第三方massan，nmap等扫描
# 3、调用系统工具脚本执行
def ports_check(url):
    ports = {'80', '1433', '3306', '8080', "9090", '8089', '8888'}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in ports:
        result = server.connect_ex((url, int(port)))
        if result == 0:
            print(port + ':open')
        else:
            print(port + ':close')


# whois查询
# 第三方库进行whois查询也可以利用网络接口查询
# whois第三方库名是python-whois，安装whois库会报错
def whois_check(url):
    who_data = whois('www.xiaodi8.com')
    print(who_data)


# 子域名查询
# 1.利用字典记载爆破进行查询
# 2.利用 bing 或第三方接口进行查询
def zym_check(url):
    urls = url.replace('www', '')
    for zym_data in open('D:\BaiduNetdiskDownload\Python开发源码资料-小迪安全\day76\dic.txt'):  # dic是子域名字典
        zym_data = zym_data.replace('\n', '')
        url = zym_data + urls
        try:
            ip = socket.gethostbyname(url)
            print(url + '|' + ip)
            time.sleep(0, 1)
        except Exception as e:
            pass


# 主函数调用
if __name__ == '__main__':
    # python参数形式执行
    check = sys.argv[1]
    url = sys.argv[2]
    if check == '-all':
        ip_check(url)
        whois_check(url)
        cdn_check(url)
        ports_check(url)
        zym_check(url)
