import pandas as pd
import seaborn as sns
import plotly.express as px

#Ler a base
sleep_df = pd.read_excel('sleep_healty.xlsx')
sleep_df = sleep_df.dropna()
sleep_df = sleep_df.drop(columns = ['Gender','Occupation','BMI Category','Blood Pressure','Sleep Disorder'], axis = 1)
sleep_df.info()

correlation = sleep_df.corr()
sns.heatmap(correlation, annot = True, fmt = ".1f", vmax = 1, vmin = -1)