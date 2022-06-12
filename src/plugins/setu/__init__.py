import re
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event,Bot,Message
from .get_pic import get_pic

async def wuneigui(event:Event):
    white_groups=['237776131','1073903632']
    white_user=['2250926180','2445456295']
    session_id=event.get_session_id()
    if 'group' in session_id:
        for w in white_groups:
            if w in session_id:
                return True
    else:
        if session_id in white_user:
            return True
    return False


setu = on_command("setu",rule=wuneigui,aliases={'无内鬼', '涩图', '色图'})

@setu.handle()
async def _(bot:Bot,event:Event):
    message = str(event.get_message()).split(' ')
    message.remove('setu')
    r18=0
    if 'r18' in message:
        message.remove('r18')
        r18=1
    keyword=message.pop()if len(message)>0 else ''
    pic_url = await get_pic(r18,keyword)
    try:
        pic = "[CQ:image,file=" + pic_url + "]"
        await setu.send(message=Message(pic))
    except Exception as e:
        print(e)
        await setu.send(message=Message('可能是图太涩了，没发出去，自己去看'))
        await setu.send(message=pic_url)
        print(pic)

