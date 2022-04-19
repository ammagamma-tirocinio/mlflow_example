import copy
import pandas as pd
import pickle
import sys
import os
from sklearn.ensemble import AdaBoostRegressor

current_dir = os.getcwd()
sys.stderr.write("Current directory" + str(current_dir) + "\n")

train_path = os.path.join(sys.argv[1],'train.csv')
output = sys.argv[2]

df_train = pd.read_csv(train_path)
df_train.index = pd.to_datetime(df_train.dteday)
train = copy.deepcopy(df_train.drop(columns = 'dteday'))

X_train = train.iloc[:,:-1]
y_train = train.iloc[:,-1]

sys.stderr.write("Input matrix size {}\n".format(train.shape))
sys.stderr.write("X matrix size {}\n".format(X_train.shape))
sys.stderr.write("Y matrix size {}\n".format(y_train.shape))

model = AdaBoostRegressor()
model.fit(X_train,y_train)

with open(output, "wb") as fd:
    pickle.dump(model, fd)