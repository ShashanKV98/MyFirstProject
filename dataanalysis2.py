# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:15:24 2018

@author: srinivasarao
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
path='https://ibm.box.com/shared/static/q6iiqb1pd7wo8r3q28jvgsrprzezjqk3.csv'

df = pd.read_csv(path)

print (df.head())

print (df.dtypes)

sns.regplot(x="engine-size",y="price",data=df)
plt.ylim(0,)
