import pandas as pd
import seaborn as sns
from scipy.cluster import hierarchy
from scipy import cluster   
import matplotlib.pyplot as p
from sklearn import decomposition as skldec

df = pd.read_excel(r"C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\ex.xlsx",index_col=0)

sns.clustermap(df,method ='ward',metric='euclidean')
