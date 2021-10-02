import pandas as pd

# Read 'xlsx' files as dataframes
df1 = pd.read_excel(r'data/maltrato1_hos.xlsx', converters={'Hospital':str}, index_col=None)
df2 = pd.read_excel(r'data/maltrato2_hos.xlsx', converters={'Hospital':str}, index_col=None)
df3 = pd.read_excel(r'data/maltrato3_hos.xlsx', converters={'Hospital':str}, index_col=None)
df4 = pd.read_excel(r'data/maltrato4_hos.xlsx', converters={'Hospital':str}, index_col=None)
df5 = pd.read_excel(r'data/maltrato5_hos.xlsx', converters={'Hospital':str}, index_col=None)
df6 = pd.read_excel(r'data/maltrato6_hos.xlsx', converters={'Hospital':str}, index_col=None)
df7 = pd.read_excel(r'data/maltrato7_hos.xlsx', converters={'Hospital':str}, index_col=None)
df8 = pd.read_excel(r'data/maltrato8_hos.xlsx', converters={'Hospital':str}, index_col=None)
df9 = pd.read_excel(r'data/maltrato9_hos.xlsx', converters={'Hospital':str}, index_col=None)
df10 = pd.read_excel(r'data/maltrato10_hos.xlsx', converters={'Hospital':str}, index_col=None)
df10


# Remove '\n' from column 'Hospital'
df1['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df2['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df3['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df4['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df5['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df6['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df7['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df8['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df9['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)
df10['Hospital'].replace(r'\\n|^\s', '', regex=True, inplace=True)

# Merge dataframes by a column
df_join = pd.merge(df1, df2, on ='Hospital', how ='left')

df_join

df_join = pd.merge(df_join, df3, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df4, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df5, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df6, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df7, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df8, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df9, on ='Hospital', how ='left')
df_join = pd.merge(df_join, df10, on ='Hospital', how ='left')
df_join

# Create a column with rows sum
df_join.loc[:, 'Total'] = df_join.sum(axis=1)
df_join

# Save dataframe as 'xlsx'
df_join.to_excel(f'data/data_hospital.xlsx', index = False)
