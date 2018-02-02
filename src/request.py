#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import requests

def getData(url):
    # url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-02&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=XUN&purpose_codes=ADULT'
    r = requests.get(url)
    return r.text