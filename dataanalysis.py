# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 23:12:01 2018

@author: srinivasarao
"""
import numpy as np
import pandas as pd
filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df= pd.read_csv(filename, names= headers)

print (df.head())

df.replace("?",np.nan,inplace= True)

print (df.head())

missing_data= df.isnull()
print (missing_data.head())

for column in missing_data.columns.values.tolist():
    print (column)
    print (missing_data[column].value_counts())
    print (" ")

avg_1= df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan,avg_1,inplace= True)

print (df["noramlized-losses"].ix[0])