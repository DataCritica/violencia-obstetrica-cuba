import pandas as pd

"""
Function to remove 
whitespace and new line
at the beginning in a 
specified dataframe column
"""
def clean_dataframe(*args, col_name='None'):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i] = dfs[i][col_name].replace(r'^\s*|\n*', '', regex=True, inplace=True)
    return dfs

"""
Function to merge dataframes
"""
def merge_dataframes(*args, col_name='None', how='outer'):
    dfs = list(args)
    for i in range(len(dfs)):
        if i <= 1:
            df = pd.merge(dfs[0], dfs[1], on=col_name, how=how)
        else:
            df = pd.merge(df, dfs[i], on=col_name, how=how)
    return df

"""
Function to create a 
simple pivot table
"""
def create_pivot_tabe(df, values=int, index=int, cols=int, func='count'):
    list_cols = df.columns
    table = pd.pivot_table(df, values=list_cols[values], index=list_cols[index],
            columns=list_cols[cols], aggfunc=func)
    return table

"""
Function to create pivot
tables for several columns
"""
def create_complex_pivot_table(df, values=int, index=int, cols=list, func='count'):
    tables = []
    list_cols = df.columns
    count = len(cols)
    for i in range(count):
        table = pd.pivot_table(df, values=list_cols[values], index=list_cols[index],
                columns=list_cols[cols[i]], aggfunc=func)
        tables.append(table)
    return tables

"""
Function to clean
a pivot table
"""
def clean_table(*args, col_name='None'):
    tables = list(args)
    for i in range(len(tables)):
        tables[i] = tables[i].rename_axis(col_name).reset_index().rename_axis('', axis='columns')
    return tables

"""
Function to delete a column,
rename a column, drop their
NaN values and reset index
"""
def process_table(*args, del_col="None", old_col="Old", new_col="New"):
    tables = list(args)
    for i in range(len(tables)):
        # Delete column and rename other column
        tables[i] = tables[i].drop(del_col, 1).rename(columns={old_col: f'{new_col}{i+1}'})
        # Remove rows with NaN values on column
        tables[i].dropna(subset=[f'{new_col}{i+1}'], inplace=True)
        # Reset index
        tables[i] = tables[i].reset_index(drop=True)
    return tables