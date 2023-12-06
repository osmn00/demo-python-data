# -*- coding: utf-8 -*-
"""
身高越高越容易参加奥运吗?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

import os
os.chdir('./')

df = pd.read_excel('./olympic.xlsx', header=0)
df_length = len(df)
df_columns = df.columns.tolist()

data = df[['event','name','gender','height']]
data.dropna(inplace = True)
data_male = data[data['gender'] == '男']
data_female = data[data['gender'] == '女']

hmean_male = data_male['height'].mean()
hmean_female = data_female['height'].mean()

sns.set_style("ticks")

plt.figure(figsize = (8,4))
sns.distplot(data_male['height'],hist = False,kde = True,rug = True,
             rug_kws = {'color':'y','lw':2,'alpha':0.5,'height':0.1},
             kde_kws={"color": "y", "lw": 1.5, 'linestyle':'--'},
             label = 'male_height')
sns.distplot(data_female['height'],hist = False,kde = True,rug = True,
             rug_kws = {'color':'g','lw':2,'alpha':0.5},
             kde_kws={"color": "g", "lw": 1.5, 'linestyle':'--'},
             label = 'female_height')

plt.axvline(hmean_male,color='y',linestyle=":",alpha=0.8)
plt.text(hmean_male+2,0.005,'male_height_mean: %.1fcm' % (hmean_male), color = 'y')
# 绘制男运动员平均身高辅助线

plt.axvline(hmean_female,color='g',linestyle=":",alpha=0.8)
plt.text(hmean_female+2,0.008,'female_height_mean: %.1fcm' % (hmean_female), color = 'g')
# 绘制女运动员平均身高辅助线

plt.ylim([0,0.03])
plt.grid(linestyle = '--')
plt.title("Athlete's height")

plt.savefig('height.png',dpi=400)