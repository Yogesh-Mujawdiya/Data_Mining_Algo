import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from Data.forms import ClassificationForm

def KNN_Classification(Train_Data_File,Test_Data_File,Label_Name,K=5):
    Train_df = pd.read_csv(Train_Data_File)
    Test_df = pd.read_csv(Test_Data_File)
    if Label_Name not in Train_df.columns:
        return -1
    Head = list(filter(lambda x:not x in Test_df.columns and x !=Label_Name,Train_df.columns))
    x_train = Train_df[Head].values
    y_train = Train_df[Label_Name].values
    x_test = Test_df[Head].values
    knn = KNeighborsRegressor(K)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    y_pred = list(map(round,y_pred))
    Test_df[Label_Name]=y_pred
    return Test_df

def KNN_Classification_Accuracy(Data_File,Label_Name,K):
    df = pd.read_csv(Data_File)
    if Label_Name not in df.columns:
        return -1
    Head = list(filter(lambda x:x !=Label_Name and len(df[x].unique())!=len(df),df.columns))
    X = df[Head].values
    Y = df[Label_Name].values
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=4)
    knn = KNeighborsRegressor(K)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    y_pred = list(map(round,y_pred))
    c=0
    for i,j in zip(y_pred,y_test):
        if int(i)!=j:
            c+=1
    return 100-c*100//len(y_test)
