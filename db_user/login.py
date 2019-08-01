#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
# print("Content-Type:text/html")
# print("")
import cgi,cgitb
import response
cgitb.enable()
form = cgi.FieldStorage()
userName = form.getvalue("username")
password = form.getvalue("password")
import pymysql
db = pymysql.connect(host="localhost",user="root",password="root",database="test",charset="utf8")
cur = db.cursor()
sql = "select * from user where userName=%s and password=%s"
try:
    cur.execute(sql,(userName,password))
except Exception as e:
    print(e)
else:
    users = cur.fetchall()
    if users:#登陆成功
        # 设置数据响应头
        print("Content-Type:text/html;")
        """通过simpleCookie()
        1.生成cookie头的字符串
        2.解析os.environ['HTTP_COOKIE']
        """
        from http import cookies
        c = cookies.SimpleCookie()
        # cookie的名和值
        c['username'] = "lisi"
        # c['username']['path'] = "/"
        # import datetime
        # expires = datetime.datetime.now() + datetime.timedelta(days=1)
        # expires = expires.strftime("%a,%d-%b-%Y %H:%M:%S")
        # c['username']['expires'] = expires
        # c['username']['domain'] = 'localhost'
        # c['username']['max-age'] = 24 * 3600
        # c['age'] = 21
        print(c.output())
        print("")
        response.redirect("logSucess.py")
    else:
        print("Content-Type:text/html")
        print("")
        response.redirect("login.html","密码错误，请从新登陆",3)











