from math import sqrt
import altair as alt
import folium
from folium import plugins
from folium.features import FeatureGroup

LONG=22.037635528256533
LAT= -79.36879425670136

# Create a map at specified location
m = folium.Map(location=[LONG, LAT], zoom_start=7, 
               tiles=None)