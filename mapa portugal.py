import folium

latitude = 39.3999
longitude = -8.2245

mapaPortugal = folium.Map(location=[latitude, longitude], zoom_start=6)

folium.Marker(
    location=[38.7167, -9.139],
    popup='Lisboa',
    icon=folium.Icon(icon='cloud')
).add_to(mapaPortugal)

folium.Marker(
    location=[41.1579, -8.6291],
    popup='Porto',
    icon=folium.Icon(icon='green')
).add_to(mapaPortugal)

mapaPortugal.save('mapaPortugal.html')

