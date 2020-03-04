# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/17

"""设置简单的button响应"""

import Tkinter as tk
window = tk.Tk()
window.title(u"公示图大战分布图")
window.geometry("400x320")
window.iconbitmap(default = r"toolbox.ico")

# 图形界面设置标签
var = tk.StringVar()
l = tk.Label(window, textvariable=var, text = u"公示图处理", bg = "red",
			 width = 8, height = 8)
l.pack()
getText = tk.Entry(window,show=None)
getText.pack()





# 第5步，在窗口界面设置放置Button按键,连接函数hit_me
b = tk.Button(window, text='hit me', font=('Arial', 12),
			  width=10, height=1, command=hit_me)
b.pack()
# 主循环
window.mainloop()