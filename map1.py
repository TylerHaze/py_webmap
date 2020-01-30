import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

volcanoe_name = df["NAME"]

volcanoe_lat = list(df["LAT"])
volcanoe_lon = list(df["LON"])
elev = list(df["ELEV"])

map = folium.Map(location=(38.85, -99.09), zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(volcanoe_lat, volcanoe_lon, elev):
    if el < 1000:
        color = 'red'
    elif el <= 3000:
        color = 'gray'
    else:
        color = 'green'
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=color)))

map.add_child(fg)

map.save("Map1.html")