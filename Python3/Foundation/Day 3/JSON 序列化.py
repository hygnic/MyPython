# User: hygnic
# Date: 2018/9/3
"""
序列化，比如将字典序列化后转为字符串，再转化为bytes进行传输，
在接收端再转换回来
"""
import json
dic = {'name': 'hygnic', 'age': 18}
f = open('JS_dump', 'w')
json.dump(dic, f)
f.close()
#---------------------------------
# dump和dumps的区别

dic = {'name': 'hygnic', 'age': 18}
f = open('JS_dumps', 'w')
data = json.dumps(dic)
f.write(data)
f.close()


# dump保存数据 load读取数据

# 模块pickle可用于存储函数和类，用法和json一样
# shelve模块