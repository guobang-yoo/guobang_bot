from nonebot import on_command,rule
from nonebot.adapters.onebot.v11 import Event,Bot,Message
from .get_pic import get_pic
from nonebot.plugin import require

auth = require("white_list")
wuneigui=rule.Rule(auth['auth']['wuneigui'])
setu = on_command("setu",rule=wuneigui,aliases={'无内鬼', '涩图', '色图'})


@setu.handle()
async def _(bot:Bot,event:Event):
    message = str(event.get_message()).split(' ')
    # if 'setu' in message:
    #     message.remove('setu')
    # r18=0
    # if 'r18' in message:
    #     message.remove('r18')
    #     r18=1
    # keyword=message.pop()if len(message)>0 else ''
    r18,keyword=verify_message(message)
    pic_url = await get_pic(r18,keyword)
    try:
        if "i.pixiv.re" in pic_url:
            pic = "[CQ:image,file=" + pic_url + "]"
            await setu.send(message=Message(pic))
        else:
            await setu.send(message=Message(pic_url))
    except Exception as e:
        print(e)
        await setu.send(message=Message('可能是图太涩了，没发出去，自己去看'))
        await setu.send(message=pic_url)

def verify_message(message=[]):
    aliases={'无内鬼', '涩图', '色图'}
    r18=0
    for al in aliases:
        if al in message:
            return 0,''
    message.remove('setu')
    if 'r18' in message:
        message.remove('r18')
        r18=1
    keyword = message.pop() if len(message) > 0 else ''
    return r18,keyword


