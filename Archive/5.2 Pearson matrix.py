import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv(r'C:\Users\dell\Desktop\2021_ICM_Problem_D_Data\output\data233.csv')

for i in range(5):
    overall_pearson_r = df.corr().iloc[i,i+5]
    print(overall_pearson_r)
