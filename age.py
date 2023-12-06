# -*- coding: utf-8 -*-
"""
4、奥运会已经进入90后的天下了？

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') 


import os
os.chdir('./')


df = pd.read_excel('./olympic.xlsx')
df_length = len(df)
df_columns = df.columns.tolist()




data = df[['event','name','birthday']]
data.dropna(inplace = True)   


data.index = pd.to_datetime(data['birthday'])  
data['birthyear'] = data.index.year
data['age'] = 2016 - data['birthyear']
data['age_range'] = pd.cut(data['age'],
                          [0,26,60],           
                          labels=["90s", "not 90s"])  

sns.set_style("ticks")  
g = sns.FacetGrid(data, col="event", hue = 'age_range',palette="Set2_r",
                  height=2.5,   
                  aspect=1.2,
                 col_wrap=3,sharex=False,
                xlim=[15,40], ylim=[0,14]) 


g.map(sns.stripplot,"age",jitter=True,
     size = 10, edgecolor = 'w',linewidth=1,marker = 'o')
g.add_legend()  
plt.savefig('age.png',dpi=400)

