#WINDOWS 3.6
import smtplib
import string,json

HOST = 'smtp.163.com'
SUBJECT = '节日祝福'
TO = '1775176461@163.com'
FROM = '177@163.com'
# TEXT = '测试节日祝福正文'
# TEXT = 'test'
# 读取预置的祝福语
# with open('zjy_gbk.txt', 'rt') as open_file:
#     context = open_file.read()

# 读取预置的邮件参数
with open('mail.json', 'rt',encoding="utf-8") as open_file:
    context = open_file.read()
JSON_CONTEXT = json.loads(context.encode("utf-8"))
# 检验读出的信息是否正确
# print(JSON_CONTEXT)
# 摘取信息
FROM = JSON_CONTEXT['FROM']
Q4SSW0RD = JSON_CONTEXT['Q4SSW0RD']
SUBJECT = JSON_CONTEXT['SUBJECT']
TO = JSON_CONTEXT['TO']

def send_mail(TEXT):
    BODY = "\r\n".join(["From:%s" % FROM,
                        "To:%s" % TO,
                        "Subject:%s" % SUBJECT,
                        "",
                        TEXT])


    #sendmail只能发送ASCII码
    #防止出现无法转换成ASCII码的报错问题，进行编码转换
    BODY =BODY.encode('utf-8')

    server = smtplib.SMTP()
    #不输出调试信息
    #server.set_debuglevel(1)
    server.connect(HOST, "25")
    #不启用TTLS加密
    #server.starttls()
    server.login(FROM, Q4SSW0RD)
    server.sendmail(FROM, [TO], BODY)
    server.quit()
    #print(BODY)

# 单独执行时，会执行下面的语句
if __name__ == 'main':
    send_mail('happy')