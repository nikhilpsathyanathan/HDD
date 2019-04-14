import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

print("Model 2 preprocessig started")
data_train = pd.read_csv('train.csv', usecols=['date', 'serial_number', 'model', 'failure', 'smart_5_raw', 'smart_9_raw', 'smart_10_raw',
                                               'smart_184_raw', 'smart_187_raw', 'smart_188_raw', 'smart_192_raw', 'smart_197_raw',  'smart_198_raw'])

data_train.dropna(inplace=True, axis=0)
fail_case = data_train['serial_number'].loc[data_train['failure'] == 1]  #get failure device serial num 
train_data = pd.DataFrame()
count = 0

# window selection of 6days
for fail in fail_case:   # for each model take 6 day beofore data mark all data before 2 days as failure
    data = data_train.loc[data_train['serial_number'] == fail]   
    data = data.sort_values(['date', 'failure'],
                            ascending=False).groupby('failure').head(6)   #sort data based on date and failure
    try:
        data.loc[1:3, 'failure'] = 1 #mark last 3 data as failuree
    except:
        pass
    train_data = pd.concat([train_data, data])
    count = count+1
    print(count)

missing_vals= data_train.isnull().sum().sort_values(ascending=False)  # print if there us any missing values
print(missing_vals) 

data_train.dropna(inplace=True, axis=0)
train_data.drop('model', axis=1, inplace=True)
train_data.drop('date', axis=1, inplace=True)
train_data.to_csv("model2.csv", index=False, encoding='utf-8-sig')  # save as a csv file
print("Model 2 preprocessig finished")