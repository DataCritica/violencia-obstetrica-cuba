"""
Function to save dataframe as excel

df: dataframe
folder: directory name
filename: file's name
sheet_name: sheet's name
"""
def save_excel(df, folder=None, filename=None, sheet_name=None):
    df.to_excel(f'{folder}/{filename}.xlsx', index=False, sheet_name=sheet_name)

"""
Function to save dataframe as JSON 

folder: directory name
filename: file's name
orient: format of the JSON string (index as default)
"""
def save_json(df, folder=None, filename=None, orient='index'):
    df.to_json(f'{folder}/{filename}.json', orient=orient, force_ascii=False)

"""
Function to save map as html

map: folium object
folder: directory name
filename: file's name
"""
def save_map(map, folder=None, filename=None):
    map.save(f'{folder}/{filename}.html')