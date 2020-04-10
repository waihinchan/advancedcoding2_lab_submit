from bs4 import BeautifulSoup
import requests
import pymongo
a = 1
client = pymongo.MongoClient('127.0.0.1',27017)
xiaozhu = client['xiaozhu']
xiaozhuinfo = xiaozhu['xiaozhuinfo']
#mogodb的常规操作

url ='http://london.xiaozhu.com/275-4500yuan-duanzufang-1/'
xiaozhudata = requests.get(url)
#请求链接#
soup = BeautifulSoup(xiaozhudata.text,'lxml')
#转换成文本#
# ========================到这一步测试没有问题========================
imgs = soup.select('li:nth-child(n) > a > img')
#imgs测试成功
prices = soup.select('div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
#price测试成功
titles = soup.select('div.result_intro > a > span')
#titile测试成功
#zip的用处是https://www.runoob.com/python/python-func-zip.html 将列表打包成元祖
#实际上imgs、prices、titles都是可以迭代的对象(列表)
#zip就是把他们打包成一个一个的，方便可以一次性做循环
#然后就是data，data是一个字典（加了这个大括号{}），然后就是用逗号，来分割。冒号前是键（类似于序号），冒号后是值
#所以data就是一个字典
for img,price,title in zip(imgs,prices,titles):
    data = {
        "img": img.get("lazy_src"),
        "price": int(price.get_text()),
        "title":title.get_text()
    }
    xiaozhuinfo.insert_one(data)
    #把字典写入xiaozhu这个数据库里面的xiaozhuinfo列表中
print('done')
#搞定了不难

