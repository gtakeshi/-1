import math
import numpy as np  
import matplotlib.pyplot as plt
from scipy import signal

def gene_sample():    #サンプル生成の関数
    Hz = 20
    Period = 1/Hz    #サンプリング周期
    Number = 1000
    y = np.zeros((1,Number))
    y[0][int(Number/2)] = 10
    t = [i/Hz for i in range(0,Number)]
    
    return t,y,Period,Number

def w(t , D , Lw):     #w(t-D)を算出する関数
    if (D - Lw / 2) <= t <= (D + Lw / 2):
        w_tD = 0.54 + 0.46 * (np.cos(2 * np.pi * ((t - D) / Lw)))  
    else:
        w_tD = 0
        
    return w_tD

def hw(T , t , D ,Lw):    #h_w(t)を算出する関数
    #print(w(t , D , Lw))
    h_w = np.sinc( (np.pi / T) * (t - D) ) * w(t , D , Lw)
    return h_w

t,y,p,num = gene_sample()   
delay = 20
h_w = [hw(p,i * p, delay, p * 10) for i in range(0,num)]

#print(np.array(h_w))   #検証用

y = y[0][:]
#print(len(y),len(h_w))  #検証用
con = np.convolve( np.array(h_w),y,mode='same')    #畳み込み
#print(len(con))    #検証用

plt.plot(t,y)         #元の信号を表示
plt.xlabel("seconds")

i = [x + delay for x in t]   #処理後の信号を表示
plt.plot(i,con)     
plt.show()

#print(hw(30,30,34,8))     #検証用 
