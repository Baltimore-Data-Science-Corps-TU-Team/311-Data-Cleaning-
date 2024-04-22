import folium
import pandas as pd

data = pd.read_csv("311_Customer_Service_Requests_2021.csv")

baltimoredata = data[data['City'] == 'Baltimore']

locations = baltimoredata[['Latitude', 'Longitude']]
otherinfo = baltimoredata[['SRType', 'Address']]

bmoremap = folium.Map(location=[39.2904, -76.6122], zoom_start=11)

for index, row in locations.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=otherinfo.iloc[index]['SRType']).add_to(bmoremap)

bmoremap.save("baltimore_311_call_pins.html")
