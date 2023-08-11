# Sleep Healthy (Still working on it)

## How to sleep better?

In this data analysis, I'll dive into the healthy area, specifically about sleep. As variáveis contidas nessa base de dados são:

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

## Passo 1: Importar as bibliotecas e a base de dados usada
As bibliotecas usadas ao longo dessa análise serão: "pandas", para leitura e tratamento dos dados através de dataframes, "seaborn", matplotlib.pyplot e plotly.express para plotagem de gráficos.

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px

    sleep_df = pd.read_excel('sleep_healthy.xlsx')
    sleep_df.info()
    
## Passo 2: Visualização e limpeza dos dados
Analisando as informações das colunas e Checking if there's NaN (Not a Number) values 

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

Como pode ser visto, há 219 NaN na coluna "Sleep Disorder". Então, é interessante transformá-los em 0 (zero).

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

Agora, com os dados tratados, a análise em si pode ser iniciada.

## Passo 3: Avaliando correlações entre variáveis

Uma boa métrica para analisar as relações entre colunas é a correlação de Pearson, onde tal relação varia entre -1 e +1. Assim, pode-se analisar o quanto uma variável influencia na outra, positiva ou negativamente, onde valores próximos aos extremos significam uma forte relação. Vale ressaltar que apenas pode ser usado em dados numéricos (int or float). Então, as colunas "objeto" devem ser separadas das numéricas. Abaixo foi criado um dataframe apenas com as variáveis numéricas.
  
    sleep_number = sleep_df[['Age','Sleep Duration','Quality of Sleep','Physical Activity Level','Stress Level','Heart Rate','Daily Steps']]
    correlation = sleep_number.corr()
    sns.heatmap(correlation, annot = True, fmt = '.2f', vmax = +1, vmin = -1, cmap = "RdBu_r")

## Heatmap ##
![Pearson_Correlation](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/10482bf4-a374-4332-9872-dfd84c98f0d3)

Como pode ser visto, há algumas correlações fortes com "Quality of Sleep": 

- -0.66 com "Heart Rate"
- -0.90 com "Stress Level"
- +0.88 com "Sleep Duration"

Isso significa que, enviesado em uma análise estatística, quanto mais alta for a frequência cardíaca, pior será a qualidade do sono (inversamente proporcionais), assim como quanto mais alto for o nível de estresse, haverá redução da qualidade do sono. Em contrapartida, quanto maior for a duração do sono, melhor ele será. 

## Passo 4: Análise gráfica
Vimos que há três variáveis numéricas que possuem correlação com a qualidade do sono. Uma análise gráfica dessas variáveis ajuda, visualmente, a reforçar a ideia da correlação de Pearson. Para isso, foi utilizada o gráfico "density_heatmap", do "seaborn".

## 1. Quality of Sleep x Heart Rate 
        graphic = px.density_heatmap(sleep_df, x = 'Heart Rate', y = 'Quality of Sleep')
        graphic.show()
![Quality x Heart Rate](https://github.com/JPedroPy/Data_Analysis_Sleep_Healty/assets/141521444/dd995fac-006c-4bd4-8d4f-9b4cbf01e118)
Como esperado, há uma relação indireta entre as variáveis, onde os maiores valores de qualidade do sono são relacionados com os menores valores de frequência cardíaca, sendo a maior concentração para valores abaixo de 75.
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
- Variáveis como "Age", "Physical Activity Level" e "Daily Steps" não são significativos.



    
