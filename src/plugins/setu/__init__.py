from nonebot import on_command,on_keyword,rule
from nonebot.adapters.onebot.v11 import Event,Bot,Message
from .get_pic import get_pic
from nonebot.plugin import require
from nonebot.exception import ActionFailed

auth = require("white_list")
wuneigui=rule.Rule(auth['auth']['wuneigui'])

setu = on_command("setu",rule=wuneigui)
kw = on_keyword(set(['无内鬼','色图','涩图']),rule=wuneigui)

@kw.handle()
@setu.handle()
async def _(bot:Bot,event:Event):
    message = str(event.get_message())
    r18,keyword=verify_message(message)
    pic_url = await get_pic(r18,keyword)
    try:
        if "i.pixiv.re" in pic_url:
            pic = "[CQ:image,file=" + pic_url + "]"
            await setu.send(message=Message(pic))
        else:
            await setu.send(message=Message(pic_url))
    except ActionFailed as e:
        await setu.send(message=Message('可能是图太涩了，没发出去，自己去看'))
        await setu.send(message=pic_url)
    except Exception as e:
        await setu.send(message=Message('坏了，出毛病了'))


def verify_message(message=''):
    aliases={'无内鬼', '涩图', '色图'}
    r18=0
    #aliases判断关键字
    for al in aliases:
        if al in message:
            return 0, ''
    message = message.replace('setu','').split(' ')
    # 如果只有一个setu，直接返回
    if len(message) == 1:
        return 0, ''
    # r18参数
    if 'r18' in message:
        message.remove('r18')
        r18=1
    # 获取keyword
    keyword = message.pop() if len(message) > 0 else ''
    return r18,keyword


