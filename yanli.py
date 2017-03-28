import logging
import pprint

import requests

from wxpy.ext.talk_bot_utils import get_context_user_id, get_text_without_at, next_topic
from wxpy.utils import enhance_connection

logger = logging.getLogger(__name__)


class YanLi(object):
    """
    展老师聊天机器人
    """
    #接收到聊天后，从公众号获取聊天内容，然后和公众号里面的小冰聊天，得到聊天结果后发送给当前用户。

    url = 'http://www.tuling123.com/openapi/api'

    def __init__(self):

        self.session = requests.Session()
        enhance_connection(self.session)

        # noinspection SpellCheckingInspection
        self.last_member = dict()

    def do_reply(self, msg):
        msg.forword()

