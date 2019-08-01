#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑加载python解释器
#声明相应头
print("Content-Type:text/json;")
print("")
import cgi
import cgitb
cgitb.enable()

# form = cgi.FieldStorage()
# msg = form.getvalue("msg")
# print(123)
# print(msg)




# import time
# print(type(time.localtime()))
# print(type(time.time()))
# print(type(time.gmtime()))
# print(type(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
import pymysql
import json
db = pymysql.connect(host="localhost",user="root",password="root",database="liuyanban",charset="utf8")
cur = db.cursor()
sql = "select * from message"
rs = cur.execute(sql)
print(rs)
msgs = cur.fetchall()
print(msgs)
for m in msgs:
    print(m)