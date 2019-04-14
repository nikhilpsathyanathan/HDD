
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import os
def predict(model):
    X = pd.read_csv('./data/'+model+'.csv')
    fail = X.loc[X['failure'] == 1]
    print("fail", fail.shape[0])
    X = X.loc[X['failure'] == 0]

    print(X.shape[0])
    X.drop_duplicates(keep='first', inplace=True)
    print(X.shape[0])

    X = pd.concat([X, fail])

    Y = X['failure']
    X.drop('failure', axis=1, inplace=True)
    from imblearn.over_sampling import SMOTE
    smt = SMOTE()
    X, Y = smt.fit_sample(X, Y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.33, random_state=42)
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    val = clf.predict(X_test)
    print(confusion_matrix(y_test, val))
    score=clf.score(X_test, y_test)
    print(clf.score(X_test, y_test))
    conf = confusion_matrix(y_test, val)
    print(conf.item(3))
    return str(format(score*100, '.2f'))


def predict_new(file_name,model_name):
    X = pd.read_csv('./data/'+model_name+'.csv')
    fail = X.loc[X['failure'] == 1]
    print("fail", fail.shape[0])
    X = X.loc[X['failure'] == 0]

    print(X.shape[0])
    X.drop_duplicates(keep='first', inplace=True)
    print(X.shape[0])

    X = pd.concat([X, fail])

    Y = X['failure']
    X.drop('failure', axis=1, inplace=True)

    from imblearn.over_sampling import SMOTE
    smt = SMOTE()
    X, Y = smt.fit_sample(X, Y)

    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    x = pd.read_csv('./predict/'+model_name+'.csv')
    y = x['failure']
    x.drop('failure', axis=1, inplace=True)
    print(y.value_counts())
    if (x.shape[0]==0):
        return -1
    else:
        val = clf.predict(x)
        try:
            print(confusion_matrix(y, val))
            print(clf.score(x, y))
            conf = confusion_matrix(y, val)
            print(conf.item(3))
        except:
            print('there is no Class name to check accuracy')
        try:
            count=(val == 1).sum()
            print(count)
            x['failure']=val
            x.to_csv( "./static/result.csv", index=False, encoding='utf-8-sig')
            if(count==0):
                return 0
            else:
                return count
        except:
            print('Error occured')
            

def predict_all():
        model_names=os.listdir("data")
        fail_count=0;
        for model in model_names:
            fail_count=fail_count+predict_new(model,model[:-4])    
        return fail_count          

    
