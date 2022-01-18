"""
Function to remove whitespaces and new lines
at the beginning in a specified dataframe column

args: dataframes
col_name: column name to clean
return: list of dataframes
"""
def clean_dataframe(*args, col_name=None):
    dfs = list(args)
    for i in range(len(dfs)):
        dfs[i] = dfs[i][col_name].replace(r'^\s*|\n*', '', regex=True, inplace=True)
    return dfs