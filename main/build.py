# _*_ coding:utf-8 _*_
from dingtalkchatbot.chatbot import DingtalkChatbot, CardItem, ActionCard

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=58a529717946cd7302b78808d62c622bc5817c4d7e8096d33a839ea4101c33be'
secret = 'SECb410b3519c1337382ea5f02dda485d47e143ee80446c98c65f5609ca0985c9bd'  # 可选：创建机器人勾选“加签”选项时使用
xiao_ding = DingtalkChatbot(webhook, secret=secret, pc_slide=False, fail_notice=False)


def start_build():
    btn = [CardItem(title="查看构建详情", url="https://www.dingtalk.com/")]
    action_card = ActionCard(title='开始构建',
                             text="**应用xxx开始构建**\n* 发起人：xxx\n* 开始时间：xxx\n* [提交详情：xxx](https://www.imooc.com/ '提交详情')",
                             btns=btn,
                             btn_orientation=1,
                             hide_avatar=1)
    xiao_ding.send_action_card(action_card)


def end_build():
    btn = [CardItem(title="查看构建详情", url="https://www.dingtalk.com/")]
    action_card = ActionCard(title='构建成功',
                             text="**应用xxx构建成功**\n* 构建时长：5分30秒\n* 构建人：xxx\n* 完成时间：xxx\n* [提交详情：xxx](https://www.imooc.com/ '提交详情')",
                             btns=btn,
                             btn_orientation=1,
                             hide_avatar=1)
    xiao_ding.send_action_card(action_card)


end_build()
