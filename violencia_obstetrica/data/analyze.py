import pandas as pd

"""
Function to create a simple pivot table

df: dataframe
values: values
index: index
cols: columns
func: function (count as default)
return: pivot table
"""
def create_pivot_tabe(df, values=None, index=None, cols=None, func='count'):
    list_cols = df.columns
    table = pd.pivot_table(df, values=list_cols[values], index=list_cols[index],
            columns=list_cols[cols], aggfunc=func)
    return table

"""
Function to create pivot tables for several columns

df: dataframe
values: set values
index: set index
cols: list with columns by index 
func: function (count as default)
return: list of pivot tables
"""
def create_complex_pivot_table(df, values=None, index=None, cols=list, func='count'):
    tables = []
    list_cols = df.columns
    count = len(cols)
    for i in range(count):
        table = pd.pivot_table(df, values=list_cols[values], index=list_cols[index],
                columns=list_cols[cols[i]], aggfunc=func)
        tables.append(table)
    return tables

"""
Function to create pivot tables for several columns and indexes

df: dataframe
values: set values
index: list with indexes 
cols: list with columns by index 
func: function (count as default)
return: list of pivot tables
"""
def create_vcomplex_pivot_table(df, values=None, index=list, cols=list, func='count'):
    tables = []
    list_cols = df.columns
    count_cols = len(cols)
    count_index = len(index)
    for i in range(count_cols):
        for j in range(count_index):
            table = pd.pivot_table(df, values=list_cols[values], index=list_cols[index[j]],
                    columns=list_cols[cols[i]], aggfunc=func)
            tables.append(table)
    return tables

"""
Function to convert a dataframe index
to column, rename it and reset index

args: dataframes
col_name: new column name
return: list of dataframes
"""
def set_new_index(*args, col_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i] = dfs[i].rename_axis(col_name).reset_index().rename_axis('', axis=1)
    return dfs

"""
Function to delete a column

args: dataframes
col_name: name of the column to remove
return: list of dataframes
"""
def del_col(*args, col_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i].drop(col_name, axis=1, inplace=True)
    return dfs

"""
Function to delete a row

args: dataframes
row_name: index of the row to remove
return: list of dataframes
"""
def del_row(*args, row_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i].drop(row_name, axis=0, inplace=True)
        dfs[i].reset_index(drop=True)
    return dfs

"""
Function to replace a value

args: dataframes
col_name: name of the column with the values
old_val: old value
new_val: new value
return: list of dataframes
"""
def replace_value(*args, col_name=None, old_val=None, new_val=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i].replace({f'{col_name}': {old_val: new_val}}, inplace=True)
    return dfs

"""
Function to rename a column, drop NaN values and reset index

args: dataframes
old_col: name of the column to rename
new_col: new column's name
return: list of dataframes
"""

def prepare_table(*args, old_col=None, new_col=None):
    tables = list(args)
    for i in range(len(tables)):
        if len(tables) == 1:
            tables[i] = tables[i].rename(columns={old_col: f'{new_col}'})
            tables[i].dropna(subset=[f'{new_col}'], inplace=True)
        else:
            tables[i] = tables[i].rename(columns={old_col: f'{new_col}{i+1}'})
            tables[i].dropna(subset=[f'{new_col}{i+1}'], inplace=True)
        tables[i] = tables[i].reset_index(drop=True)
    return tables

"""
Function to sum up rows values

args: dataframes
col_name: name of the column with sum values
"""
def sum_rows(*args, col_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i][f'{col_name}{i+1}'] = dfs[i].sum(axis=1, numeric_only=True)
    return dfs


"""
Function to drop rows with zero values on a column

args: dataframes
col_name: column name to check for values
return: list of dataframes
"""
def drop_zeros(*args, col_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        if len(dfs) == 1:
            dfs[i].drop(dfs[i].loc[dfs[i][col_name] == 0].index, inplace=True)
        else:
            dfs[i].drop(dfs[i].loc[dfs[i][f'{col_name}{i+1}'] == 0].index, inplace=True)
    return dfs

"""
Function to drop NaN values and reset index

df: dataframe
col_name: column's name to remove NaN values
return: dataframe
"""
def drop_nan(df, col_name=None):
    df.dropna(subset=[col_name], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

"""
Function to filter columns and reset index

args: dataframes
items: list of column names
return: list of dataframes
"""
def filter_cols(*args, items=None, regex=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i] = dfs[i].filter(regex=regex, axis=1)
        dfs[i].reset_index(drop=True, inplace=True)
    return dfs

"""
Function to merge dataframes

args: dataframes
col_name: column or index level names to join on
how: type of merge to be performed (outer as default)
return: dataframe
"""
def merge_dataframes(*args, col_name=None, how='outer'):
    dfs = list(args)
    for i in range(len(dfs)):
        if i <= 1:
            df = pd.merge(dfs[0], dfs[1], on=col_name, how=how)
        else:
            df = pd.merge(df, dfs[i], on=col_name, how=how)
    return df

"""
Function to sort dataframes according to index

df: dataframes
index: list with indexes 
return: list of dataframes
"""
def sort_by_index(df, index=list):
    df_sorted = [list() for x in index]
    for i in range(len(index)):
        for j in range(i, len(df), len(index)):
            df_sorted[i].append(df[j])
    return df_sorted