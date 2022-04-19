import pandas as pd
import requests
import zipfile
import io
import copy
import os
import sys

current_dir = os.getcwd()
sys.stderr.write("Current directory" + str(current_dir) + "\n")
#os.chdir('..')

current_dir = os.getcwd()
final_dir = os.path.join(current_dir,'storage')
sys.stderr.write("Data directory" + str(final_dir) + "\n")

content = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip").content

with zipfile.ZipFile(io.BytesIO(content)) as arc:
    raw_data = pd.read_csv(arc.open("day.csv"), header=0, sep=',', parse_dates=['dteday'], index_col='dteday')

da = raw_data[(raw_data.index.year == 2011) & ((3 < raw_data.index.month) & (raw_data.index.month < 10))]
db = raw_data[(raw_data.index.year == 2012) & ((3 < raw_data.index.month) & (raw_data.index.month < 10))]
dc = raw_data[(raw_data.index.year == 2011) & (( 3 >= raw_data.index.month) |(raw_data.index.month >= 10))]
dd = raw_data[(raw_data.index.year == 2011) & (( 3 >= raw_data.index.month) | (raw_data.index.month >= 10))]

d1 = copy.deepcopy(pd.concat([da, db])) # winter
d2 = copy.deepcopy(pd.concat([dc,dd])) # summer

train = copy.deepcopy(raw_data[(raw_data.index.day<20) & ((raw_data.index.year == 2011) | ((raw_data.index.year == 2012) &(raw_data.index.month < 8)))])
val = copy.deepcopy(raw_data[(raw_data.index.day>=20) & ((raw_data.index.year == 2011) | ((raw_data.index.year == 2012) &(raw_data.index.month < 8)))])
test = copy.deepcopy(raw_data[(raw_data.index.year == 2012) &(raw_data.index.month >= 8)])

if not os.path.exists(final_dir):
    os.mkdir(final_dir)
    
if 'train.csv' in os.listdir(final_dir):
    sys.stderr.write('Data already stored in' + str(final_dir))
else:
    train.to_csv(os.path.join(final_dir,'train.csv'))
    val.to_csv(os.path.join(final_dir,'val.csv'))
    test.to_csv(os.path.join(final_dir,'test.csv'))
    sys.stderr.write('Data stored in' + str(final_dir))




