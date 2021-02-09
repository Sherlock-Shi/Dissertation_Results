import numpy as np
import pandas as pd
import glob as gb
import os 

path = 'c:/Users/Sherlock/OneDrive - Durham University/Dissertation/Dissertation Results/Final Data unpacked/igt_test/'
filenames = gb.glob(path+'/*txt')

# initialize three list to store final results from single participants
final_amount = []
loss_total = []
win_total = []
rt_avg = []
subject_id = []
b1_score = []
b2_score = []
b3_score = []
b4_score = []
b5_score = []

def block_score(list_for_append, min = 0, max = 20):
     ad = 0
     dis = 0
     for i in df.iloc[min:max]['card_selected']:
          if i == 1 or i == 2:
               ad = ad + 1
          else:
               dis = dis + 1
     list_for_append.append(ad - dis)


# get each file under the directory
for file in filenames:
     df = pd.read_csv(file, sep = ' ', header = None, index_col=False, 
                 names = ['decisiontime', 'card_selected', 'p5', 'p7', 'total_before', 'final_total', 'win', 'lose'])
     
     # check block_scores 
     block_score(b1_score)
     block_score(b2_score, min = 20, max = 40)
     block_score(b3_score, min = 40, max = 60)
     block_score(b4_score, min = 60, max = 80)
     block_score(b5_score, min = 80, max = 100)
     
     # appned the final_amount to final_amount list
     final_amount.append(df.iloc[-1, 5])
     
     # sum the loss and append to loss_total list
     total_loss = np.sum(df['lose'])
     loss_total.append(total_loss)
     
     # sum the win and append to win_total list
     total_win = np.sum(df['win'])
     win_total.append(total_win) 
     
     # calc the average rt and append to rt_avg 
     rt_avg.append(round(np.mean(df['decisiontime']), 2))
     
     # find the filename and append the filename to as subject_id
     subject = 's.' + os.path.basename(file)[-40:]
     subject_id.append(subject)

dm_under_limited = np.array(b1_score) + np.array(b2_score)
dm_under_risk = np.array(b3_score) + np.array(b4_score) + np.array(b5_score)
     
frame = pd.DataFrame({'subject_id': subject_id, 'rt_avg': rt_avg, 'final_amount': final_amount, 
                      'loss_total': loss_total, 'win_total': win_total, 'b1_score': b1_score, 'b2_score': b2_score,
                      'b3_score': b3_score, 'b4_score': b4_score, 'b5_score': b5_score, 'dm_under_limited': dm_under_limited,
                      'dm_under_risk': dm_under_risk})
frame.to_excel('igt_complete(R2).xlsx')