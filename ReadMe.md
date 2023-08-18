# Sleep Healthy
## What is the best way to have a good night's sleep?

## _Stages of Analysis_
[1. Define the Problem](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#1-define-the-problem-%EF%B8%8F-return)

[2. Collect Data](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#2-collect-data-%EF%B8%8F-return)

[3. Data Cleaning and Preprocessing](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#3-data-cleaning-and-preprocessing-%EF%B8%8F-return)

[4. Data Analysis Techniques](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#4-data-analysis-techniques-%EF%B8%8F-return)

[5. Exploratory Data Analysis (EDA) and Interpretation of Results](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#5-exploratory-data-analysis-eda-and-interpretation-of-results-%EF%B8%8F-return)

[6. Conclusion and Recommendations](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#6-conclusion-and-recommendations-%EF%B8%8F-return)

### _1. Define the Problem_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
In this dataset, we aim to analyze variables related to sleep and understand the reasons that make it less healthy, in order to make it better. The variables are:

- Gender
- Age
- Occupation
- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps
- Sleep Disorder


### _2. Collect Data_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
The data was extracted from the file `sleep_healty.xlsx`, from `Kaggle`, availabre at: <https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset>.

### _3. Data Cleaning and Preprocessing_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
Using the library [pandas](https://pandas.pydata.org/docs/) to import and interprete the data:

    import pandas as pd
    
    sleep_df = pd.read_excel('sleep_healthy.xlsx')
    sleep_df.info()
    
Viewing the column information and checking for `NaN` (Not a Number) values.

    sleep_df.info()
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 374 entries, 0 to 373
    Data columns (total 13 columns):
     #   Column                   Non-Null Count  Dtype  
    ---  ------                   --------------  -----  
     0   Person ID                374 non-null    int64  
     1   Gender                   374 non-null    object 
     2   Age                      374 non-null    int64  
     3   Occupation               374 non-null    object 
     4   Sleep Duration           374 non-null    float64
     5   Quality of Sleep         374 non-null    int64  
     6   Physical Activity Level  374 non-null    int64  
     7   Stress Level             374 non-null    int64  
     8   BMI Category             374 non-null    object 
     9   Blood Pressure           374 non-null    object 
     10  Heart Rate               374 non-null    int64  
     11  Daily Steps              374 non-null    int64  
     12  Sleep Disorder           155 non-null    object 
    dtypes: float64(1), int64(7), object(5)
    memory usage: 38.1+ KB
    
    sleep_df.isna().sum()

    Person ID                    0
    Gender                       0
    Age                          0
    Occupation                   0
    Sleep Duration               0
    Quality of Sleep             0
    Physical Activity Level      0
    Stress Level                 0
    BMI Category                 0
    Blood Pressure               0
    Heart Rate                   0
    Daily Steps                  0
    Sleep Disorder             219

As observed, there are `219 NaN` values in the `Sleep Disorder` column. Therefore, it would be interesting to set them to `zero`.

    sleep_df.fillna(0, inplace = True)
    sleep_df.isna().sum()

    Person ID                    0
    Gender                       0
    Age                          0
    Occupation                   0
    Sleep Duration               0
    Quality of Sleep             0
    Physical Activity Level      0
    Stress Level                 0
    BMI Category                 0
    Blood Pressure               0
    Heart Rate                   0
    Daily Steps                  0
    Sleep Disorder               0

    sleep_df.info()

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 374 entries, 0 to 373
    Data columns (total 13 columns):
     #   Column                   Non-Null Count  Dtype  
    ---  ------                   --------------  -----  
     0   Person ID                374 non-null    int64  
     1   Gender                   374 non-null    object 
     2   Age                      374 non-null    int64  
     3   Occupation               374 non-null    object 
     4   Sleep Duration           374 non-null    float64
     5   Quality of Sleep         374 non-null    int64  
     6   Physical Activity Level  374 non-null    int64  
     7   Stress Level             374 non-null    int64  
     8   BMI Category             374 non-null    object 
     9   Blood Pressure           374 non-null    object 
     10  Heart Rate               374 non-null    int64  
     11  Daily Steps              374 non-null    int64  
     12  Sleep Disorder           374 non-null    object 
    dtypes: float64(1), int64(7), object(5)
    memory usage: 38.1+ KB

### _Initial quality of sleep_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)

    initial_sleep_quality = sleep_df['Quality of Sleep'].mean()
    print(f'{initial_sleep_quality:.3f}')
    7.313

The initial quality of sleep is `7.313`.

### _4. Data Analysis Techniques_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
It will be used `Pearson's correlation matrix` for numerical correlations and `Density Heatmap` for a visual analysis.

### _5. Exploratory Data Analysis (EDA) and Interpretation of Results_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
A good metric to analyse correlations between columns is the `Pearson's Correlation`, Where these relationships range from -1 to +1. This way, it's possible to analyze how much one variable influences another, positively or negatively, where values close to the extremes signify a strong relationship. It's worth noting that this can only be used with numerical data (integers or floats). Therefore, the 'object' columns should be separated from the numerical ones. Below, a dataframe containing only the numerical variables has been created: `Age`, `Sleep Duration`, `Quality of Sleep`, `Physical Activity Level`, `Stress Level`, `Heart Rate` and `Daily Steps`.

        sleep_number = sleep_df[['Age','Sleep Duration','Quality of Sleep','Physical Activity Level','Stress Level','Heart Rate','Daily Steps']]
        correlation = sleep_number.corr()
        sns.heatmap(correlation, annot = True, fmt = '.2f', vmax = +1, vmin = -1, cmap = "RdBu_r")

![Pearson_Correlation](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/10482bf4-a374-4332-9872-dfd84c98f0d3)

As can be observed, that are `strong correlations` with `Quality of Sleep`: 

- `-0.66` with `Heart Rate`
- `-0.90` with `Stress Level`
- `+0.88` with `Sleep Duration`

This means that, biased in a statistical analysis, the higher the heart rate, the worse the sleep quality (inversely proportional), just as the higher the stress level, the lower the sleep quality will be. On the other hand, the longer the duration of sleep, the better it will be.

### _Graphical analysis_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
We observed that there are three numerical variables that have a correlation with sleep quality. A graphical analysis of these variables reinforces the idea of Pearson correlation. For this, the `.density_heatmap` plot, by [plotly.express](https://plotly.com/python/), was utilized.

**_Quality of Sleep x Heart Rate_** 

        graphic = px.density_heatmap(sleep_df, x = 'Heart Rate', y = 'Quality of Sleep')
        graphic.show()
![Quality x Heart Rate](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/dd995fac-006c-4bd4-8d4f-9b4cbf01e118)

As expected, there is an indirect  relationship between the variables, where higher sleep quality values are associeted with the lower heart rate values, with the highest concentration for values below 75.

**_Quality of Sleep x Stress Level_** 

        graphic = px.density_heatmap(sleep_df, x = 'Stress Level', y = 'Quality of Sleep')
        graphic.show()
![Quality x Stress](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/2c5339b3-5e94-4965-8769-184ba34cee0a)
As expected, similarly with the previous graphic, as the stress level increases, There is a deterioration in sleep quality. So, they are inversely related.

**_Quality of Sleep x Sleep Duration_** 

        graphic = px.density_heatmap(sleep_df, x = 'Sleep Duration', y = 'Quality of Sleep')
        graphic.show()
![Quality x Sleep Duration](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/9da68021-dc72-4fea-9ed4-e97f116fbe5f)
In contrast to the previous graphs, as the sleep duration increases, its quality improves.

With this analysis of the numerical variables, several conclusions can be drawn:

- High heart rate is detrimental to sleep
- A high stress level hinders sleep quality
- Sleeping for longer durations contributes to better sleep quality
- Variables like `Age`, `Physical Activity Level` and `Daily Steps` are not significant.

### _Improving the quality of sleep_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)

s we've observed, there are certain factors that have a more significant impact on healthy sleep: `Heart Rate`, `Stress Level` and `Sleep Duration`. Following the graphical analysis, a few points can be highlighted:

- Value `less than or equal` to `71` are desirable for `Heart Rate`
- Value `less than or equal` to `6` are desirable for `Stress Level`
- Value `greater than or equal` to `7` are desirable for `Sleep Duration`

So, making these adjustments to calculate a new average:

    sleep_df = sleep_df[(sleep_df['Heart Rate'] <= 71) & (sleep_df['Stress Level'] <= 6) & (sleep_df['Sleep Duration'] >= 7)]
    new_sleep_quality = sleep_df['Quality of Sleep'].mean()
    print(f'{new_sleep_quality:.3f}')
    8.171

The new average sleep quality is `8.171`, which is `11.73%` higher than the initial average. 

### _Evaluating correlations between non-numerical variables_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)

The non-numerical variables are: `BMI Category`, `Gender`, `Occupation`, `Blood Pressure` and `Sleep Disorder`. The average sleep quality was calculated for each unique value of each variable to analyze if there is any correlation with sleep quality. The obtained results are as follows:

    variable_not_numerical_df = sleep_df[['BMI Category', 'Gender', 'Occupation', 'Blood Pressure', 'Sleep Disorder']]

    for variable in variable_not_numerical_df.columns:
        variable_not_numerical = sleep_df.groupby(variable)['Quality of Sleep'].mean().sort_values(ascending = False)
        print(variable_not_numerical)

### _BMI Category_

    Normal           7.661538
    Normal Weight    7.428571
    Overweight       6.898649
    Obese            6.400000

Individuals who are overweight tend to have lower sleep quality compared to those with a healthy weight.

### _Gender_

    Female    7.664865
    Male      6.968254

In general, women tend to have better sleep quality.

### _Occupation_

    Engineer                8.412698
    Lawyer                  7.893617
    Accountant              7.891892
    Nurse                   7.369863
    Manager                 7.000000
    Teacher                 6.975000
    Doctor                  6.647887
    Software Engineer       6.500000
    Salesperson             6.000000
    Scientist               5.000000
    Sales Representative    4.000000

In this study, the top 3 professions with the best sleep quality are: `Engineer`, `Lawyer` and `Accountant`.

### _Blood Pressure_
    118/75    9.000000
    139/91    9.000000
    115/78    9.000000
    115/75    8.000000
    118/76    8.000000
    119/77    8.000000
    121/79    8.000000
    122/80    8.000000
    125/80    7.661538
    140/95    7.523077
    130/85    7.242424
    120/80    7.022222
    135/90    7.000000
    135/88    7.000000
    128/84    7.000000
    125/82    7.000000
    117/76    7.000000
    142/92    7.000000
    128/85    6.333333
    126/83    6.000000
    129/84    5.000000
    130/86    5.000000
    132/87    5.000000
    140/90    4.500000
    131/86    4.000000

In general, individuals with lower systolic blood pressure values (around 125 or less) and lower diastolic blood pressure values (around 80 or less) tend to have better sleep quality.

### _Sleep Disorder_
    Sleep Apnea    7.205128
    Insomnia       6.532468

Individuals who experience insomnia are more likely to have lower sleep quality compared to those with sleep apnea.

### _6. Conclusion and Recommendations_ [⬆️ Return](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty#stages-of-analysis)
Based on the analyses conducted, some recommendations can be made:

- Avoid smoking and alcohol consumption, as well as being cautious with medication use, to manage heart rate and blood pressure.
- Aim for at least 7 hours of sleep per night.
- Reduce stress levels by adopting a healthy diet, engaging in regular physical activity, practicing meditation, allocating time for enjoyable activities, and ensuring longer sleep durations.
- Establish regular sleep schedules, avoid caffeine-containing drinks in the evening, have light meals for dinner, and limit daytime napping to prevent insomnia.

These are the key areas to focus on for improving sleep quality.


