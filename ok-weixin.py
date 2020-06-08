#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2018-04-20
# comment: zabbix接入微信报警脚本

import requests
import sys
import os
import json
import logging

# logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s, %(filename)s, %(levelname)s, %(message)s',datefmt = '%a, %d %b %Y %H:%M:%S',filename = os.path.join('/data/zabbix','weixin.log'),filemode = 'a')
corpid = 'wwa211a8c23f5f7f08'  # 企业ID
appsecret = 'MtOt1bWi11fg_Pbnn-tcmWC5BlZ_mJfk8hLiKN02FJY'  # secret
agentid = 1000003  # AgentID
# 获取accesstoken
token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
req = requests.get(token_url)
accesstoken = req.json()['access_token']

# 发送消息
msgsend_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken

touser = sys.argv[1]
subject = sys.argv[2]
# toparty='3|4|5|6'
message = sys.argv[3]

params = {
    "touser": touser,
    #       "toparty": toparty,
    "msgtype": "text",
    "agentid": agentid,
    "text": {
        "content": message
    },
    "safe": 0
}

req = requests.post(msgsend_url, data=json.dumps(params))

logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message)
