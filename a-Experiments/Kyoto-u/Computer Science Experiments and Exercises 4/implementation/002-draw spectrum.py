import matplotlib.pyplot as plt
import numpy as np
import librosa


#サンプリングレート
SR = 16000

#音声ファイル(wavファイル)を読み込む
x, _ = librosa.load('/content/aiueo.wav', sr=SR)

#高速フーリエ変換
fft_spec = np.fft.rfft(x)

#複素スペクトル→対数振幅スペクトルに
fft_log_abs_spec = np.log(np.abs(fft_spec))


#スペクトルを描画
fig = plt.figure()
plt.xlabel('frequency [Hz]') # x軸のラベルを設定
plt.ylabel('amplitude') # y軸のラベルを設定
plt.xlim([0, SR/2]) 
x_data = np.linspace((SR/2)/len(fft_log_abs_spec), SR/2, len(fft_log_abs_spec))
plt.plot(x_data, fft_log_abs_spec)
plt.show()




# 横 軸 を0 ̃2000 H zに拡大
# xlimで表示の領域を変えるだけ
fig = plt.figure()
plt.xlabel('frequency [Hz]')
plt.ylabel('amplitude')
plt.xlim([0, 2000])
plt.plot(x_data, fft_log_abs_spec)
# 表 示
plt.show()
