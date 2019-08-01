#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑加载python解释器
import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")
#声明相应头
print("Content-Type:text/html;")
print("")

import cgi,cgitb
import pymysql
import Response
cgitb.enable()
data = cgi.FieldStorage()
username = data.getvalue("username")
password = data.getvalue("password")

db = pymysql.connect(host="localhost",user="root",password="root",database="liuyanban",charset="utf8")
cursor = db.cursor()
sql_user = "select * from user where username=%s and password = %s"

if username and password:
    try:
        cursor.execute(sql_user,(username,password))
    except Exception as e:
        print(e)
        print("出错了。。。")
        db.rollback()
    else:
        rs = cursor.fetchall()
        if rs:
            sql_msg = "select * from message where parent_id=0"
            # sql_msg = "SELECT * FROM message JOIN USER ON message.`uid`=user.`uid` where parent_id=0"
            try:
                cursor.execute(sql_msg)
            except Exception as e:
                print(e)
            else:
                msgs = cursor.fetchall()
                if msgs:
                    content = """
                                        <link rel="stylesheet" href="css/index.css" type="text/css">
                                    """
                    content += f"""
                                    <div id="wrap">
                                        <div id="welcome">欢迎光临</div>
                                        <div id="user">欢迎：{username}</div>
                                        <form action="addMsg.py" method="post">
                                            <div id="leaveAMsg">
                                                <input type="hidden" name="uid" value="{rs[0][0]}">
                                                <textarea id="area2Msg" name="textarea_msg"></textarea>
                                                <button type="submit" >留言</button>
                                            </div>
                                        </form>
                                        <div id="msgs">
                                            <ul>
                                        """
                    for msg in msgs:
                        content += f"<li><p><span>{msg[0]}</span><span id='msg_time'>{msg[2]}</span></p>"
                        content += f"<a href='#'><p>{msg[1]}</p></a>"
                        content += "</li><hr>"

                    content += """

                                            </ul>
                                        </div>
                                    </div>

                                """

                    print(content)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    print("暂无留言")

            # Response.redirect("test.html", "登陆成功", 3)



        else:
            Response.redirect("login.html","密码错误",3)
else:
    Response.redirect("login.html","请输入数据",3)