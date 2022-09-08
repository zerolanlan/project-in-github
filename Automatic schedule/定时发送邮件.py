"""
功能：每天晚上8点给第二天上班的人员发送邮件通知
备注：邮箱的服务器、端口、收发件人端口需要配置，Exchange的邮箱暂时还不清楚怎么做- -
"""
import datetime
import threading
from email.mime.text import MIMEText
import smtplib

def autoemail():
    mail_host = "smtp.XXXX.XX"                       #输入SMTP服务器
    sslPort = "25"                                   #邮箱端口
    user_name = "77"                                 #登录用户名
    user_password = "密码"                           #邮箱密码
    sender_add = "XXXX@XXXX"                         #发件人地址
    reciver_add = "XXXX@XXXX"                        #收件人地址，可以是多人
    mail_title = "e-mail title"                      #设置邮件标题
    massage = r"邮件内容"

    msg = MIMEText(massage, 'html', 'utf-8')
    msg['From'] = sender_add
    msg['To'] = ','.join(reciver_add)
    msg['Subject'] = mail_title

    server = smtplib.SMTP(mail_host, sslPort)
    server.login(user_name, user_password)           #也有可能用邮箱地址
    server.sendmail(sender_add, reciver_add, msg.as_string())
    server.quit()
    print("邮件已发送成功！")

    #迭代循环计时器
    timer = threading.Timer(86400, autoemail())
    timer.start()

#主函数，含初始化
if __name__== "__main__":
    # 获取现在时间
    now_time = datetime.datetime.now()
    #当前时间是今天的多少秒
    t_now = int(now_time.hour) * 3600 + int(now_time.minute) * 60 + int(now_time.second)
    #晚8点是今天的多少秒,为了符合晚8点发送的要求
    t_twenty = 20 * 3600
    if now_time.hour >= 20:
        timer_start_time = 86400 - t_now + 86400
    elif now_time.hour < 20:
        timer_start_time = t_twenty - t_now
    #程序启动
    timer = threading.Timer(timer_start_time, autoemail())
    timer.start()