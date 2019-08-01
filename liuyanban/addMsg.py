#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑加载python解释器
#声明相应头
print("Content-Type:text/html;")
print("")
import cgi,cgitb
import pymysql
import time
import Response
data = cgi.FieldStorage()
uid = data.getvalue("uid")
textarea_msg = data.getvalue("textarea_msg")
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
db = pymysql.connect(host="localhost",user="root",password="root",database="liuyanban",charset="utf8")
cursor = db.cursor()
# queryUser = "select * from user where uid =%s" #根据uid查询用户
addMsg = "insert into message(content,time,uid) values (%s,%s,%s)" #得到前台数据添加数据
print(textarea_msg)
print(nowtime)
if uid and textarea_msg:
    try:
       rs = cursor.execute(addMsg,(textarea_msg,nowtime,uid))
    except Exception as e:
        print(e)
        print("出什么问题了呢？？？")
        db.rollback()
    else:

        if rs :
            # print("留言成功")
            Response.redirect("log.py","留言成功",3)
            db.commit()
            cursor.close()
            db.close()
        else:
            print("留言失败")
else:
    print("请输入数据")
