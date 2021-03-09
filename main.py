
import requests,time
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
 
 
 
 
# 获取cookie的方法，最好是隐身模式登陆，然后控制台输入document.cookie
cookie = '*************************************************************'
 
def sign():
    headers = {
        'Referer': 'https://film.qq.com/x/autovue/grade/',
        'User-Agent': 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'cookie': cookie
    }
    sign_url = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385'
    sign_response = requests.get(sign_url, headers=headers)
    sign_text = sign_response.text
    return sign_text
 
def sendEmail(receiver,title,content):
    host_server = 'smtp.qq.com'
    sender_qq = '811593937'
    sender = sender_qq + '@qq.com'
    # 这里要用授权码
    pwd = '************'  
 
    mail_content = content
    mail_title = title
 
    smtp = SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
 
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = receiver
    smtp.sendmail(sender, receiver, msg.as_string())
 
    print('邮件发送完毕...')
    smtp.quit()
 
 
def main():
    sign_text = sign()
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    qq = cookie[cookie.index('uin=o')+5:cookie.index('skey')-2]
    logs = local_time+'\t  '+qq+'\t  '+sign_text +'\r\n'
    print(logs)
 
    sendEmail('1361786108@qq.com', '腾讯视频VIP自动签到反馈', logs)
 
 
main()
