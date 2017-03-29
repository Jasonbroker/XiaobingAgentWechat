from wxpy import *

# bot = Bot()
# my_friend = bot.friends().search('李旭')[0]
# my_friend.send('您的机器人已经上线咯~')
# my_friend.send_image('pic.jpg')
#
# limiao = bot.friends().search('礼苗')[0]
# limiao.send('机器人已经上线咯~')
# limiao.send_image('pic.jpg')

# tuling = Tuling(api_key='42824c30e972429f9ec99028bf71f1ce')

# @bot.register(my_friend)
# def reply_my_friend(msg):
#     tuling.do_reply(msg)
#
#
# @bot.register(limiao)
# def reply_my_friend(msg):
#     tuling.do_reply(msg)

############################ xiaobing robot ##############################
# 小冰机器人

bot = Bot(cache_path='./cache')
xiao_bing = bot.mps().search('小冰')[0]

my_friend = bot.friends().search('李旭')[0]

my_friend.send('Hi~MC小萌旭 (●ﾟωﾟ●)')


@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Text':
        text = msg.text
        print(msg.raw.get('User').get('NickName') + text)
        if text.find('展') >= 0:
            text = '周正昌公告：对我的女神一切信息暂时屏蔽'
            my_friend.send(text)
        elif text.lower().find('goodbye') >= 0:
            my_friend.send('机器人将自动退出，👋')
            bot.stop()
        elif text.find('李旭') >= 0:
            my_friend.send('我造你是小萌旭')
        elif text.find('我是') >= 0:
            my_friend.send('我不关心你是谁')
        else:
            xiao_bing.send(text)
    else:
        msg.forward(xiao_bing)


@bot.register(xiao_bing)
def replay_xiao_bing(msg):
    # msg.forword(my_friend, prefix="xiaobingsay")
    print(msg.type)
    if msg.type == 'Text':
        my_friend.send(msg.text)
    elif msg.type == 'Picture':
        my_friend.send_image(path=msg)
    else:
        my_friend.send('我想发语音的，氮素周正昌暂时没研究明白怎么发图片和语音，你等等他啊')


bot.join()
