import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
if not os.path.exists('data'):    
    os.makedirs('data')      # Create data folder for saving the file  

print("Preprocessing train data :started ")
data_train = pd.read_csv('train.csv',usecols=['model', 'capacity_bytes', 'failure', 'smart_5_raw','smart_9_raw','smart_10_raw', 'smart_184_raw' ,'smart_187_raw', 'smart_188_raw', 'smart_192_raw','smart_196_raw', 'smart_197_raw',  'smart_198_raw'])
model_names=data_train['model'].drop_duplicates()  # TO GET  unique model names
print(data_train['failure'].sum())    # failure count on log

# this would preprocess all the data group by model name and select only columns and rows based on thier missing values
for model in model_names:
    process_data=data_train.loc[data_train['model'] == model]
    data_train.drop(data_train[data_train['model'] == model].index, inplace=True)
    if process_data['failure'].sum()>=6:        # SELECT only failure greater than 6  because SMOTE sampling need minimum 6 class values
        print(process_data['failure'].sum())   
        process_data.drop(process_data.loc[process_data['capacity_bytes']==-1].index, inplace=True)
        process_data.drop('capacity_bytes', axis=1, inplace=True)
        process_data.drop('model', axis=1, inplace=True)
        attribute = process_data.columns
        for att in attribute:
            if process_data[att].isnull().sum()>=1:
                process_data.drop(att, axis=1, inplace=True)    # to drop cols
        process_data.to_csv( "./data/"+model+".csv", index=False, encoding='utf-8-sig')  #save csv file for each model

print("Preprocessing test data : completed")


