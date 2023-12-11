import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv(r'C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\time sequence\data.csv',encoding='utf-8-sig')

year=[]
for i in range(1944,2021):
    year.append(i)
df.index=pd.Series(year)

def crosscorr(datax, datay, lag=0, wrap=False):
    if wrap:
        shiftedy = datay.shift(lag)
        shiftedy.iloc[:lag] = datay.iloc[-lag:].values
        return datax.corr(shiftedy)
    else: 
        return datax.corr(datay.shift(lag))

# 滑动窗口时间滞后互相关
seconds = 5
fps = 30
window_size = 20 #样本
t_start = 1944
t_end = t_start + window_size
step_size = 1
rss=[]
while t_end < 2021:
    d1 = df['R&B'].loc[t_start:t_end]
    d2 = df['Jazz'].loc[t_start:t_end]
    rs=[]
    for lag in range(-10,10):
        rs.append(d1.corr(d2.shift(lag)))
    rss.append(rs)
    t_start = t_start + step_size
    t_end = t_end + step_size
rss = pd.DataFrame(rss)

f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(rss,cmap='RdBu_r',ax=ax)
ax.set(title=f'Rolling Windowed Time Lagged Cross Correlation',xlim=[0,20], xlabel='Offset',ylabel='Epochs')
ax.set_xticklabels([int(item-10) for item in ax.get_xticks()])
ax.set_yticklabels([item for item in range(1944,2001,2)],rotation=0)
plt.show()