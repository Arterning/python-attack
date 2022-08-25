import requests, time
from lxml import etree


def edu_list(page):
    for page in range(1, page + 1):
        try:
            url = 'https://src.sjtu.edu.cn/list/?page=' + str(page)
            data = requests.get(url).content
            # print(data)
            soup = etree.HTML(data.decode('utf-8'))
            result = soup.xpath('//td[@class=""]/a/text()')
            # print(result)
            results = '\n'.join(result)
            resultss = results.split()
            print(resultss)
            for edu in resultss:
                with open(r'src.txt', 'a+', encoding='utf-8') as f:
                    f.write(edu + '\n')
                    f.close()
        except Exception as e:
            time.sleep(0.5)
            pass


if __name__ == '__main__':
    edu_list(10)
