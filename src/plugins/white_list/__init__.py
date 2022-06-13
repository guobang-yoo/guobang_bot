from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.plugin import export

export=export()

@export.auth
async def wuneigui(event:MessageEvent):
    white_groups=['237776131','1073903632']
    # white_user=['2250926180','2445456295']
    # white_list=white_groups+white_user
    white_list = white_groups
    session_id=event.get_session_id()
    event_name = event.get_event_name()
    if 'private.friend' in event_name:
        return True
    elif 'group' in event_name:
        for w in white_list:
            if w in session_id:
                return True
    return False