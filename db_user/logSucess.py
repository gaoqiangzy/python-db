#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
print("Content-Type:text/html;charset=gbk")
print("")
import os
import cgitb
cgitb.enable()
"""通过simpleCookie()
2.解析os.environ['HTTP_COOKIE']
"""
# print(os.environ)
# #从环境变量中获取cookie字符串
cookie_str=os.environ.get('HTTP_COOKIE')
# #创建一个simpleCookie对象
from http import cookies
c = cookies.SimpleCookie()
if cookie_str.__contains__('username'):
    # #加载cookie字符串
    c.load(cookie_str)
    html = f"""
                   <table>
                   <tr>
                       <td>欢迎:</td>
                       <td>{c['username'].value}</td>
                   </tr>
                   <tr>
                        <td><a href='test.py'>点击</a></td>
                   </tr>
               </table>
               """
    print(html)
else:
    print("cookie不存在")