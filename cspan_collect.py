import numpy as np
import pandas as pd
import glob as gb
import os 

path = 'c:/Users/Sherlock/OneDrive - Durham University/Dissertation/Dissertation Results/Final Data unpacked/corsi_block/'
filenames = gb.glob(path+'/*txt')

# initialize three list to store final results from single participants
cspan = []
rt_avg = []
subject_id = []

# get each file under the directory
for file in filenames:
     df = pd.read_csv(file, sep = ' ', header = None, index_col=False, 
                 names = ['corsispan','currentcount', 'SeqCorrect', 'TABLEROW', 'RT', 'BLOCKNAME'])
     
     # appned the current subject's cspan to the list
     cspan.append(df.iloc[-1, 0])
     
     # subset the experimental rows and append the rt avg
     experimental = df[df['BLOCKNAME'] == 'experimental']
     rt_avg.append(round(np.mean(experimental['RT']), 2))
     
     # find the filename and append the filename to as subject_id
     subject = 's.' + os.path.basename(file)[-40:]
     subject_id.append(subject)
     
frame = pd.DataFrame({'subject_id': subject_id, 'cspan': cspan, 'rt_avg': rt_avg})
frame.to_excel('corsispan_complete.xlsx')