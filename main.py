# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import time

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

response = requests.get('http://casad.cas.cn/ysxx2017/ysmdyjj/jskxb_124286/')

responsestr = response.text
mainpg = responsestr.encode("iso-8859-1").decode('utf-8')
mainbs = BeautifulSoup(mainpg,'html.parser')
namebs = mainbs.find(id='allNameBar').find_all(href=re.compile(r'http://casad.cas.cn/sourcedb_ad_cas/zw2/ysxx/jskxb/.*'))

pg = []
# print(namebs)
count = 0
namedt =[]

for i in namebs:
    url = i['href']
    # print(url)
    tmpres = requests.get(url)
    tmppg = tmpres.text.encode("iso-8859-1").decode('utf-8')
    # print(url)
    while tmppg == None:
        tmppg = requests.get(url)
        time.sleep(1)
    tmpbs = BeautifulSoup(tmppg,'html.parser')
    # print(tmpbs)
    tmpstr = tmpbs.find(class_='contentTest').find('p').text
    # break
    name = i.text
    namedt.append([name, tmpstr])
    count +=1

print(namedt)

dt = pd.DataFrame(namedt)
dt.to_csv('name.csv',encoding='utf-8')


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
