# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:43:53 2018
比较计算的声参数
@author: SCUTYJ
"""
import pymysql
import pandas as pd 
import numpy as np
import sklearn 
import matplotlib.pyplot as plt

#从数据库读取
def takeout_waveband(sql_id):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='2064', db='ultrasound', charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)   
        sql_select = "SELECT ID,波段1,波段2,波段3,波段4,波段5,波段6 FROM hisdata WHERE ID = {}".format(sql_id)
        cur.execute(sql_select)
        waveband_dict = cur.fetchone()
        waveband_dict.pop('ID')
        cur.close()
        conn.close()    
    except:
        waveband_dict = {}
        print('数据出现错误')
    return waveband_dict
    

def sound_parameters(waveband_dict):
    highest_Xpoints = [] 
    highest_Ypoints = [] 
    lowest_Xpoints = []
    lowest_Ypoints = []
    for num,waveband in waveband_dict.items():
        #从小到大排列
        waveband_num = pd.read_json(waveband,typ = 'Series').sort_values()
        lowest_Xpoints.append(waveband_num.index[0])
        lowest_Ypoints.append(waveband_num.values[0])
        highest_Xpoints.append(waveband_num.index[-1])
        highest_Ypoints.append(waveband_num.values[-1])
    return [highest_Xpoints,highest_Ypoints,lowest_Xpoints,lowest_Ypoints]                          
        
def sound_parameters_tosql(waveband):
    
    
