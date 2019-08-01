#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
#↑解释器路由
#设置数据响应头
print("Content-Type:text/html")

"""
Set-Cookie:在响应头中，该字段就是用于设置cookie，发送给浏览器，当浏览器解析响应头的时候，如果有Set-Cookie字段
说明就是服务器要浏览器保存cookie，浏览器就会将cookie保存在浏览器的内存或硬盘
Set-Cookie：名称=值；Domain=域名；expires=过期时间；Path=cookie的路径
1.名称=值：
    唯一要求，必须为字符串
2.Domain=域名：
    默认不写域名，默认是当前访问域名
    写了域名字段，就使用定制的域名
    获取cookie只能获取自己域名下的cookie（不同父域名之间cookie不能共享）
    相同父域名下，cookie可以贡献
    工作设置域名时，将Domain=父域名
    eg:
        Domain=.baidu.com(设置父域名时，域名前最好加个.)
        在baidu。com父域名下设置的cookie，在子域名下内容是共享的，可以通过子域名访问获取cookie值
    
    父域名
        baidu.com
        qq.com
    子域名
        www.baidu.com
        news.baidu.com
        20018.baidu.com
"""
print("Set-Cookie:userName=zhangsan; Domain=localhost; expires=Tue, 25-Aug-2019 10:10:10 GMT; Path=/")
print("")
print("设置成功")













