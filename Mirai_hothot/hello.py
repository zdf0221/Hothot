# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hello
   Description :
   Author :       zdf's desktop
   date：          2020/6/15
-------------------------------------------------
   Change Activity:
                   2020/6/15:02:48
-------------------------------------------------
"""

import asyncio
import os
from urllib import request

import requests
from bs4 import BeautifulSoup
from mirai import (
    Mirai, Depend,
    Plain, Face, Image,
    MessageChain,
    Friend, Group, Member, Source,
    At, MemberJoinEvent, BotJoinGroupEvent, BotMuteEvent, BotUnmuteEvent,
)
from mirai.face import QQFaces
from mirai.exceptions import *
from InfoLib import *

qq = 2715723655  # 字段 qq 的值
authKey = '543112018'  # 字段 authKey 的值
mirai_api_http_locate = '172.105.231.148'  # httpapi所在主机的地址端口,如果 setting.yml 文件里字段 "enableWebsocket" 的值为 "true" 则需要将 "/" 换成 "/ws", 否则将接收不到消息.

app = Mirai(host=mirai_api_http_locate, port=8070, authKey=authKey, qq=qq)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "",
    "Connection": "keep-alive",
}


async def preprocess_command(message: MessageChain):
    print(message)
    return message.toString()


"""
这里是私聊消息处理部分
"""


@app.receiver("FriendMessage")
async def event_fm(app: Mirai, friend: Friend, message: str = Depend(preprocess_command)):
    await app.sendFriendMessage(friend, [
        Plain(text=friend_respond)
    ])

"""
这里是WOD图书馆消息处理部分
"""

# @app.receiver("GroupMessage")
# 这个是基础的响应群聊的模板


async def event_gm(app: Mirai, group: Group, message: str = Depend(preprocess_command)):
    try:
        await app.sendGroupMessage(group.id, [
            Plain(text="响应群聊的消息")
        ])
    except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
        print("send group message error!")


@app.receiver("GroupMessage")
async def help(app: Mirai, group: Group, message: MessageChain):
    matches = ['.help', '.帮助', '.使用说明']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=Help_text
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send help message error!")


@app.receiver("GroupMessage")
async def mosaicist(app: Mirai, group: Group, message: MessageChain):
    matches = ['.mosaicist', '.镶嵌师', '.镶嵌师傅']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=Mosaicist_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send mosaicist message error!")


@app.receiver("GroupMessage")
async def mosaic(app: Mirai, group: Group, message: MessageChain):
    matches = ['.mosaic', '.镶嵌种类', '.镶嵌种族', '.镶嵌材料']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=Mosaic_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send mosaic message error!")


@app.receiver("GroupMessage")
async def mosaic_formula(app: Mirai, group: Group, message: MessageChain):
    matches = ['.mosaic_formula', '.镶嵌公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=mosaic_formula_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send mosaic_formula_info message error!")


@app.receiver("GroupMessage")
async def two_slots(app: Mirai, group: Group, message: MessageChain):
    matches = ['.2s', '.两孔镶嵌公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=two_slots_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send two_slots_info message error!")


@app.receiver("GroupMessage")
async def three_slots(app: Mirai, group: Group, message: MessageChain):
    matches = ['.3s', '.三孔镶嵌公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=three_slots_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send three_slots_info message error!")


@app.receiver("GroupMessage")
async def four_slots(app: Mirai, group: Group, message: MessageChain):
    matches = ['.4s', '.四孔镶嵌公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=four_slots_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send four_slots_info message error!")


@app.receiver("GroupMessage")
async def five_slots(app: Mirai, group: Group, message: MessageChain):
    matches = ['.5s', '.五孔镶嵌公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=five_slots_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send five_slots_info message error!")


@app.receiver("GroupMessage")
async def potion(app: Mirai, group: Group, message: MessageChain):
    matches = ['.potion', '.药剂']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=potion_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send potion message error!")


@app.receiver("GroupMessage")
async def holy_parade(app: Mirai, group: Group, message: MessageChain):
    matches = ['.songbook', '.神圣进军']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=holy_parade_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send holy_parade_info message error!")


@app.receiver("GroupMessage")
async def tune(app: Mirai, group: Group, message: MessageChain):
    matches = ['.tune', '.歌曲']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=tune_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send tune_info message error!")


@app.receiver("GroupMessage")
async def book(app: Mirai, group: Group, message: MessageChain):
    matches = ['.book', '.书籍']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=book_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send tunebook_info_info message error!")


@app.receiver("GroupMessage")
async def herb(app: Mirai, group: Group, message: MessageChain):
    matches = ['.herb', '.草药']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=herb_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send herb_info message error!")


@app.receiver("GroupMessage")
async def dodge(app: Mirai, group: Group, message: MessageChain):
    matches = ['.dodge', '.躲闪', '.躲闪公式']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=dodge_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send dodge_info message error!")


@app.receiver("GroupMessage")
async def scroll(app: Mirai, group: Group, message: MessageChain):
    matches = ['.scroll', '.卷轴', '.学者双卷']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=scroll_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send scroll_info message error!")


@app.receiver("GroupMessage")
async def gods_name(app: Mirai, group: Group, message: MessageChain):
    matches = ['.gods_name', '.神名']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=gods_name_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send gods_name_info message error!")


@app.receiver("GroupMessage")
async def blessing(app: Mirai, group: Group, message: MessageChain):
    matches = ['.blessing', '.祝福']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=blessing_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send blessing_info message error!")


@app.receiver("GroupMessage")
async def spicy(app: Mirai, group: Group, message: MessageChain):
    matches = ['.spicy', '.香料']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text=spicy_info
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send spicy_info message error!")


@app.receiver("GroupMessage")
async def item_search(app: Mirai, member: Member, group: Group, message: MessageChain):
    matches = ['.item', '.物品查询', '.装备查询', '.查询物品']
    if any(x in message.toString() for x in matches):
        try:
            item_name = message.toString()[5::]
            print(item_name)
            url = "http://canto.world-of-dungeons.org/wod/spiel/hero/item.php?name={}".format(item_name)
            req = requests.get(url, headers=headers, )
            html = req.content
            html = str(html, 'utf-8')  # Same as: html_doc=html.decode("utf-8","ignore")
            soup = BeautifulSoup(html, features='html5lib')

            item_name = str(soup.title.string)[5:-20:]  # strip title tag

            spec = soup.find(id='details')
            if not spec:
                await app.sendGroupMessage(group.id, [
                    At(target=member.id),
                    Plain("抱歉没有找到您说的这件装备，可能有如下原因："),
                    Plain("1: 装备名称输入错误（例如双引号，感叹号）"),
                    Plain("2: 装备内部包含非法字符（例如：& % ^ 等）"),
                ])
            detail = spec.text.replace(' ', '').strip()
            detail = detail.split("\t")
            detail = [c for c in detail if c]
            detail = [c for c in detail if c != '\n']
            detail = [c for c in detail if c != '\n\n']
            detail = [c for c in detail if c != '\n\n\n']
            detail = [c for c in detail if c != '\n\n\n\n']
            detail = [c for c in detail if c != '\n\n\n\n\n']
            detail = [c for c in detail if c != '\n\n\n\n\n\n']
            ans = []
            for s in detail:
                s = s.strip('\n')
                ans.append(s)
            detail = ans
            # print(detail)

            attribute = soup.find(id='link')
            attribute = attribute.text.replace(' ', '').strip()
            attribute = attribute.split("\t")
            attribute = [c for c in attribute if c]
            attribute = [c for c in attribute if c != '\n']
            attribute = [c for c in attribute if c != '\n\n']
            attribute = [c for c in attribute if c != '\n\n\n']
            attribute = [c for c in attribute if c != '\n\n\n\n']
            attribute = [c for c in attribute if c != '\n\n\n\n\n']
            attribute = [c for c in attribute if c != '\n\n\n\n\n\n']
            ans = []
            for s in attribute:
                s = s.replace('\n', ' ')
                ans.append(s)
            attribute = ans
            # print(attribute)

            ans = detail + attribute

            await app.sendGroupMessage(group.id, [
                At(target=member.id),
                Plain("这是您要查询的装备："),
                Plain(
                    text=" ".join(ans)
                )
            ])
        except (RuntimeError):

            print("send spicy_info message error!")



"""
这里是每日一句毒鸡汤功能
"""


@app.receiver("GroupMessage")
async def single_idiom(app: Mirai, group: Group, member: Member, message: MessageChain, source: Source):
    matches = ['毒鸡汤', '一言']
    if any(x in message.toString() for x in matches):
        try:
            import aiohttp
            async with aiohttp.request("GET", "https://v1.alapi.cn/api/soul") as req:
                data = await req.json()
                if data["code"] != 200:
                    raise ValueError("Status Error:" + str(data["code"] + ":" + data["msg"]))
                return await app.sendGroupMessage(group, [At(member.id), Plain(data["data"]["title"])],
                                                  quoteSource=source,
                                                  )
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send 毒鸡汤 message error!")


@app.receiver("GroupMessage")
async def single_chp(app: Mirai, group: Group, member: Member, message: MessageChain, source: Source):
    matches = ['彩虹屁', '夸我']
    if any(x in message.toString() for x in matches):
        try:
            import aiohttp
            async with aiohttp.request("GET", "https://chp.shadiao.app/api.php?lang=zh_cn") as req:
                data = await req.text()
                data = str(data)
                print(data)
                if not data:
                    raise ValueError("empty response Error!")
                return await app.sendGroupMessage(group, [At(member.id), Plain(data)],
                                                  quoteSource=source,
                                                  )
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send 毒鸡汤 message error!")


"""
这里是今日运势功能
"""


@app.receiver("GroupMessage")
async def rp(app: Mirai, group: Group, message: MessageChain):
    matches = ['.jrrp', '今日运势', '求签', '抽签']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Plain(
                    text="抱歉，我的主人最近偷懒，还没有写这个模块呢"
                )
            ])
        except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send jrrp message error!")


"""
这里是表情测试功能
"""


@app.receiver("GroupMessage")
async def face_fight(app: Mirai, group: Group, message: MessageChain):
    matches = ['.face', '发个表情']
    if any(x in message.toString() for x in matches):
        try:
            await app.sendGroupMessage(group.id, [
                Face(faceId=random.randint(0, 324))
            ])
        except (EnvironmentError, PermissionError, ConnectionRefusedError):
            print("send help message error!")


"""
这里是图片测试功能
"""


@app.receiver("GroupMessage")
async def daily_pic(app: Mirai, group: Group, member: Member, message: MessageChain):
    matches = ['.setu', '来张色图', '来份色图', '不够色', '就这？']
    if any(x in message.toString() for x in matches):
        ans = random.randint(0, 1)
        if ans:
            try:
                path = os.path.abspath(__file__)
                path = os.path.dirname(path)
                path = os.path.join(path, 'Tornado_webite_test')
                path = os.path.join(path, 'Pixiv')
                # print(path)
                pic_name = os.listdir(path)
                # print(pic_name)
                random_pic = os.path.join(path, random.choice(pic_name))
                await app.sendGroupMessage(group.id, [
                    At(target=member.id),
                    Image.fromFileSystem(random_pic),
                    Plain(text="这是您点的一份色图~")
                ])
            except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
                print("send setu message error!")
        else:
            await app.sendGroupMessage(group.id, [
                At(target=member.id),
                Plain(text="本烫不想理你"),
                Face(faceId=212),
            ])


"""
下面是群组功能区
"""


@app.receiver("MemberJoinEvent")
async def member_join(app: Mirai, event: MemberJoinEvent):
    await app.sendGroupMessage(
        event.member.group.id,
        [
            At(target=event.member.id),
            Plain(text="烫烫代表全体群员，欢迎您的到来~")
        ]
    )


@app.receiver("BotUnmuteEvent")
async def member_join(app: Mirai, event: BotUnmuteEvent):
    await app.sendGroupMessage(
        # todo...
        event.member.group.id,
        [
            At(target=event.operator[0]),
            Plain(text="是哪个人禁言我？出来")
        ]
    )


@app.receiver("BotJoinGroupEvent")
async def bot_join(app: Mirai, event: BotJoinGroupEvent):
    try:
        await app.sendGroupMessage(
            event.group.id,
            [
                Plain(text=bot_join_text)
            ]
        )
    except (RuntimeError, ValueError, EnvironmentError, PermissionError, ConnectionRefusedError):
        print("send bot join group message error!")


if __name__ == "__main__":
    app.run()
