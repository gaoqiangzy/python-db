#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
import os
import cgitb
cgitb.enable()
print("Content-Type:text/html")
print("")
cookie_str=os.environ.get('HTTP_COOKIE')
# #创建一个simpleCookie对象
from http import cookies
c = cookies.SimpleCookie()
if cookie_str.__contains__('username'):
    c.load(cookie_str)
    print(f"{c['username'].value}")
else:
    print("username不存在")

