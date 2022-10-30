import argparse
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal
import brainflow 
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds

def main(): 
    BoardShim.enable_dev_board_logger() 
    params = BrainFlowInputParams () 
    board_id=0 
    params.serial_port = '/dev/ttyUSB0' #USB address must be changed for it to work
    eeg_channels = BoardShim.get_eeg_channels(BoardIds.CYTON_BOARD.value) 
    board = BoardShim(board_id, params) 
    board.prepare_session() 
    board.start_stream() 
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread') 
    print('Comienzo') 
    time.sleep(5) 
    data= board.get_current_board_data(1000) 
    board.stop_stream() 
    board.release_session() 
    datf= pd.DataFrame(np.transpose(data)) 
    #print(' Data From the Board') 
    #print(df.head(10)) 
    DataFilter.write_file(data, 'test2raw.csv','w') 
    print('samples in file .csv') 
if __name__ == "__main__": 
    main()
# Board data streaming through USB
# This records 1000 samples in a .csv file that you can access with software such as Excel for all the 8 channels connected to the Cyton board.
