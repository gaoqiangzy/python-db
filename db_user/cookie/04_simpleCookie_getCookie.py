#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
import os
import cgitb
cgitb.enable()
print("Content-Type:text/html")
print("")
"""通过simpleCookie()
2.解析os.environ['HTTP_COOKIE']
"""
# print(os.environ)
# #从环境变量中获取cookie字符串
cookie_str=os.environ.get('HTTP_COOKIE')
# #创建一个simpleCookie对象
from http import cookies
c = cookies.SimpleCookie()
if cookie_str:
    # #加载cookie字符串
    c.load(cookie_str)
    print(c['username'].value)
    # print(c['age'].value)
print(123)





