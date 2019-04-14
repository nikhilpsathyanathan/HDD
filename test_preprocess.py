import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
if not os.path.exists('predict'):
    os.makedirs('predict')

def test_process(file_name):
    data_train = pd.read_csv(file_name,usecols=[ 'model', 'capacity_bytes', 'failure', 'smart_5_raw','smart_9_raw','smart_10_raw', 'smart_184_raw' ,'smart_187_raw', 'smart_188_raw', 'smart_192_raw','smart_196_raw', 'smart_197_raw',  'smart_198_raw'])
    import os
    model_names=os.listdir("data")
    print(data_train['failure'].sum())  
    for model in model_names:
        process_data=data_train.loc[data_train['model'] == model[:-4]]
        data_train.drop(data_train[data_train['model'] == model[:-4]].index, inplace=True)
        if process_data['failure'].sum()>=0:
            print(process_data['failure'].sum())   
            process_data.drop(process_data.loc[process_data['capacity_bytes']==-1].index, inplace=True)
            process_data.drop('capacity_bytes', axis=1, inplace=True)
            process_data.drop('model', axis=1, inplace=True)
            attribute = process_data.columns
            for att in attribute:
                if process_data[att].isnull().sum()>=1:
                    process_data.drop(att, axis=1, inplace=True)
            process_data.to_csv( "./predict/"+model, index=False, encoding='utf-8-sig')



