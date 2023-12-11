from dtw import dtw,accelerated_dtw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv(r'C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\time sequence\data.csv',encoding='utf-8-sig')

'''year=[]
for i in range(1947,2021):
    year.append(i)
df.index=pd.Series(year)'''

d1 = df['S1'].interpolate().values
d2 = df['S2'].interpolate().values
d, cost_matrix, acc_cost_matrix, path = accelerated_dtw(d1,d2, dist='euclidean')

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='RdBu_r', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.xlabel('Popularity of Electronic')
plt.ylabel('Acoustics of Electronic')
plt.title(f'DTW Minimum Path with minimum distance: {np.round(d,2)}')
plt.show()
