# -*- coding: utf-8 -*-
"""
运动员身材都是完美型吗?
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

data = df[['event','name','height','weight']]

event_count = data['event'].value_counts()
event_drop = event_count[event_count<15]

data2 = data[data['event'] != 'swim']
data2.dropna(inplace = True)

data2['BMI'] = data2['weight']/(data2['height']/100)**2
data2['BMI_range'] = pd.cut(data2['BMI'],
                            [0,18.5,24,28,50], 
                            labels=["Thin", "Normal", "Strong",'ExtremelyStrong'])
# 计算运动员BMI指数，并整理出BMI区间值，设置为四挡：低于18.5纤瘦，18.5-23.9适中，24-27强壮，28-32极壮

sns.set_style("ticks")

plt.figure(figsize = (8,4))
sns.violinplot(x="event", y="BMI", data=data2,
               scale = 'count',
               palette = "hls", 
               inner = "quartile")

sns.swarmplot(x="event", y="BMI", data=data2, color="w", alpha=.8,s=2)

plt.grid(linestyle = '--')
plt.title("Athlete's BMI")

plt.savefig('body.png',dpi=400)

data2[data2['BMI']>30]