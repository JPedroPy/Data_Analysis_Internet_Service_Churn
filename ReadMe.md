# Sleep Healthy
## What is the best way to have a good night's sleep?

## _Stages of Analysis_
[1. Define the problem]()

[2. Collect Data]()

[3. Data Cleaning and Preprocessing]()

[4. Data Analysis Techniques]()

[5. Exploratory Data Analysis (EDA) and Interpretation of Results]()

[6. Conclusion and Recommendations]()

### _1. Define the problem_
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


### _2. Collect Data_
The data was extracted from the file `wine_quality.xlsx`, from `Kaggle`, availabre at: <[https://www.kaggle.com/datasets/yasserh/wine-quality-dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)>.

### _3. Data Cleaning and Preprocessing_
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

As observed, there are `219 NaN` values in the "Sleep Disorder" column. Therefore, it would be interesting to set them to zero.

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

## Qualidade inicial do sono

    initial_sleep_quality = sleep_df['Quality of Sleep'].mean()
    print(f'{initial_sleep_quality:.3f}')
    7.313

A qualidade inicial do sono é `7.313`.

## Passo 3: Avaliando correlações entre variáveis numéricas

Uma boa métrica para analisar as relações entre colunas é a `correlação de Pearson`, onde tal relação varia entre -1 e +1. Assim, pode-se analisar o quanto uma variável influencia na outra, positiva ou negativamente, onde valores próximos aos extremos significam uma forte relação. Vale ressaltar que apenas pode ser usado em dados numéricos (int or float). Então, as colunas "objeto" devem ser separadas das numéricas. Abaixo foi criado um dataframe apenas com as variáveis numéricas: `Age`, `Sleep Duration`, `Quality of Sleep`, `Physical Activity Level`, `Heart Rate` and `Daily Steps`.

        sleep_number = sleep_df[['Age','Sleep Duration','Quality of Sleep','Physical Activity Level','Stress Level','Heart Rate','Daily Steps']]
        correlation = sleep_number.corr()
        sns.heatmap(correlation, annot = True, fmt = '.2f', vmax = +1, vmin = -1, cmap = "RdBu_r")

## Heatmap ##
![Pearson_Correlation](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/10482bf4-a374-4332-9872-dfd84c98f0d3)

Como pode ser visto, há algumas `correlações fortes` com `Quality of Sleep`: 

- `-0.66` com `Heart Rate`
- `-0.90` com `Stress Level`
- `+0.88` com `Sleep Duration`

Isso significa que, enviesado em uma análise estatística, quanto mais alta for a frequência cardíaca, pior será a qualidade do sono (inversamente proporcionais), assim como quanto mais alto for o nível de estresse, haverá redução da qualidade do sono. Em contrapartida, quanto maior for a duração do sono, melhor ele será. 



## Passo 4: Análise gráfica
Vimos que há três variáveis numéricas que possuem correlação com a qualidade do sono. Uma análise gráfica dessas variáveis ajuda, visualmente, a reforçar a ideia da correlação de Pearson. Para isso, foi utilizada o gráfico `.density_heatmap`, by [plotly.express](https://plotly.com/python/).

## 1. Quality of Sleep x Heart Rate 
        graphic = px.density_heatmap(sleep_df, x = 'Heart Rate', y = 'Quality of Sleep')
        graphic.show()
![Quality x Heart Rate](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/dd995fac-006c-4bd4-8d4f-9b4cbf01e118)
Como esperado, há uma relação indireta entre as variáveis, onde os maiores valores de qualidade do sono são relacionados com os menores valores de frequência cardíaca, sendo a maior concentração para valores `abaixo de 75`.
## 2. Quality of Sleep x Stress Level
        graphic = px.density_heatmap(sleep_df, x = 'Stress Level', y = 'Quality of Sleep')
        graphic.show()
![Quality x Stress](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/2c5339b3-5e94-4965-8769-184ba34cee0a)
Como imaginado, de modo similar à análise anterior, conforme aumenta o nível de estresse, há piora na qualidade do sono, ou seja, são relacionados de modo inverso.
## 3. Quality of Sleep x Sleep Duration
        graphic = px.density_heatmap(sleep_df, x = 'Sleep Duration', y = 'Quality of Sleep')
        graphic.show()
![Quality x Sleep Duration](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/9da68021-dc72-4fea-9ed4-e97f116fbe5f)
Diferentemente dos gráficos anteriores, conforme aumenta a duração do sono, melhor será a qualidade do mesmo. 

Com essa análise das variáveis numéricas, pode-se tirar algumas conclusões:

- Uma alta frequência cardíaca é prejudicial ao sono
- Um elevado nível de estresse atrapalha a qualidade do sono
- Dormir por mais tempo ajuda a ter um sono melhor
- Variables like `Age`, `Physical Activity Level` e `Daily Steps` não são significativos.

## Improving the quality of sleep
Como vimos, há alguns fatores que intererem com mais impacto em um sono saudável: `Heart Rate`, `Stress Level` and `Sleep Duration`. Então, após a análise gráfica, alguns pontos podem ser destacados:

- Valores `menores ou iguais` a `71` são interessantes para `Heart Rate`
- Valores `menores ou iguais` a `6` são interessantes para `Stress Level`
- Valores `maiores ou iguais` a `7` são interessantes para `Sleep Duration`

Então, realizando esses ajustes para obter uma nova média:

    sleep_df = sleep_df[(sleep_df['Heart Rate'] <= 71) & (sleep_df['Stress Level'] <= 6) & (sleep_df['Sleep Duration'] >= 7)]
    new_sleep_quality = sleep_df['Quality of Sleep'].mean()
    print(f'{new_sleep_quality:.3f}')
    8.171

A nova média da qualidade do sono é `8.171`, sendo `11.73%` maior do que a média inicial. 

## Passo 3: Avaliando correlações entre variáveis não numéricas
As variáveis não numéricas são: `BMI Category`, `Gender`, `Occupation`, `Blood Pressure` and `Sleep Disorder`. Cada variável teve a sua média da qualidade do sono calculada para cada valor diferente, de modo a analisar se há alguma correlação com a qualidade do sono. Os resultados obtidos foram:

    variable_not_numerical_df = sleep_df[['BMI Category', 'Gender', 'Occupation', 'Blood Pressure', 'Sleep Disorder']]

    for variable in variable_not_numerical_df.columns:
        variable_not_numerical = sleep_df.groupby(variable)['Quality of Sleep'].mean().sort_values(ascending = False)
        print(variable_not_numerical)

### BMI Category

    Normal           7.661538
    Normal Weight    7.428571
    Overweight       6.898649
    Obese            6.400000

Pessoas que são acima do peso possuem um sono de menor qualidade em relação às que estão com o peso adequado.

### Gender

    Female    7.664865
    Male      6.968254

De maneira geral, as mulheres possuem um sono de melhor qualidade.

### Occupation

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

Nesse estudo, as 3 profissões com a melhor qualidade de sono: `Engineer`, `Lawyer` and `Accountant`.

### Blood Pressure
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

De maneira geral, pessoas que possuem a pressão sistolítica com valores menores (por volta de 125 ou menos) e pressão diastolítica com valores também menores (por volta de 80 ou menos) são as que possuem um sono melhor.

### Sleep Disorder
    Sleep Apnea    7.205128
    Insomnia       6.532468

Pessoas que possuem insônia estão propícias a terem um sono de menor qualidade em relação às que possuem apneia do sono.

## Considerações finais
Então, através das análises feitas, algumas recomendações podem ser feitas:

- Evitar o uso de cigarro e bebidas alcoólicas, assim como atentar-se com relação ao uso de medicamentos, de modo a controlar a frequência cardíaca e a pressão sanguínea.
- Dormir pelo menos 7 horas por noite.
- Diminuir o nível de estresse, adotando uma alimentação saudável, praticando mais exercícios físicos e meditação, reservando um tempo para atividades prazerosas, assim como dormir por mais tempo.
- Adotar horários regulares de sono, evitar bebidas com cafeína à noite, comer alimentos leves no jantar e evitar dormir muito durante o dia, de modo a evitar a insônia.

Esses são os pontos focais no processo da melhoria do sono.


