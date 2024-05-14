import folium
import pandas as pd

data = pd.read_csv("cleaned311srtypes.csv")
data = data.head(10000)

locations = data[['Latitude', 'Longitude']]
otherinfo = data[['SRType']]

bmoremap = folium.Map(location=[39.2904, -76.6122], zoom_start=12)

for index, row in locations.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=otherinfo.iloc[index]['SRType']).add_to(bmoremap)

bmoremap.save("baltimore_311_call_pins.html")