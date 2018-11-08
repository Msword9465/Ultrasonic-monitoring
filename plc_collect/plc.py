# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import snap7
import struct
import numpy as np
from snap7.snap7types import *

ip = '192.168.1.99'  # PLC的ip地址
rack = 0  # 机架号
slot = 1  # 插槽号
tcpport = 102  # TCP端口号

# 建立连接

def get_plc(db_num=3,num=13):
    client = snap7.client.Client()
    client.connect(ip, rack, slot, tcpport)
    reading = client.db_read(db_number=db_num, start=0, size=2*num)
    client.read_area(area['Mk'], 3, 0, 26)
    data_get = np.array(struct.unpack('!' + 'h'*num,  reading))
    client.disconnect()
    client.destroy()
    print(data_get)

def set_plc():
    client = snap7.client.Client()
    client.connect(ip, rack, slot, tcpport)
    reading = struct.pack('!' + 'h'*3, 50, 50, 50)
    client.db_write( 3, 0 ,reading)     
    client.destroy()
    
get_plc()
set_plc()
get_plc()
#

