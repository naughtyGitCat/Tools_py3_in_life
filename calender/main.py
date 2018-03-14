import time
from calender import getDate2list,json_context
from send_mail import send_mail



while True:
    # 取日期的月日
    now_time = time.localtime()
    today_date = time.strftime('%m%d',time.localtime())
    # print(time.strftime('%Y %m %d %H %M %S',time.localtime()))
    # 检查今天的月日获取正确性
    # print(today_date)

    JSON_list=json_context()
    fest_date=getDate2list(JSON_list)

    # 调试节日日期列表
    # print('节日日期：',fest_date)

    if today_date in fest_date:
        print('今天在节日日期中')
        for x in JSON_list:
            if today_date==x['date']:
                fest=x['festival']
                flag=x['send']
                print('节日：',fest+'\n','是否发送祝福：',flag)
                if flag == 'no':
                    print('今天的节日：',fest)
                else:
                    print('将通过邮件发送祝福')
                    send_mail('亲爱的xx：\n'+'今天是'+fest+'\n 祝你节日快乐')
                    break

    else:
        print('今天不在节日日期中')

