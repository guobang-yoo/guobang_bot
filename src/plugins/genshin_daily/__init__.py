from nonebot import on_command,on_keyword,rule
from nonebot.adapters.onebot.v11 import Message,MessageEvent
from configs.path_config import GENSHIN_IMAGE
from nonebot.plugin import require

from datetime import datetime

IMAGE_PATH = GENSHIN_IMAGE + "/material"

auth = require("white_list")
wuneigui=rule.Rule(auth['auth']['wuneigui'])

wqtf = on_keyword(['天赋','武器'])
material = on_command("今日素材", aliases={"今日材料", "今天素材", "今天材料"},rule=wuneigui)

@wqtf.handle()
@material.handle()
async def _(event:MessageEvent):
    week = datetime.today().weekday()+1
    if week == 7:
        await material.send("今天是周日，所有材料副本都开放了。")
        return
    file_path = str(IMAGE_PATH) + "/zhou"+ str(week) +".png"
    # print(file_path)
    msg=f'[CQ:image,file=file:///{file_path}]'
    await material.send(message=Message(msg))