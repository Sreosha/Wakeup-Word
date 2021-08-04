import os
import librosa
import librosa.display
import numpy as np
import pandas as pd

all_data=list()
data_path={1:["wakeup_audio/"+ file_path for file_path in os.listdir("wakeup_audio/")],
0:["bg_noise/"+ file_path for file_path in os.listdir("bg_noise/")]}

for class_label,list_of_files in data_path.items():
    for each_file in list_of_files:
        data,sample_rate=librosa.load(each_file)
        mfccs=librosa.feature.mfcc(y=data,sr=sample_rate,n_mfcc=40)
        mfcc_processed=np.mean(mfccs.T,axis=0)
        all_data.append([mfcc_processed,class_label])
    print("Successfully preprocessed")

df=pd.DataFrame(all_data,columns=["features","class_label"])
df.to_pickle("final_audio_wakeup/audio_data.csv")