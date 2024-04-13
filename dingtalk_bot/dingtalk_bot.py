from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import  datetime

# 读取上一次的值
with open('index.txt', 'r') as file:
    index = int(file.read())
    print("index:",index)

# 部门列表
department_list=["行政部","信息部","编辑部","网评部"]
# 生成内容
content = f"""
            '**今天是星期{datetime.now().strftime("%A")}**\n'
            '**请各位同学注意今天的工作安排**\n\n'
            '由{department_list[index]}负责打扫卫生\n\n'
            '发送时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
"""
print(content)
def dingtalk_robot(webhook,secret):
    remindrobot = DingtalkChatbot(webhook, secret)
    remindrobot.send_markdown(
        title = f'###来自管理员的提醒',
        text = content,
        is_at_all=False)

# 保存下一次的值   
index = index + 1
if index == 4:
        index = 0
with open('index.txt', 'w') as file:
    file.write(str(index))

# 定义钉钉机器人的webhook参数
webhook = ''
secrets = ''

# 调用函数
dingtalk_robot(webhook=webhook, secret=secrets)
