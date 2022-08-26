import nmap


# 内网主机信息探针
# 1.原生利用ping进行获取
# 2.原生利用icmp,tcp,udp等协议获取
# 3.利用第三方模块库nmap等加载扫描获取
def nmapscan():
    nm = nmap.PortScanner()
    try:
        data = nm.scan(hosts='192.168.76.0/24', arguments='-T4 -F')
        print(nm.all_hosts())
        print(nm.csv())
        print(data)
    except Exception as err:
        print("error")


if __name__ == '__main__':
    nmapscan()
