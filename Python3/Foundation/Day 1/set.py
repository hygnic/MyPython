# User: hygnic
# Date: 2018/8/27


# 集合set可以去重
s = ['hygnic', 'hello', 1122, 1122, 'hygnic']
print(set(s))

print(list(s))

# set中不能放dic和list的， 因为他们是可变的，是不可哈希的
# ————set是无序的，不重复的，可变的————

# s.pop()
# # 清空容器中的东西，容还在
# s.clear()
# s.add()
# s.update()
# ...etc

print(set('alex'))

a = set('fuck')
print(a)

# 还有差集，并集，交集