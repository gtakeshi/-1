import math
import numpy as np  
import matplotlib.pyplot as plt
from scipy import signal

def gene_sample():
    Hz = 50
    Period = 1/Hz    #サンプリング周期
    Number = 1000
    y = np.zeros((1,Number))
    y[0][int(Number/2)] = 20
    t = [i/Hz for i in range(0,Number)]
    
    return t,y,Period,Number

def w(t , D , Lw):
    if (D - Lw / 2) <= t <= (D + Lw / 2):
        w_tD = 0.54 + 0.46 * (np.cos(2 * np.pi * ((t - D) / Lw)))  
    else:
        w_tD = 0
        
    return w_tD

def hw(T , t , D ,Lw):
    #print(w(t , D , Lw))
    h_w = np.sinc( (np.pi / T) * (t - D) ) * w(t , D , Lw)
    return h_w

t,y,p,num = gene_sample()
h_w = [hw(p,i * p, 10.99, p * 10) for i in range(0,num)]
#print(np.array(h_w))   #検証用
plt.plot(t,y[0])
plt.xlabel("seconds")
y = y[0]
#print(len(y),len(h_w))  #検証用
con = np.convolve( np.array(h_w),y,mode='same')
#print(len(con))    #検証用
#print(con)
i = [x + 10 for x in t]

plt.plot(i,con)

plt.show()

#print(hw(30,30,34,8))     #検証用 
