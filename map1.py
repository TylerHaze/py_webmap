import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

volcanoe_name = df["NAME"]

volcanoe_lat = list(df["LAT"])
volcanoe_lon = list(df["LON"])
elev = list(df["ELEV"])

map = folium.Map(location=(38.85, -99.09), zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="USA Volcanoes")

for lt, ln, el in zip(volcanoe_lat, volcanoe_lon, elev):
    if el < 1000:
        color = 'red'
    elif el <= 3000:
        color = 'orange'
    else:
        color = 'green'
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=el, fill_color=color, radius=6, fill_opacity=1, color='gray'))

fg2 = folium.FeatureGroup(name="Population Colors")
fg2.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map1.html")