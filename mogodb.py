import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
#本地服务器
# 前面的walden是python对象，类似如果你要调用在python内调用walden的接口
#后面是数据库的名字
sheet_test = walden['sheet_test']
#同上
path = '/Users/waihin/Desktop/fk!.txt'
with open(path,'r') as f:
    lines = f.readlines()
    #print(lines)
    for index, line in enumerate(lines):
        #这个函数有点东西，就是给他们数数
        #lines在上面就是读取了walden有多少行每行有什么
        #enumerate了这个lines之后就会生成类似
        #1，第一行内容，2，第二行内容，3，第三行内容的enumerate对象
        #这个对象是可以用于迭代的
        #这里的index对应的就是1、2、3、4
        #这里的line就是对应的第一行内容，第二行内容，第三行内容
        #然后words就是使用计算每一行有多长
        #https://blog.csdn.net/anneqiqi/article/details/61192065这个说了split参数的用法
        data = {
            'index':index,
            'line':line,
            'wrods':len(line.split())
        }
        sheet_test.insert_one(data)

