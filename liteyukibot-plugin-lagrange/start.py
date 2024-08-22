# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/22 下午8:54
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : start.py
@Software: PyCharm
"""
import threading

from lagrange import Lagrange
from lagrange.client.events.group import GroupMessage
from functools import partial
from lagrange.client.events.friend import FriendMessage
from lagrange.client.client import Client
from lagrange.client.message.elems import Text
from liteyuki.comm.storage import shared_memory
from liteyuki.message.event import MessageEvent

lgr = Lagrange(sign_url="https://sign.lagrangecore.org/api/sign/25765", uin=0)


def launch():
    threading.Thread(target=lgr.launch).start()
    pass


uin_to_uid: dict[str, str] = {}


def get_uid_from_uin(uin: str):
    return uin_to_uid.get(uin, None)


def get_uin_from_uid(uid: str):
    for k, v in uin_to_uid.items():
        if v == uid:
            return k
    return None


@partial(lgr.subscribe, GroupMessage)
async def group_message_handler(client: Client, event: GroupMessage):
    # do something
    lme = MessageEvent(
        bot_id=str(client.uin),
        raw_message=event.msg,
        message=event.msg,
        message_type="group",
        session_id=str(event.grp_id),
        session_type="group",
        receive_channel="event_to_lagrange",
        data={}
    )
    shared_memory.publish("event_to_liteyuki", lme)


@partial(lgr.subscribe, FriendMessage)
async def friend_message_handler(client: Client, event: FriendMessage):

    lme = MessageEvent(
        bot_id=str(client.uin),
        raw_message=event.msg,
        message=event.msg,
        message_type="private",
        session_id=str(event.from_uid),
        session_type="private",
        receive_channel="event_to_lagrange",
        data={}
    )
    shared_memory.publish("event_to_liteyuki", lme)


@shared_memory.on_subscriber_receive("event_to_lagrange")
async def _(event: MessageEvent):
    client = lgr.client
    if event.message_type == "private":
        await client.send_friend_msg([Text(event.message)], event.session_id)
    else:
        await client.send_grp_msg([Text(event.message)], int(event.session_id))
