import requests
import base64
import re

url="https://api.lolicon.app/setu/v2"

async def get_pic(r18=0,keyword=''):
    param={
        "r18":r18,
        "keyword":keyword,
        'proxy': 'i.pixiv.re'
    }
    print(param)
    try:
        response = requests.get(url,params=param)
        pic_url = response.json()['data'][0]['urls']['original']
        # base64_pic = await down_pic(pic_url)
        # pic = "[CQ:image,file=base64://" + base64_pic + "]"
        return pic_url
    except IndexError as e:
        return f'根据条件没找到图'
    except Exception as e:
        print(e)
        return f'请求太快了hxd'


async def down_pic(url):
    response = requests.get(url)
    if response:
        ba = str(base64.b64encode(response.content))
        pic = re.findall(r"\'([^\"]*)\'", ba)[0].replace("'", "")
        return  pic