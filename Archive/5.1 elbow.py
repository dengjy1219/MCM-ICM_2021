import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
from kneed import KneeLocator

style.use('seaborn-whitegrid')

df = pd.read_csv(r'C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\time sequence\data.csv',encoding='utf-8-sig')
x=np.array(df['S1'])
y=np.array(df['S2'])

kneedle = KneeLocator(x,y,10,curve='convex',direction='increasing',online=True)
 
fig, axe = plt.subplots(figsize=[8, 4])
 
axe.plot(x, y, linestyle='-',color='salmon')
axe.set_title('Knee Point Detection (sensitivity=10)')
axe.scatter(x=list(kneedle.all_knees), y=[y[item-1921] for item in list(kneedle.all_knees)], c='cornflowerblue', s=50, marker='H', alpha=1)
#axe.fill_between(np.arange(1955,1970,1),y[34:49],0,alpha=0.3,color='cornflowerblue')
#axe.fill_between(np.arange(2000,2011,1),y[79:90],0,alpha=0.3,color='cornflowerblue')
axe.set_ylim(0,75)
axe.set_xlim(1920,2020)
plt.xlabel('year',fontsize=12)
plt.ylabel('Popularity of Pop/Rock',fontsize=12)