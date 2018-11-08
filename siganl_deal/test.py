'''
-*- coding: utf-8 -*-
'''

from ctypes import windll,c_double
import numpy as np
import matplotlib.pyplot as plt
dll = windll.LoadLibrary(r'D:\Software\Utrasonic monitoring-python\X86Dll\ZXUTConfigMgr.dll')
def start():
    dll.ZXUT_CreatUTMgrRes()          #创建硬件资源管理器，并初始化
    dll.ZXUT_SetSmplDepth(4096)       #设置采样深度为4096
    dll.ZXUT_StartSmpl()              #开启采样

'''参数设置与获取
chan_1 = 0                                   #通道一序号
dll.ZXUT_SetRptFreq(10)                      #设置重复频率
chan_depth = dll.ZXUT_GetSmplDepth(chan_1)  #获取当前采样深度                              
dll.ZXUT_SetDemMode(3)                       #设置检波模式;0 - 全检,1 - 正检波,2 - 负检波,3 - 射频      
dll.ZXUT_SetImpMode(1)                      #设置阻抗模式，0-50欧姆，1-500欧姆
dll.ZXUT_SetPulWidth(70)                     #设置脉冲宽度
dll.ZXUT_SetTransVol(300)                    #设置发射电压
dll.ZXUT_SetMediVeloc(2000)                  #设置介质声速
dll.ZXUT_SetSoundVeloc(300)                  #设置材料声速
dll.ZXUT_SetAvgTimes(8)                      #设置平均次数
dll.ZXUT_SetTstDist(c_float(20))             #设置检测范围为20
chan_range = dll.ZXUT_GetTstRange(chan_1)    #获取检测范围
#dll.ZXUT_SetAutoGainHeight(100)             #自动增益百分比
#dll.ZXUT_SetdBBase(dB)                         #设置增益
#dll.ZXUT_SetAutoGainEnb()
'''
dll.ZXUT_LoadUTCraftFile()           #导入配置文件 


'''波形数据获取'''
ARRAY2D = (c_double *2)*4096                   #4096×2的数组类型
wave = ARRAY2D() 

def wave():
    dll.ZXUT_GetTimeWaveData(a,0)
    b = np.array(wave)
#    plt.plot(b[:,0],b[:,1])


'''关闭退出'''
def stop():
    dll.ZXUT_StopSmpl()          #关闭采样
def exit():
    dll.ZXUT_ReleaseUTMgrRes()   #关闭硬件资源管理器

