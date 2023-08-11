# Sleep Healthy (Still working on it)

## How to sleep better?

In this data analysis, I'll dive into the healthy area, specifically about sleep. Os parâmetros contidos nessa base de dados são:

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
    
## Passo 2: Limpeza dos dados
Checking if there's NaN (Not a Number) values 

    sleep_df.isna().sum()
