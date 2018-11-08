'''
多条波形信号处理
'''
import utwave
import pandas as pd

df = pd.read_excel(r'D:\Jupyter Notebook\Research_Ultrasound\加工条件影响\不同转速.xlsx')['30']
print(utwave.wavepoint(df))