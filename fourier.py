filtered = butter_bandpass_filter(outputSignal[1], lowcut=2, highcut=35, fs=250, order=6) 
data_range = filtered[600:850]  # range selected in which the impulse is visible 
fft_vals = np.absolute(np.fft.rfft(data_range)) 
fft_freq = np.fft.rfftfreq(len(data_range), 1.0/fs) 

eeg_bands = {'Delta': (2, 4), 
             'Theta': (4, 8), 
             'Alpha': (8, 12), 
             'Beta': (12, 30), 
             'Gamma': (30, 45)} 

eeg_band_fft = dict() 
for band in eeg_bands:   
    freq_ix = np.where((fft_freq >= eeg_bands[band][0]) &  
                       (fft_freq <= eeg_bands[band][1]))[0] 
    eeg_band_fft[band] = np.mean(fft_vals[freq_ix]) 
    # EEG Band graph with average values 

df = pd.DataFrame(columns=['band', 'val']) 
df['band'] = eeg_bands.keys() 
df['val'] = [eeg_band_fft[band] for band in eeg_bands] 
ax = df.plot.bar(x='band', y='val', legend=False) 
ax.set_xlabel("Banda EEG") 
ax.set_ylabel("Amplitud promedio de Banda") 
