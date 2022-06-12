from nonebot import on_keyword
from nonebot.adapters.onebot.v11.message import Message

hello = on_keyword(["hello"])

@hello.handle()
async def hello_handle():
    await hello.finish(Message(f'Hello World!'))