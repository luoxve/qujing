#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from models import Colored
import request, json

def resolveData():
    #查询链接
    #url = 'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2018-01-31&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=GZG&purpose_codes=ADULT'    #获取数据
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-02&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=XUN&purpose_codes=ADULT'
    stations2CN = {}
    while 1:
        try:
            # data = getData(url)
            data = request.getData(url)
            jdata = json.loads(data)
            lists = jdata["data"]["result"]
            stations2CN = jdata["data"]["map"]
            print(stations2CN["OYN"])
            break
        except:
            continue
    cont = []
    name = [
        "station_train_code",
        "from_station_name",
        'start_time',
        "lishi",
        "swz_num",
        "zy_num",
        "ze_num",
        "gr_num",
        "rw_num",
        "dw_num",
        "yw_num",
        "rz_num",
        "yz_num",
        "wz_num",
        "qt_num",
        "note_num"
    ]
    color = Colored()#创建Colored对象
    for items in lists:#遍历result的每一项
        #data字典用于存放每一车次的余票信息
        data = {
            "station_train_code": '',
            "from_station_name": '',
            "to_station_name": '',
            'start_time': '',
            'end': '',
            "lishi": '',
            "swz_num": '',
            "zy_num": '',
            "ze_num": '',
            "dw_num": '',
            "gr_num": '',
            "rw_num": '',
            "yw_num": '',
            "rz_num": '',
            "yz_num": '',
            "wz_num": '',
            "qt_num": '',
            "note_num": ''
        }
        item = items.split('|')#用"|"进行分割
        data['station_train_code'] = item[3]#车次在3号位置
        data['from_station_name'] = item[6]#始发站信息在6号位置
        data['to_station_name'] = item[7]#终点站信息在7号位置
        data['start_time'] = item[8]#出发时间信息在8号位置
        data['arrive_time'] = item[9]#抵达时间在9号位置
        data['lishi'] = item[10]#经历时间在10号位置
        data['swz_num'] = item[32] or item[25]# 特别注意：商务座在32或25位置
        data['zy_num'] = item[31]#一等座信息在31号位置
        data['ze_num'] = item[30]#二等座信息在30号位置
        data['gr_num'] = item[21]#高级软卧信息在31号位置
        data['rw_num'] = item[23]#软卧信息在23号位置
        data['dw_num'] = item[27]#动卧信息在27号位置
        data['yw_num'] = item[28]#硬卧信息在28号位置
        data['rz_num'] = item[24]#软座信息在24号位置
        data['yz_num'] = item[29]#硬座信息在29号位置
        data['wz_num'] = item[26]#无座信息在26号位置
        data['qt_num'] = item[22]#其他信息在22号位置
        if item[0] == 'null':
            data['note_num'] = item[1]
        else:
            data['note_num'] = color.white(item[1])#加高亮白色
            #如果没有信息则用“-”代替
        for pos in name:
            if data[pos] == '':
                data[pos] = '-'

        cont.append(data)
    tickets = []#存放所有车次的余票信息
    #格式化添加进tickets中
    for x in cont:
        tmp = []
        for y in name:
            if y == "from_station_name":
                s = color.green(stations2CN[x[y]]) + '\n' + color.red(stations2CN[x["to_station_name"]])#始发站绿色，终点站红色
                # s = color.green(x[y]) + '\n' + color.red(x["to_station_name"])  # 始发站绿色，终点站红色
                tmp.append(s)
            elif y == "start_time":
                s = color.green(x[y]) + '\n' + color.red(x["arrive_time"])
                tmp.append(s)
            elif y == "station_train_code":
                s = color.yellow(x[y])
                tmp.append(s)
            else:
                tmp.append(x[y])
        tickets.append(tmp)
    return tickets#返回所有车次余票信息