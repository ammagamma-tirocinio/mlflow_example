import pandas as pd
import numpy as np
import sys
import os
import pickle
import json
import copy

current_dir = os.getcwd()
final_dir = os.path.join(current_dir,'')
sys.stderr.write("Current directory" + str(current_dir) + "\n")

model_file = sys.argv[1]
data_path = sys.argv[2]
scores_file = sys.argv[3]

def create_dataset(test_dataset_path, window = 0):
    test_dataset = pd.read_csv(test_dataset_path)
    test_dataset.dteday = pd.to_datetime(test_dataset.dteday)
    test_dataset.set_index('dteday')
    current_dataset = copy.deepcopy(test_dataset.drop(columns=['dteday','Unnamed: 0']))
    return current_dataset

print(data_path)

test = create_dataset(os.path.join(current_dir, data_path))

X_test = test.iloc[:,:-1]
y_test = test.iloc[:,-1]

sys.stderr.write("Input matrix size {}\n".format(test.shape))
sys.stderr.write("X matrix size {}\n".format(test.shape))
sys.stderr.write("Y matrix size {}\n".format(y_test.shape))

with open(model_file,'rb') as fd:
    model = pickle.load(fd)

res = model.predict(X_test)
MAPE = np.mean(np.abs(y_test.iloc[-1] - res[-1]) / y_test.iloc[-1]) * 100
results = pd.DataFrame({'predcted': res, 'labels': y_test})

run_dir = os.path.join(current_dir,'run')
results.to_csv(os.path.join(run_dir,'result.csv'))

with open(scores_file, "w") as fd:
    json.dump({"MAPE": MAPE},
              fd,
              indent=4)
sys.stderr.write("Mape = {}%\n".format(round(MAPE,2)))
