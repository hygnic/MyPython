# User: hygnic
# Date: 2018/11/9

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:00:53 2018
要批量下载ladsweb.modaps.eosdis.nasa.gov上的数据前从cvs导出、合成下载链接
尝试PEP8风格
@author: 墨大宝
"""
import pandas as pd


def main(CSVPATH):
#    在cmd运行的Python中正常传入字符串，但是在Ipython控制台会多加一层单引号
    if CSVPATH.startswith("'"):
        CSVPATH = CSVPATH[1 : -1]
    TXTPATH = CSVPATH[:-4] + '导出.txt'
#    第2列是下载链接的部分，第1、3列无关
    links = pd.read_csv(CSVPATH, engine='python', usecols=[1],
                        header=None, skiprows=1)
#    links = links.values.tolist()
#    links= ['https://ladsweb.modaps.eosdis.nasa.gov' + y for x in links
#            for y in x]
    [links] = links.values.transpose().tolist()  # 比上一种方法简洁
#    补全下载链接
    links= ['https://ladsweb.modaps.eosdis.nasa.gov' + x for x in links]
    with open(TXTPATH, 'w') as txtFile:
        txtFile.write('\n'.join(links))
    print('\n\n完成！\n导出的下载链接文件与.csv同路径')


if __name__ == '__main__':
    print('\n**从cvs导出、合成ladsweb.modaps.eosdis.nasa.gov的下载链接**\n')
    CSVPATH = input('请将从ladsweb.modaps.eosdis.nasa.gov上导出的.csv文件' +
                    '拖拉至此（或者输入其绝对路径）:\n')
    main(CSVPATH)
else:
    raise ImportError('滚滚滚！')
# ---------------------
# 作者：墨大宝
# 来源：CSDN
# 原文：https://blog.csdn.net/modabao/article/details/79211243
# 版权声明：本文为博主原创文章，转载请附上博文链接！