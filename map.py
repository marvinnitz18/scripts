#!/usr/bin/env python3.7
import json
import folium
m = folium.Map(location=[38, 6], tiles='Stamen Toner', zoom_start=2)

coordinates = open("/var/scripts/coordinate.list", "r")
line = coordinates.readline()
user_count= 1
while line:
    line = line.replace('\n','')
    line = eval(line)
    lat = line['lat']
    long = line['long']
    folium.Marker([lat, long], tooltip="User #"+str(user_count)).add_to(m)
    user_count= user_count + 1
    line = coordinates.readline()
coordinates.close()
m.save('/var/www/html/map.html')
