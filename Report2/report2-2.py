import numpy as np
import wave
import matplotlib.pyplot as plt


with wave.open("exam.wav") as w_obj:          # WAVファイルを開く with使うと､close()いらず
    data = w_obj.readframes(w_obj.getnframes())
    frame = w_obj.getnframes()                  #ここでフレーム数を得る
    Hz = w_obj.getframerate()                      #周波数も得る
buffer = np.frombuffer(data, dtype="int16") / float((2 ^ 15))     #バッファ計算

dft = np.abs(np.fft.fft(buffer))         #DFTを計算する

plt.figure(figsize=(20, 10))            #パワースペクトルを出力
plt.subplot(211)
plt.plot(np.linspace(0, Hz , int(frame)) , ( dft / 60000))
plt.xlabel("frequence(Hz)")
plt.ylabel("Amp[dB]")
plt.show()
