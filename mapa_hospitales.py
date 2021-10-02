import folium
# from folium.features import CustomIcon
import pandas as pd

df = pd.read_excel(r'data/data_hospital.xlsx', index_col=None)

df

m = folium.Map(location=[22.037635528256533, -79.36879425670136], zoom_start=7, tiles="Stamen Toner", attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
# Add another layer
#folium.TileLayer(tiles='Stamen Toner Labels').add_to(m)

# Custom icon image
# icon_image = "assets/hospital.png"
# icon = CustomIcon(
#     icon_image,
#     icon_size=(50, 50),
#     icon_anchor=(20, 10),
#     popup_anchor=(-3, -76),
# )

# help(folium.Icon)
# https://github.com/python-visualization/folium/issues/617
for i, r in df.iterrows():
    folium.Marker([r['Long'], r['Lat']],
    popup=r['Hospital'],
    icon=folium.Icon(icon_color='white', color='red')).add_to(m)

for i, r in df.iterrows():
    folium.vector_layers.CircleMarker(location=[r['Long'], r['Lat']],  radius=r['Total']/10000, color='#3186cc', fill_color='#3186cc').add_to(m)



# Custom tooltip message
tooltip = "¡Haz click!"

# Add markers
folium.Marker([19.435011442107704, -99.13265026035839], icon=icon, popup="<b>Parque República de Guatemala</b>", tooltip=tooltip).add_to(m)

# Save as 'html'
m.save("hospitales_cuba_copy.html")
