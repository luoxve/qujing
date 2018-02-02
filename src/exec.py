#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from prettytable import PrettyTable
import resolve
#显示查询结果
def display(tickets):
    ptable = PrettyTable('车次 出发/到达站 出发/到达时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他 备注'.split(' '))
    for ticket in tickets:
        ptable.add_row(ticket)
    print(ptable)

if __name__ == "__main__":#main方法
    tickets = resolve.resolveData()
    display(tickets)
    input('按任意键退出...')