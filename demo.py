#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-21 23:23:10
LastEditTime: 2021-07-21 23:37:42
Description: OPQBot 机器人框架
'''
from botoy import Botoy, GroupMsg
from botoy import jconfig

bot = Botoy(qq="2593923636", host=jconfig.host, port=jconfig.port)


@bot.on_group_msg
def group(ctx: GroupMsg):
    print('收到群消息，群号为', ctx.FromGroupId)


if __name__ == '__main__':
    bot.run()
