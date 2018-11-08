'''
超声信号（单条）处理函数
特征点获取
声参数求解
波段划分
幅相频谱
'''
import numpy as np
import pandas as pd

point_index = ['A-00','A-01','A-02','A-03','A-04','A-05','A-06'\
    ,'T-00','T-01','T-02','T-03','T-04','T-05','T-06'\
    ,'A-10','A-11','A-12','A-13','A-14','A-15','A-16'\
    ,'T-10','T-11','T-12','T-13','T-14','T-15','T-16',]

Time = np.linspace(0, 163.8, 4096)

def pointmax(df, Tl, Tr):      
    '''区间最大值及索引'''          
    A = df[(df.index <= Tr) & (df.index >= Tl) ].max()
    T = df[(df.index <= Tr) & (df.index >= Tl) ].idxmax()
    point = pd.Series([A,T],index = ['A','T'])
    return point

def pointmin(df, Tl, Tr):  
    '''区间最小值及其索引 '''              
    A = df[(df.index <= Tr) & (df.index >= Tl) ].min()
    T = df[(df.index <= Tr) & (df.index >= Tl) ].idxmin()
    point = pd.Series([A,T],index = ['A','T'])
    return point


def wavepoint(df):    
    '''获取特征点'''                  
    pmax0 = pointmax(df,0,1) 
    pmin0 = pointmin(df,0,1)
    pmax1 = pointmax(df,60,80)            
    pmin1 = pointmin(df,68,80)
    pmax2 = pointmax(df,75,90)             #点2和5靠经验值，有待求证！！！
    pmin2 = pointmin(df,75,90)             
    t1 = pmax2['T'] + 0.8 * (pmax2['T']- pmin1['T'])
    t2 = pmax2['T'] + 1.2 * (pmax2['T']- pmin1['T'])
    pmax3 = pointmax(df,t1,t2)
    pmin3 = pointmin(df,t1,t2)
    pmax4 = pointmax(df,135,145)
    pmin4 = pointmin(df,135,145)
    pmax5 = pointmax(df,140,160)
    pmin5 = pointmin(df,140,160)
    t3 = pmax5['T'] + 0.8 * (pmax5['T']- pmin4['T'])
    t4 = pmax5['T'] + 1.2 * (pmax5['T']- pmin4['T'])
    pmax6 = pointmax(df,t3,t4)
    pmin6 = pointmin(df,t3,t4)
    maxpoint = pd.concat([pmax0,pmax1,pmax2, pmax3,pmax4,pmax5,pmax6])
    maxpoint = pd.concat([maxpoint['A'],maxpoint['T']])                      #幅值和时间类合并并一次对方
    minpoint = pd.concat([pmin0,pmin1,pmin2,pmin3,pmin4,pmin5,pmin6])   
    minpoint = pd.concat([minpoint['A'],minpoint['T']])
    wave_point = pd.concat([maxpoint,minpoint])                              #先正坐标点再负坐标点
    wave_point.index =  point_index                                   #点的顺序需要整理
    return wave_point
    
