# 逐行提取
path = 'pi_digits.txt'
with open(path) as file_object:
    for line in file_object:
        print('look ' + line.rstrip())
# 全文提取
path = 'pi_digits.txt'
with open(path) as file_object:
    content = file_object.read()
    print(content.rstrip()) #rstrip函数可以除去右边的空白/换行符

#将文本内容转移出来
path = 'pi_digits.txt'
with open(path) as file_object:
    content = file_object.readlines()
print('\n')
for line_1 in content:
    print(line_1.rstrip())

path = 'pi_digits.txt'
with open(path) as file_object:
    content = file_object.readlines()
print('\n')
pi_strings = ''
for pi_string in content:
    pi_strings += pi_string.strip() #除去换行符，使数据变成一行
print(pi_strings)


# 文件写出
writing = 'lcc.txt'
with open(writing, 'w') as K_project:
    K_project.write('i love python\nas i do\n')
# 文件附加模式
writing = 'lcc.txt'
k = open(writing, 'a')
k.write('i love')


# 使用try-except代码块处理零除错误
#这个zerodivisionerror只是帮助你理解
# print('\n')
# print('input two numbers')
# print("enter 'q' to quit")
# while True:
#     first = input('enter your first number')
#     if first == 'q':
#         break
#     second = input('enter your second number')
#     if second =='q':
#         break
#     try:
#         answer = int(first)/int(second)
#     except ZeroDivisionError:
#         print('error')
#     else:
#         print(answer)
#     break


# 单词计算
# split()函数将文本拆成单词组合成列表
print('\n')
def count_word(bookname):
    try:
        with open('alice in woderland.txt') as count_project:
            alice_contents = count_project.read()
            numb = alice_contents.split()
    except:
        print('error') #未找到文件
    else:
        number_words = len(numb)
        print(number_words)
bookname = 'alice in woderland.txt'
count_word(bookname)


#将数据存储到json文件中
print('\n')
import json
number_j = [1,2,3,4]
with open('file_j_1.json', 'w') as o_b:
    json.dump(number_j, o_b)
#读取存储在json文件中的数据
with open('file_j_1.json') as o_a:
    number_j_load = json.load(o_a)
print(number_j_load)
