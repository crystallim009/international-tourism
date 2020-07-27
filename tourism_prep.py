# combine multiple columns of individual years into single column so that it appears as a single field in tableau

import pandas as pd

df = pd.read_csv("tourism.csv")

df = df.drop(df.columns.to_series()["1960":"1994"], axis=1)                      # delete range of columns at one go

df = df.drop(columns=['2019'])

#df = pd.melt(df, id_vars=['Country Name'], value_vars=['1995':'1996'])      

df = df.set_index(['Country Name']).rename_axis(['Year'], axis=1).unstack().reset_index()

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\projects\tourism\tourism1.csv", encoding='utf-8', index=False)
