
def redirect(url,msg=None,time=0):
    html ="<div >提示信息</div>"
    html +=f"<div id='msg' style='color:red;'>{msg}</div>"
    html += "<div id='errormsg'>提示信息</div>"
    html += """
        <script>
        """
    html +=f" var times = {time};"
    html +="if(times==0){"
    html +=f"       window.location.href='{url}';"
    html +="}"

    html +="""  window.setInterval(function(){
                times--;
                document.getElementById('msg').innerHTML=times+"S后从新登陆";
                if(times==0){
            """
    html +=f"       window.location.href='{url}';"
    html +="""
                }
            },1000)
        </script>
    """
    print(html)