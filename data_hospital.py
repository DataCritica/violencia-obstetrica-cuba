import pandas as pd

# Read 'xlsx' files as dataframes
df1 = pd.read_excel(r'data/cruce7_a-bis.xlsx', converters={'Hospital':str}, index_col=None)
df2 = pd.read_excel(r'data/cruce7_b-bis.xlsx', converters={'Hospital':str}, index_col=None)
df3 = pd.read_excel(r'data/cruce7_c-bis.xlsx', converters={'Hospital':str}, index_col=None)

df2


# Remove '\n' from column 'Hospital'
df1['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df2['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
#df3['Hospital'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)


# Merge dataframes by a column
df_join = pd.merge(df1, df2, on ='Hospital', how ='left')

df_join

#df_join = pd.merge(df_join, df3, on ='Hospital', how ='left')
#df_join


# Save dataframe as 'xlsx'
df_join.to_excel(f'data/data_hospital.xlsx', index = False)
