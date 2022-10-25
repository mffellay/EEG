import argparse 
import time 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import scipy 
from scipy import signal 
import brainflow 
import tensorflow as tf 
from sklearn.metrics import accuracy_score, precision_score, recall_score 
from sklearn.model_selection import train_test_split 
from tensorflow.keras import layers, losses 
from tensorflow.keras.datasets import fashion_mnist 
from tensorflow.keras.models import Model 
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds 
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations, NoiseTypes, WindowFunctions 

def butter_bandpass(lowcut, highcut, fs, order=6): 
    nyq = 0.5 * fs 
    low = lowcut / nyq 
    high = highcut / nyq 
    sos = scipy.signal.butter(order, [low, high], analog=False, btype='band', output='sos') 
    return sos 

  def butter_bandpass_filter(data, lowcut, highcut, fs, order=6): 
    sos = butter_bandpass(lowcut, highcut, fs, order=order) 
    y = scipy.signal.sosfilt(sos, data) 
    return y

  with open('raw/filein.csv') as fin, open('coma/fileout.csv', 'w') as fout: 
    for line in fin: 
        fout.write(line.replace('\t', ','))
        
raw = DataFilter.read_file('coma/fileout.csv')

# Processing the raw file by changing tabs to commas, also defining Butterworth filters to be used

with open('raw/botones2.csv') as fin, open('coma/botones.csv', 'w') as fout: 
    for line in fin: 
        fout.write(line.replace('\t', ',')) 
raw = DataFilter.read_file('coma/botones.csv') 
i=0 
fs = 250.0  # Sampling frequency (Hz) 
f0 = 50.0  # Frequency to remove from the recorded signal (Hz). This is due to the 220V 50Hz outlet
Q = 100.0  # Quality factor 
b, a = signal.iirnotch(f0, Q, fs)

for i in range (1,9): 
    channel[i]=raw[i,31:] 
    std=np.std(channel[i]) 
    var[i]=channel[i]-np.mean(channel[i]) 
    var[i]=var[i]/std 
    outputSignal[i] = signal.filtfilt(b, a, var[i])
# For all the channels the 50Hz frequency is removed. There is also noise reduction by diving the average of each channel and diving it by the standard deviation.

# Its plotting time
plt.figure(figsize=(16,10)) 
plt.subplot(8, 1, 1) 
plt.plot(outputSignal[1],label='Canal 1') 
plt.legend() 
plt.title('Señal Filtrada 50[Hz] Notch ', fontsize=20
plt.subplot(8, 1, 2) 
plt.plot(outputSignal[2], label='Canal 2') 
plt.ylabel('Magnitud', fontsize=18) 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.subplot(8, 1, 3) 
plt.plot(outputSignal[3], label='Canal 3') 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.subplot(8, 1, 4) 
plt.plot(outputSignal[4], label='Canal 4') 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.ylabel('Magnitud', fontsize=18) 
plt.subplot(8, 1, 5) 
plt.plot(outputSignal[5], label='Canal 5') 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.subplot(8, 1, 6) 
plt.plot(outputSignal[6], label='Canal 6') 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.ylabel('Magnitud', fontsize=18) 
plt.subplot(8, 1, 7) 
plt.plot(outputSignal[7], label='Canal 7') 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
plt.subplot(8, 1, 8) 
plt.plot(outputSignal[8], label='Canal 8') 
plt.xlabel('Muestras', fontsize=20) 
plt.subplots_adjust(hspace=0.5) 
plt.legend() 
