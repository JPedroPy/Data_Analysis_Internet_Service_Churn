#Importing libraries
import pandas as pd
import seaborn as sns
import plotly.express as px

#Reading dataset and showing informations resume
sleep_df = pd.read_excel('sleep_healthy.xlsx')
sleep_df.info()

#Cleaninng the dataset
sleep_df.isna().sum()

#Filling NaN's with zero
sleep_df.fillna(0, inplace = True)

#Checking
sleep_df.isna().sum()

#Checking
sleep_df.info()

#Initial quality of sleep
initial_sleep_quality = sleep_df['Quality of Sleep'].mean()
print(f'{initial_sleep_quality:.3f}')

#Selecting numerical variables
sleep_number = sleep_df[['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']]

#Using Pearson's correlation 
correlation = sleep_number.corr()
sns.heatmap(correlation, annot = True, fmt = '.2f', vmax = +1, vmin = -1, cmap = "RdBu_r")

#Generating graphic 'Quality of Sleep' x 'Stress Level'
graphic = px.density_heatmap(sleep_df, x = 'Stress Level', y = 'Quality of Sleep', color_continuous_scale = 'teal')
graphic.show()

#Generating graphic 'Quality of Sleep' x 'Heart Rate'
graphic = px.density_heatmap(sleep_df, x = 'Heart Rate', y = 'Quality of Sleep', color_continuous_scale = 'teal')
graphic.show()

#Generating graphic 'Quality of Sleep' x 'Sleep Duration'
graphic = px.density_heatmap(sleep_df, x = 'Sleep Duration', y = 'Quality of Sleep', color_continuous_scale = 'teal')
graphic.show()

#Improving the quality of sleep
sleep_df = sleep_df[(sleep_df['Heart Rate'] <= 71) & (sleep_df['Stress Level'] <= 6) & (sleep_df['Sleep Duration'] >= 7)]
new_sleep_quality = sleep_df['Quality of Sleep'].mean()
print(f'{new_sleep_quality:.3f}')

#Evaluating correlations between non-numerical variables
variable_not_numerical_df = sleep_df[['BMI Category', 'Gender', 'Occupation', 'Blood Pressure', 'Sleep Disorder']]

for variable in variable_not_numerical_df.columns:
    variable_not_numerical = sleep_df.groupby(variable)['Quality of Sleep'].mean().sort_values(ascending = False)
    print(variable_not_numerical)