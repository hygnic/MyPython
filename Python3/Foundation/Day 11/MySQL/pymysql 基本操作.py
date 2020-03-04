# User: hygnic
# Date: 2018/9/19
# 创建连接
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='831015',
                       db='homework') # charset='utf8' 部分情况需要加入
# 创建游标
cursor = conn.cursor()
# 执行
cursor.execute('insert into class(caption)values("四年五班")')
    # 执行函数都会返回一个值，表示受影响的行数

# 获取最后影响的行的自增数（即多份数据时，只显示最后一个的自增数）
auto_increment_id = cursor.lastrowid
print(auto_increment_id)

    # 其他执行方法：
        # 其一：
            # 参数传递,必须使用参数的形式

            # inp = input(">>>")
            # cursor.execute('insert into class(caption)values(%s)',inp)                   # cursor.execute('insert into class(caption)values(%s)' %inp) 这样不行，SQL注入
                    # 传入多个
                        # cursor.execute('insert into student(sname,gender,sid)values(%s,%s,%s)', ("燕丹","女",'8'))
                                                                                                    # 元组
                    # 传入多组
                        # l = [("燕丹", "女", '7'), ("燕丹2", "女", '9'), ("燕丹4", "女", '98')]
                        # cursor.executemany('insert into student(sname,gender,sid)values(%s,%s,%s)', l)
                                    # 可以使用列表变量l来代替也可以直接加上列表   注意是executemany（）



        # 其二：
            # 字符串格式化（不能使用，有很大的风险，有SQL注入的问题）

            # inp=input('>>>')
            # sql='insert into class(caption)values("%s")'
            # sql= sql %(inp,)
            #cursor.execute(sql)




# 存储过程的执行：

u=cursor.callproc('p2', args=(1, 22, 3, 4))
# 这里拿到的是结果集
procedure_result1 = cursor.fetchall()
print('here！ 结果集',procedure_result1)

print('*'*20)

h=cursor.execute("select @_p2_0,@_p2_1,@_p2_2,@_p2_3")
print(u,'>>>>',h)

# 这里拿到的是 @_p2_0 的值（一个数）
procedure_result2 = cursor.fetchall()
print('here!',procedure_result2)



# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 查看表，不用执行conn.commit()
cursor.execute('select * from class')   # 数据已经进入内存，所以fetchmany无法替代分页功能
    # 返回的是受影响的列表行数
info = cursor.fetchall()
    # 取得数据
        # 其他方法：
            # cursor.fetchone()  # 只取一个
            # cursor.fetchmany(5) # 表示取出5条数据
                # 注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，比如（不重要）：
                    # cursor.scroll(-1,mode='relative')  # 相对当前位置移动，将指正往后回退一个
                    # cursor.scroll(0,mode='absolute') # 相对绝对位置移动，将指针移动到开始的位置


            # 默认获取的数据是元祖类型，如果想要或者字典类型的数据（不重要）：
                # import pymysql
                #
                # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='831015',
                #                        db='homework')
                #
                # # 游标设置为字典类型
                # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
                # r = cursor.execute("call p1()")
                #
                # result = cursor.fetchone()
                #
                # conn.commit()
                # cursor.close()
                # conn.close()

print(info)



# 关闭游标
cursor.close()
# 关闭连接
conn.close()