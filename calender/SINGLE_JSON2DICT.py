import json

with open('mail.json', 'rt',encoding="utf-8") as open_file:
    context = open_file.read()
JSON_CONTEXT = json.loads(context.encode("utf-8"))
print(JSON_CONTEXT)
FROM = JSON_CONTEXT['FROM']
PASSWORD = JSON_CONTEXT['Q4SSW0RD']
SUBJECT = JSON_CONTEXT['SUBJECT']
TO = JSON_CONTEXT['TO']

print('发信人：{},\n密码：{},\n主题：{},\n收件人：{}'.format(FROM,PASSWORD,SUBJECT,TO))