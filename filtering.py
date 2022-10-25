# Canales 1 y 2 /Channels
plt.figure(figsize=(16,10)) 
plt.title('Datos EEG, Filtro 1.5-35[Hz]') 
for x in range(1,3): 
    filtered = butter_bandpass_filter(outputSignal[x], lowcut=2, highcut=35, fs=250, order=6) 
    plt.plot(var[x], c='y', label='Raw Data channel' + str(x)) 
    plt.plot(filtered, label='Channel'+str(x)) 
plt.legend() 
# Canales 3 y 4 /Channels
plt.figure(figsize=(16,10)) 
plt.title('Datos EEG, Filtro 1.5-35[Hz]') 
for x in range(3,5): 
    filtered = butter_bandpass_filter(outputSignal[x], lowcut=2, highcut=35, fs=250, order=6) 
    plt.plot(var[x], c='y', label='Raw Data channel' + str(x)) 
    plt.plot(filtered, label='Channel'+str(x)) 
plt.legend() 
# Canales 5 y 6 /Channels
plt.figure(figsize=(16,10)) 
plt.title('Datos EEG, Filtro 1.5-35[Hz]') 
for x in range(5,7): 
    filtered = butter_bandpass_filter(outputSignal[x], lowcut=2, highcut=35, fs=250, order=6) 
    plt.plot(var[x], c='y', label='Raw Data channel' + str(x)) 
    plt.plot(filtered, label='Channel'+str(x)) 
plt.legend() 
# Canales 7 y 8 /Channels
plt.figure(figsize=(16,10)) 
plt.title('Datos EEG, Filtro 1.5-35[Hz]') 
for x in range(7,9): 
    filtered = butter_bandpass_filter(outputSignal[x], lowcut=2, highcut=35, fs=250, order=6) 
    plt.plot(var[x], c='y', label='Raw Data channel' + str(x)) 
    plt.plot(filtered, label='Channel'+str(x)) 
plt.legend() 
