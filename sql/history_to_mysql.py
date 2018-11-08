# coding: utf-8
'''
将数据写入mysql数据库
'''

import pymysql
import pandas as pd
import os
import time
start = time.clock()
#自增字段重置为1开始
sql_reset = 'ALTER TABLE historydata AUTO_INCREMENT=1;' 
#更新数据
sql_update = ''
#删除语句
sql_delete = ''
'''定义数据库插入函数'''
def insert_todb():    
    #创建数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                           passwd='2064', db='ultrasound', charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #插入语句，省略了列清单
    sql_insert = "INSERT INTO hisdata VALUES({0},'{1}','{2}',{3},'{4}','{5}',\
    '{6}',{7},{8},{9},{10},{11},{12},{13},'{14}',{15},'{16}','NULL','NULL','NULL',\
    'NULL','NULL','NULL')".format('NULL', name_materials,name_detail, test_number, 
    test_date, test_eqm , probe_name, probe_scale ,test_shear , test_rpm , probe_freq ,
    die_gap , test_T , test_P , wave, time_interval, test_remark)
    try:
        #执行语句
        cur.execute(sql_insert)
        #提交使语句生效
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()    
        
dir_name = r'D:\Research\实验\调距探头实验汇总\不同转速对声速及衰减的影响20170410\PP不同转速实验20170412\第四组'
'''定义插入变量'''

#sql_id = 0                     设置为自增字段，无须赋值
name_materials = 'PP'
name_detail = '纯料'
test_number = 0
test_date = '2017-04-12'
test_eqm = '单螺杆挤出机'
probe_name = ''
probe_scale = -1              
test_shear = -1
#test_rpm = 30
probe_freq = 5
die_gap = 4
test_T = 200
test_P = -1
#wave = ''
time_interval = 0.02
test_remark = '第四组'

floder_names = os.listdir(dir_name)
for fd in floder_names:
    try:
        test_rpm = float(fd)
        print(test_rpm)
    except:
        print("'{}'是一个不符合格式的文件夹".format(fd))
        continue
    floder_path = os.path.join(dir_name,fd)
    file_names = os.listdir(floder_path)
    test_number = 0
    for name in file_names:
        file_path = os.path.join(floder_path,name)
        if name[-4:] == 'zwav':
            wave = pd.read_table(file_path , engine = 'python')['DATA'].to_json()
            test_number += 1
            insert_todb()
         
elapsed = (time.clock() - start)
print("执行时间：", '%.2f' %elapsed )                
        
        
        


