import pandas as pd

# Read 'xlsx' files as dataframes
df1 = pd.read_excel(r'data/cruce7_a.xlsx', converters={'Año':str}, index_col=None)
df2 = pd.read_excel(r'data/cruce7_b.xlsx', converters={'Año':str}, index_col=None)
#df3 = pd.read_excel(r'data/cruce7_c.xlsx', converters={'Año':str}, index_col=None)

df1
df2

# Merge dataframes by a column
df_join = pd.merge(df1, df2, on ='Año', how ='left')

df_join

# Create a column with rows sum
df_join.loc[:, 'Total'] = df_join.sum(axis=1)

df_join

# Save dataframe as 'xlsx'
df_join.to_excel(f'data/data_año.xlsx', index = False)
