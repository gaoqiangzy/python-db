#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑加载python解释器
#声明相应头
print("Content-Type:text/html;")
print("")


#导包
import pymysql
import cgi,cgitb
import Response
cgitb.enable()
data = cgi.FieldStorage()
username = data.getvalue('username')
password = data.getvalue("password")

#链接数据库
db = pymysql.connect(host="localhost",user="root",password="root",database="liuyanban",charset="utf8")
cursor = db.cursor()
sql = "insert into user(username,password) values (%s,%s)"
if username and password:
    try:
        rs = cursor.execute(sql,(username,password))
    except Exception as e:
        print("出错啦。。。")
        print(e)
        db.rollback()
    else:
        if rs>0: #注册成功
            Response.redirect("login.html","注册成功",3)
            db.commit()
            cursor.close()
            db.close()
        else:
            Response.redirect("register.html","注册失败",3)
else:
    Response.redirect("register.html", "请输入数据", 3)

