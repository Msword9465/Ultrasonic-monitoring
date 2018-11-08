 #coding: utf-8
'''
将波形原始文件划分6个波段
'''
import pymysql
import pandas as pd
import time
start = time.clock()

def wave_div(wave,t):
    wave_bands = []
    if t == 0.02:
        try:
            #波段0
            wave_bands.append(wave[0:100].to_json())
            #波段1
            top_1 = wave[3420:3520].sort_values(ascending=False).index[0] 
            wave_bands.append(wave[3420:3520].to_json())
            #波段2
            top_2 = wave[3541:4500].sort_values(ascending=False).index[0]    
            wave_bands.append(wave[top_2-50:top_2+50].to_json())
            #波段3
            top_3 = wave[top_2+50:top_2+1000].sort_values(ascending=False).index[0]
            wave_bands.append(wave[top_3-50:top_3+50].to_json())
            #波段4
            top_4 = wave[6880:6980].sort_values(ascending=False).index[0]
            wave_bands.append(wave[6880:6980].to_json())
            #波段5
            top_5 = wave[7000:9000].sort_values(ascending=False).index[0]
            wave_bands.append(wave[top_5-50:top_5+50].to_json())
        except:
            wave_bands = ['0']*6
    elif t == 0.04:
        try:
            #波段0
            wave_bands.append(wave[0:60].to_json())
            #波段1
            top_1 = wave[1715:1765].sort_values(ascending=False).index[0] 
            wave_bands.append(wave[1715:1765].to_json())
            #波段2
            top_2 = wave[1770:2500].sort_values(ascending=False).index[0]    
            wave_bands.append(wave[top_2-25:top_2+25].to_json())
            #波段3
            top_3 = wave[top_2+25:top_2+500].sort_values(ascending=False).index[0]
            wave_bands.append(wave[top_3-20:top_3+20].to_json())
            #波段4
            top_4 = wave[3445:3495].sort_values(ascending=False).index[0]
            wave_bands.append(wave[3445:3495].to_json())
            #波段5
            top_5 = wave[3500:4000].sort_values(ascending=False).index[0]
            wave_bands.append(wave[top_5-25:top_5+25].to_json())
        except:
            wave_bands = ['0']*6 
    return wave_bands

def sql_wave_div(sql_id):  
#    本机数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='2064', db='ultrasound', charset='utf8')
#    Vulur VPS服务器    
#    conn = pymysql.connect(host='104.238.129.12', port=3306, user='root', passwd='yjsql520.', db='ultrasound', charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#    从数据库中选出指定ID的原始波形
    sql_select = 'select ID,材料名称,材料说明,原始波形, 时间间隔\
                  from hisdata\
                  where ID ={};'.format(sql_id)
    cur.execute(sql_select)
    conn.commit() 
    sql_dict = cur.fetchone()
    if sql_dict :   
        t = sql_dict['时间间隔']
        wave = pd.read_json(sql_dict['原始波形'],typ = 'Series').sort_index()
    else:
        print('错误提示：找不到当前id的数据，请重新输入  ')
        #将原始波形取出6个主要波段
    wave_bands = wave_div(wave,t)
    #将划分好的波段放入   
    sql_update = "UPDATE  hisdata SET 波段1 ='{}',波段2 ='{}',\
    波段3 ='{}',波段4 ='{}',波段5 ='{}',波段6 ='{}' WHERE ID = {}".format(
    wave_bands[0],wave_bands[1],wave_bands[2],wave_bands[3],
    wave_bands[4],wave_bands[5],sql_id)
    try:
        cur.execute(sql_update)
        conn.commit()    
    except Exception as e:
        print(e)
        conn.rollback()
    cur.close()
    conn.close() 
    
sql_id = 0
for id in range(12283):      
    sql_id += 1
    sql_wave_div(sql_id)

elapsed = (time.clock() - start)
print("执行时间：", '%.2f' %elapsed )     
#导入时间：513.73(s)  
