
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import os

def predict_new(file_name,model_name):
    X = pd.read_csv('./data/'+model_name+'.csv')  # read test data
    fail = X.loc[X['failure'] == 1]
    print("fail", fail.shape[0])
    X = X.loc[X['failure'] == 0]

    print(X.shape[0])
    X.drop_duplicates(keep='first', inplace=True)   # removing duplicate value to reduce imbalance
    print(X.shape[0])

    X = pd.concat([X, fail])

    Y = X['failure']
    X.drop('failure', axis=1, inplace=True)

    from imblearn.over_sampling import SMOTE  # smote sampling for data balancing 
    smt = SMOTE()
    X, Y = smt.fit_sample(X, Y)

    from sklearn import tree
    clf = tree.DecisionTreeClassifier()  # using decision tree classifer 
    clf = clf.fit(X, Y)

    x = pd.read_csv('./predict/'+model_name+'.csv')  # READ  test data 
    searial_num = x['serial_number']
    x.drop('serial_number', axis=1, inplace=True) 
    try:
        y = x['failure']
        x.drop('failure', axis=1, inplace=True)  # select failure data from test if it is available # for score and confuion matrix 
        print(y.value_counts())
    except:
        print("No coloumn failure in the test file")    
    if (x.shape[0]==0):                #check if the model is not in the input file
        return -1
    else:
        val = clf.predict(x)          #predict the output
        try:
            print(clf.score(x, y))
            conf = confusion_matrix(y, val)
            print(conf.item(3))
        except:
            print('there is no Class name to check accuracy')
        try:
            count=(val == 1).sum()  #count the failure numbers from the predicted output
            print(count)
            x['failure']=val        # combine with input
            x['serial_number']=searial_num
            x.to_csv( "./static/result.csv", index=False, encoding='utf-8-sig')  #save in result file for the user for downloading analysis file 
            if(count==0):
                return 0
            else:
                return count   #return the count for showing on we app 
        except:
            print('Error occured')
            

def predict_all():  #if user choose all mode 
        model_names=os.listdir("data")
        fail_count=0
        for model in model_names:  # for each model it perform prediction
            fail_count=fail_count+predict_new(model,model[:-4])    # add the failure count of each model 
        return fail_count          

    
