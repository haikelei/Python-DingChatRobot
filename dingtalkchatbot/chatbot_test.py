#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 16/01/2018 14:37
import unittest

from dingtalkchatbot.chatbot import DingtalkChatbot, is_not_null_and_blank_str, ActionCard, FeedLink, CardItem

__author__ = 'Devin -- http://zhangchuzhao.site'


class TestDingtalkChatbot(unittest.TestCase):
    """DingtalkChatbot 测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=58a529717946cd7302b78808d62c622bc5817c4d7e8096d33a839ea4101c33be'
        cls.secret = 'SECb410b3519c1337382ea5f02dda485d47e143ee80446c98c65f5609ca0985c9bd'  # 可选：创建机器人勾选“加签”选项时使用
        cls.xiaoding = DingtalkChatbot(cls.webhook, cls.secret)

    def test_is_not_null_and_blank_str(self):
        """测试字符串不为空函数"""
        self.assertFalse(is_not_null_and_blank_str(''), 'pass')
        self.assertFalse(is_not_null_and_blank_str(' '), 'pass')
        self.assertFalse(is_not_null_and_blank_str('   '), 'pass')
        self.assertTrue(is_not_null_and_blank_str('abc'), 'pass')
        self.assertTrue(is_not_null_and_blank_str('123'), 'pass')

    def test_send_text(self):
        """测试发送文本消息函数"""
        result = self.xiaoding.send_text(msg='测试的消息，不要理我！', is_at_all=True)
        self.assertEqual(result['errcode'], 0)

    def test_send_image(self):
        """测试发送表情图片消息函数"""
        result = self.xiaoding.send_image(pic_url='http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png')
        self.assertEqual(result['errcode'], 0)

    def test_send_link(self):
        """测试发送链接消息函数"""
        result = self.xiaoding.send_link(title='万万没想到，某小璐竟然...', text='故事是这样子的...',
                                         message_url='http://www.kwongwah.com.my/?p=454748',
                                         pic_url='https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')
        self.assertEqual(result['errcode'], 0)

    def test_send_markdown(self):
        """测试发送Markdown格式消息函数"""
        result = self.xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                                                                    '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                                                                    '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                                                                    '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                                             is_at_all=True)
        self.assertEqual(result['errcode'], 0)

    def test_send_actioncard(self):
        """测试发送整体跳转ActionCard消息功能（CardItem新API)"""
        btns1 = [CardItem(title="查看详情", url="https://www.dingtalk.com/")]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard1)
        self.assertEqual(result['errcode'], 0)

        """测试发送单独跳转ActionCard消息功能"""
        btns2 = [CardItem(title="支持", url="https://www.dingtalk.com/"),
                 CardItem(title="反对", url="http://www.back china.com/news/2018/01/11/537468.html")]
        actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard2)
        self.assertEqual(result['errcode'], 0)

    def test_send_actioncard_old_api(self):
        """测试发送整体跳转ActionCard消息功能（数据列表btns旧API)"""
        btns1 = [{"title": "查看详情", "actionURL": "https://www.dingtalk.com/"}]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard1)
        self.assertEqual(result['errcode'], 0)

        """测试发送单独跳转ActionCard消息功能"""
        btns2 = [{"title": "支持", "actionURL": "https://www.dingtalk.com/"},
                 {"title": "反对", "actionURL": "http://www.back china.com/news/2018/01/11/537468.html"}]
        actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard2)
        self.assertEqual(result['errcode'], 0)

    def test_send_feedcard(self):
        """测试发送FeedCard类型消息功能（CardItem新API)"""
        carditem1 = CardItem(title="氧气美女", url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        carditem2 = CardItem(title="氧眼美女", url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        carditem3 = CardItem(title="氧神美女", url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        cards = [carditem1, carditem2, carditem3]
        result = self.xiaoding.send_feed_card(cards)
        self.assertEqual(result['errcode'], 0)

    def test_send_feedcard_old_api(self):
        """测试发送FeedCard类型消息功能(FeedLink旧API)"""
        feedlink1 = FeedLink(title="氧气美女", message_url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        feedlink2 = FeedLink(title="氧眼美女", message_url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        feedlink3 = FeedLink(title="氧神美女", message_url="https://www.dingtalk.com/",
                             pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
        links = [feedlink1, feedlink2, feedlink3]
        result = self.xiaoding.send_feed_card(links)
        self.assertEqual(result['errcode'], 0)


if __name__ == '__main__':
    unittest.main()
