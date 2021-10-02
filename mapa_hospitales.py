import folium
from folium.features import FeatureGroup
from folium.plugins import MarkerCluster
import pandas as pd
#import math
import altair as alt

# Read 'xlsx' file as pandas dataframe
df = pd.read_excel(r'data/data_hospital.xlsx', converters={'Long':str, 'Lat':str}, index_col=None)
# Remove rows based on a column value
df = df.drop(df['Long'].loc[df['Long']=="0"].index)
df

# Create a map
m = folium.Map(location=[22.037635528256533, -79.36879425670136], zoom_start=7, tiles=None)

# Add layers
# Dark Mode
folium.TileLayer(tiles="CartoDB dark_matter", name="Dark", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>').add_to(m)
# Light Mode
folium.TileLayer(tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', name="Light", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>').add_to(m)

# Add the option to switch tiles
hospitales = FeatureGroup(name="Hospitales")
hospitales.add_to(m)
folium.LayerControl().add_to(m)


# Custom tooltip message
# tooltip = "¡Haz click!"


# help(folium.Icon)
# https://github.com/python-visualization/folium/issues/617
# Custom icon image
# icon_image = "assets/hospital.png"
# icon = CustomIcon(
#     icon_image,
#     icon_size=(50, 50),
#     icon_anchor=(20, 10),
#     popup_anchor=(-3, -76),
# )

# Marker
# for i, r in df.iterrows():
#     folium.Marker([r['Long'], r['Lat']],
#     popup=r['Hospital'],
#     tooltip=r['Hospital'],
#     icon=folium.Icon(icon_color='white', color='red')).add_to(hospitales)

# Circle marker
for i, r in df.iterrows():
    folium.CircleMarker([r['Long'], r['Lat']],
    # radius=math.sqrt(r['Total']),
    radius=r['Total']/3,
    popup=r['Hospital'],
    color='#FFB100',
    fill_color='#FF8900',
    fill_opacity=(0.5),
    tooltip=r['Hospital'],
    icon=folium.Icon(icon_color='white', color='red')).add_to(hospitales)


# Marker Cluster
# marker_cluster = MarkerCluster().add_to(hospitales)
# for i, r in df.iterrows():
#     folium.Marker([r['Long'], r['Lat']],
#     popup=r['Hospital'],
#     icon=folium.Icon(icon_color='white', color='red')).add_to(marker_cluster)


# Save as 'html'
m.save("hospitales_cuba.html")
