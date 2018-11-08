# -*- coding: utf-8 -*-
"""
利用划分的6个波段，计算声参数
"""

import pymysql
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='2064', db='ultrasound', charset='utf8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql_insert = "SELECT ID,原始波形 FROM hisdata WHERE ID = 1"
cur.execute(sql_insert)
sql_dic = cur.fetchall()
cur.close()
conn.close()

wave = pd.read_json(sql_dic[0]['原始波形'],typ = 'Series').sort_index()
#注意将序号按大小重新排序
wave.index = wave.index*0.02

ax = plt.subplot(111) 
wave.plot(ax=ax,fontsize = 24,figsize = (20,5),linewidth = 1)
ax.set_title(fontsize = 24,label = '原始波形')

df1 = wave[0:2]
df2 = wave[68.8:70.8]
df3 = wave[75.8:77.8]
df4 = wave[83:85]
df5 = wave[137.96:139.96]
df6 = wave[145:147]

fig,axes = plt.subplots(nrows = 2,ncols = 3,figsize=(20,10))
df1.plot(ax=axes[0,0],xticks=np.linspace(0,2,6),fontsize = 20,linewidth = 3)
axes[0,0].set_title(fontsize = 24,label = '波段1')

df2.plot(ax=axes[0,1],xticks=np.linspace(68.8,70.8,6),fontsize = 20,linewidth = 3)
axes[0,1].set_title(fontsize = 24,label = '波段2')

df3.plot(ax=axes[0,2],xticks=np.linspace(75.8,77.8,6),fontsize = 20,linewidth = 3)
axes[0,2].set_title(fontsize = 24,label = '波段3')

df4.plot(ax=axes[1,0],xticks=np.linspace(83,85,6),fontsize = 20,linewidth = 3)
axes[1,0].set_title(fontsize = 24,label = '波段4')

df5.plot(ax=axes[1,1],xticks=np.linspace(137.96,139.96,6),fontsize = 20,linewidth = 3)
axes[1,1].set_title(fontsize = 24,label = '波段5')

df6.plot(ax=axes[1,2],xticks=np.linspace(145,147,6),fontsize = 20,linewidth = 3)
axes[1,2].set_title(fontsize = 24,label = '波段6')

plt.tight_layout(1)

