# Dissertation_Results
Raw Data, processed results and Python scripts for data analysis of Sherlock Shi's Dissertation

# Directory Explanation
- '**Final Data unpacked**' Folder has all of the **unprocessed results** both as a zip file (i.e., Final Data.zip) and as excels files (data.xlsx for VGQ results, igt_complete.xlsx for IGT results, stroop_complete.xlsx for Stroop results and corsispan_complete.xlsx for CBT results)
  
  - Folders with in this folder contains data from every cognitve tasks that are not combined and processed into one spread sheet, so *every file in the respective folder represents a participants, and every row in the spreadsheet (e.g., stroop_complete.xlsx) represents a participant)*.
  
- The **processed results** (the full results with three cognitve task outcomes and VG playtime, excluding outliers) is the **Finale(V2).xlsx**. Each row in this excel file represents a participants

- The Python script for calculating the primary outcomes of every cognitve task and combine them into one spreadsheet is written using .py files
  
  - The script for calculating **IGT outcomes** and merging them into one spreadsheet('igt_complete.xlsx) is **igt_collect.py**
  - The script for calculating **Stroop outcomes** and merging them into one spreadsheet is **stroop_collect.py**
  - The script for **CBT** is **cspan_collect.py**

- The Python script of data analysis are written using *Anaconda Jupyter Notebook*, thus the file extension is .ipynb (representing a iPython interactive terminal file). 
  
   - The script for **merging three cognitve tasks and VGQ** with corresponding subject ID is **'Result_merge.ipynb' and 'Result_merge(V2).ipynb’**.
   - The script for **cleaning the merged results** (remove outliers, etc.) is **'Results_clean.ipynb'**
   - The script for **calcualting inferential and descriptive statistics** of the cleaned results is **'Results_Statistic.ipynb'**
