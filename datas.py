import pandas as pd

"""
df is short for dataframe
dataframe: objects which are the rows and cols of our datas
series: a single column
panel: mutltiple dataframes
"""
df = pd.read_csv("avocado.csv")

albany_df = df[df['region']=='Albany']
print(albany_df.head())
