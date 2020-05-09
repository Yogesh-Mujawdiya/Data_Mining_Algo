import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def minMax(df,Head):
    x=df[Head]
    scaler=MinMaxScaler(feature_range=(0,1))
    rescaledX=scaler.fit_transform(x)
    x=pd.DataFrame(rescaledX)
    for i,j in zip(Head,x.columns):
        df[i]=list(np.around(np.array(x[j]),2))
    return df

def DataPreProcessing(root,FileName):
    df=pd.read_csv(FileName)
    categorical_cols = list(filter(lambda x:len(df[x].unique())<=10,df.select_dtypes(include='object').columns))
    if len(categorical_cols)>0:
        le = LabelEncoder()
        df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))
    remove_cols = list(filter(lambda x:len(df[x].unique())>10,df.select_dtypes(include='object').columns))
    if len(df[remove_cols[0]].unique())==len(df[remove_cols[0]]):
        remove_cols.remove(remove_cols[0])
    df = df.drop(remove_cols, axis = 1)
    # Head = df.select_dtypes(include='float64','int64').columns
    # df = minMax(df,Head)
    root.filename =  tk.filedialog.asksaveasfilename(initialdir = ".",defaultextension=".csv",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    df.to_csv(root.filename,index=False)