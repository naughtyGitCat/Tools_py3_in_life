# target:get date
#         judge the date,case is a festival,send a blessing
#         if not sleep until the next festival
#


# 思路：先将JSON中的所有日期，取出来作为列表用作In查询
#         若In则根据这个值去查出对应的节日名称，是否发送祝福语

import datetime
import json
today = datetime.datetime.today()
print('今日日期：',today)

# 读取JSON文件，并转换成JSON格式模块
def json_context():
    with open("calender.json","rt",encoding="utf-8") as json_file:
        json_context=json_file.read()
        # print(json_context)
    JSON_list = json.loads(json_context)  # 这里的JSON_LIST是list格式
    # 检查读取出来的文件内容
    # print('line 22',JSON_list)
    # 检查读取出来的内容格式
    # print('line 23',type(JSON_list))
    return JSON_list
#####################################

#把list中的所有日期取出变成列表
def getDate2list(JSON_list):
    total_list = []
    for i in range(len(JSON_list)):
        # 调试内循环
        # print(i)
        single_dict = dict(JSON_list[i])
        date_list = single_dict['date']
        total_list.append(date_list)
        #调试日期列表正确性
        #print('line 34',total_list)
    return total_list
###########################

# #把list中的所有信息分割取出
# def splitFestival():


if __name__ == 'main' :
    JSON_list=json_context()
    getDate2list(JSON_list)