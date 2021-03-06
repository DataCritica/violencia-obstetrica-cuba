"""
Function to save dataframe as excel

df: dataframe
folder: directory name
filename: file's name
sheet_name: sheet's name
"""
def save_excel(df, folder=None, file=None, sheet_name=None):
    df.to_excel(f'{folder}/{file}.xlsx', index=False, sheet_name=sheet_name)

"""
Function to save dataframe as JSON 

folder: directory name
filename: file's name
orient: format of the JSON string (index as default)
"""
def save_json(df, folder=None, file=None, orient='index'):
    df.to_json(f'{folder}/{file}.json', orient=orient, force_ascii=False)

"""
Function to save figure

fig: plotly boject
folder: directory name
filename: file's name
"""
def save_fig(fig, folder=None, file=None):
    fig.write_html(f'{folder}/{file}.html')

"""
Function to save map as html

map: folium object
folder: directory name
filename: file's name
"""
def save_map(map, folder=None, file=None):
    map.save(f'{folder}/{file}.html')