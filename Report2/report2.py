from librosa import lpc
from scipy.io.wavfile import read
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

fs, x = read("exam.wav")     #音声ファイルの読み込み

print("サンプリングは: "+str(fs))           #ここで､exam.wavの成分を確認する
                        #結果をみると､標本化周波数は11025Hzということが分かった
print("データ型は: "+str(x.dtype))        #int16型ということが分かった

# with open("wave.txt","w") as f_obj:                 #試しに､exam.wavの成分をwave.txtに書き込む
#     np.set_printoptions(threshold=np.inf)
#     f_obj.write(str(x))
     
a = lpc(x/2000,12)               #ここで､LPCを実行させる
'''                        
原理は以下である(Burg法)  これを使ってもうまくLPCを実現できる

def burg(signal, order):
    x = signal
    P = order
    a = np.zeros(P+1)
    k = np.zeros(P)
    a[0] = 1

    f = np.copy(signal)
    b = np.copy(signal)

    N = len(f)
    for p in range(P):
        kf = f[p+1:]
        kb = b[:N-p-1]
        D = np.sum(kf * kf) + np.sum(kb * kb)
        k[p] = -2 * np.sum(kf * kb) / D
        U = a[0:p+2]
        V = U[::-1]
        a[0:p+2] = U + k[p] * V
        fu = k[p] * b[:N-p-1]
        bu = k[p] * f[p+1:]
        f[p+1:] += fu
        b[:N-p-1] += bu

    return a, k
'''

def main_component(a):    #主要成分を求める関数を定義
    w, h = signal.freqz(1, a)
    for index in range(len(h)):
        if (20 * np.log10(np.abs(h[index]))) == max(20 * np.log10(np.abs(h))):
            print("主要成分は: "+ str(fs * w[index] / 2.0 / np.pi) + " Hz")
            
def pw_spectrum(fs,a):          #パワースペクトル出力の関数を定義
    w, h = signal.freqz(1, a) 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(fs * w / 2.0 / np.pi, 20 *  np.log10(np.abs(h)))
    ax.set_xlabel('frequency [Hz]')
    
    ax.set_ylabel('Amp[dB]')
    plt.show()

main_component(a)   #主要成分を出力
pw_spectrum(fs,a)     #パワースペクトル出力 

