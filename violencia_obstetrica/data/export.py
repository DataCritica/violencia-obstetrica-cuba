"""
Function to save 
dataframe as excel 
"""
def save_excel(df, folder='None', filename='None', sheet_name='sheet'):
    df.to_excel(f'{folder}/{filename}.xlsx', index=False, sheet_name=sheet_name)

"""
Function to save 
dataframe as json 
"""
def save_json(df, folder='None', filename='None', orient='index'):
    df.to_json(f'{folder}/{filename}.json', orient=orient, force_ascii=False)

"""
Function to save
map as html
"""
def save_map(map, folder='None', filename='None'):
    map.save(f'{folder}/{filename}.html')