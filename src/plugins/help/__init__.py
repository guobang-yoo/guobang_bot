from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event,Bot,Message

help=on_command("help")

@help.handle()
async def _():
    await help.send(message=Message('''菜单
ps:指令额外参数使用空格分隔
1.发送 [<setu>|r18|关键词] 随机色图;
2.发送 [今日素材|武器|天赋] 查看今日武器材料和天赋树'''))