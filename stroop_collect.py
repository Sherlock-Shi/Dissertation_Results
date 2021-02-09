import numpy as np
import pandas as pd
import glob as gb
import os 

path = 'c:/Users/Sherlock/OneDrive - Durham University/Dissertation/Dissertation Results/Final Data unpacked/stroop/'
filenames = gb.glob(path+'/*txt')

# initialize three list to store final results from single participants
# stroop_effect = congruent - incongruent rt when correct
stroop_effect = []

c_rt_avg_control= []
c_rt_avg_congruent= []
c_rt_avg_incongruent = []

subject_id = []

correct_rate_control = []
correct_rate_congruent = []
correct_rate_incongruent = []

# get each file under the directory
for file in filenames:
     df = pd.read_csv(file, sep = ' ', header = None, index_col=False, 
                 names = ['BLOCKNAME', 'condition', 'color_word', 'word_color', 
                          'condition_num', 'TABLEROW', 'key', 'status', 'rt'])
     
     # subset experimental rows
     ex_blocks = df[(df['BLOCKNAME'] == 'word_experimental') | (df['BLOCKNAME'] == 'block_experimental')]
     
     # control blocks are to make sure that stroop effect seen in participants is due to their difficulty in differentiating colors
     # subset control, congruent and incongruent trials
     controls = ex_blocks[ex_blocks['condition'] == 'control']
     congruent = ex_blocks[ex_blocks['condition'] == 'congruent']
     incongruent = ex_blocks[ex_blocks['condition'] == 'incongruent']
     
     # subset rows that were answered correctly & rt_avg from each condition
     c_controls = controls[controls['status'] == 1]
     c_congruent = congruent[congruent['status'] == 1]
     c_incongruent = incongruent[incongruent['status'] == 1]
     
     # calc the correct_rate of controls, congruent, incongruent
     rate_control = controls['status'].value_counts(normalize=True)
     correct_rate_control.append(round(rate_control.array[0], 2))
     
     rate_congruent = congruent['status'].value_counts(normalize=True)
     correct_rate_congruent.append(round(rate_congruent.array[0], 2))

     rate_incongruent = incongruent['status'].value_counts(normalize=True)
     correct_rate_incongruent.append(round(rate_incongruent.array[0], 2))
     
     # calc rt_avg from c_controls, c_congruent, c_incongruent
     c_rt_avg_control.append(round(np.mean(c_controls['rt']), 2))
     c_rt_avg_congruent.append(round(np.mean(c_congruent['rt']), 2))
     c_rt_avg_incongruent.append(round(np.mean(c_incongruent['rt']), 2))
     
     # find the filename and append the filename to as subject_id
     subject = 's.' + os.path.basename(file)[-40:]
     subject_id.append(subject)
     
frame = pd.DataFrame({'subject_id': subject_id, 'c_rt_avg_control': c_rt_avg_control, 
                      'c_rt_avg_congruent': c_rt_avg_congruent, 'c_rt_avg_incongruent': c_rt_avg_incongruent,
                      'correct_rate_control':correct_rate_control, 'correct_rate_congruent': correct_rate_congruent, 
                      'correct_rate_incongruent': correct_rate_incongruent})

# calc the stroop effect for each participants
frame['stroop_effect'] = frame['c_rt_avg_incongruent'] - frame['c_rt_avg_congruent']
frame.to_excel('stroop_complete.xlsx')    