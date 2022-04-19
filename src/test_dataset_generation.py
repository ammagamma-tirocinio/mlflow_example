import numpy as np
import pandas as pd
import os
import copy
import sys
import pickle
import json
import datetime


def create_current_dataset(current_day, test_dataset_path, window = 0):
    test_dataset = pd.read_csv(test_dataset_path)
    test_dataset.dteday = pd.to_datetime(test_dataset.dteday)
    df_current = test_dataset[test_dataset['dteday'].isin(pd.period_range(end=current_day, freq="D", periods=30).to_timestamp())]
    return copy.deepcopy(df_current)
def parse_date(current_day):
    year = current_day.split('-')[0]
    month = current_day.split('-')[1]
    day = str(current_day).split('-')[2]
    date = datetime.datetime(year,month,day)
    return date

# set working directory
current_dir = os.getcwd()
sys.stderr.write("Current directory" + str(current_dir) + "\n")

#os.chdir('..')
current_dir = os.getcwd()
sys.stderr.write("Current directory" + str(current_dir) + "\n")

current_day = sys.argv[3]
run_dir = sys.argv[2]
data_path = sys.argv[1]
#sys.stderr.write(print(current_day))

path_df_test = os.path.join(current_dir,'storage','test.csv')
run_path = os.path.join(current_dir,'run')
print(run_path)
current_dataset = create_current_dataset(current_day,path_df_test)

if not os.path.exists(run_path):
    os.mkdir(run_path)
current_dataset.to_csv(os.path.join(current_dir,run_dir))