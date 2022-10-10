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
with open('raw/botones2.csv') as fin, open('coma/botones.csv', 'w') as fout: 
    for line in fin: 
        fout.write(line.replace('\t', ',')) 
raw = DataFilter.read_file('coma/botones.csv') 
