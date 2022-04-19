import pandas as pd
import numpy as np
import sys
import os
import pickle
import json
import copy

current_dir = os.getcwd()
final_dir = os.path.join(current_dir,'storage')
sys.stderr.write("Current directory" + str(current_dir) + "\n")

model_file = sys.argv[1]
data_path = sys.argv[2]
scores_file = sys.argv[3]

print(sys.argv[0])

print(data_path)
df_val = pd.read_csv(os.path.join(data_path,'val.csv'))
df_val.index = pd.to_datetime(df_val.dteday)
val = copy.deepcopy(df_val.drop(columns = 'dteday'))

X_val = val.iloc[:,:-1]
y_val = val.iloc[:,-1]

sys.stderr.write("Input matrix size {}\n".format(val.shape))
sys.stderr.write("X matrix size {}\n".format(X_val.shape))
sys.stderr.write("Y matrix size {}\n".format(y_val.shape))

with open(model_file,'rb') as fd:
    model = pickle.load(fd)

res = model.predict(X_val)
MAPE = np.mean(np.abs(y_val - res) / y_val) * 100
results = pd.DataFrame({'predcted': res, 'labels': y_val})
results.to_csv(os.path.join(final_dir,'results.csv'))

with open(scores_file, "w") as fd:
    json.dump({"MAPE": MAPE},
              fd,
              indent=4)
results.to_csv(os.path.join(final_dir,'results.csv'))


sys.stderr.write("Mape = {}%\n".format(round(MAPE,2)))
