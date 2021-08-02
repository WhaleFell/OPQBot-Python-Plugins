#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-21 23:23:10
LastEditTime: 2021-08-02 20:52:43
Description: OPQBot 机器人框架
'''
from re import A
from botoy import Botoy, Action, GroupMsg
from botoy import decorators as deco
from botoy import jconfig
import botoy
from botoy.model import EventMsg
# from botoy import refine
from botoy.parser import group as gp  # 群消息(GroupMsg)相关解析
from botoy.parser import friend as fp  # 好友消息(FriendMsg)相关解析
from botoy.parser import event as ep  # 事件(EevntMsg)相关解析
from botoy import Action
from botoy.sugar import S

bot = Botoy(qq=2593923636, host=jconfig.host, port=jconfig.port)
action = Action(qq=2593923636, host=jconfig.host, port=jconfig.port)


@bot.on_group_msg
def group(ctx: GroupMsg):
    # 打印图片信息每张图片的地址
    # print('收到群消息，群号为', ctx.FromGroupId)
    pic_urls = gp.pic(ctx)
    if pic_urls is not None:
        for pic_url in pic_urls.GroupPic:
            print(pic_url.Url)

    at_data = gp.at(ctx)
    if at_data is not None:
        if ctx.CurrentQQ in at_data.UserID:
            print(f"念曦现在被{ctx.FromNickName}AT了,他说:{at_data.Content}")


# 监控撤回信息
@bot.on_event
def group(ctx: EventMsg):

    revoke_data = ep.group_revoke(ctx)
    print(revoke_data.MsgSeq)


@bot.on_group_msg
@deco.ignore_botself()  # 忽略机器人本身信息
@deco.equal_content("test")
def group_(ctx: GroupMsg):
    print("ok发送信息", ctx.FromGroupId)
    # 发送群信息
    S.text(f"{ctx.FromNickName},我喜欢你!", at=ctx.FromUserId)


if __name__ == '__main__':
    action.getGroupList()
    bot.run()
