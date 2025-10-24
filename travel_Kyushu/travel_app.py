import folium

# Kyushu main destinations
stops = [
    {"city": "Yanagawa", "lat": 33.1667, "lon": 130.4000},
    {"city": "Aso", "lat": 32.9500, "lon": 131.0833},
    {"city": "Kurokawa Onsen", "lat": 33.1000, "lon": 131.1500},
    {"city": "Beppu", "lat": 33.2833, "lon": 131.5000},
    {"city": "Nagasaki", "lat": 32.7500, "lon": 129.8667},
]

m = folium.Map(location=[33.0, 131.0], zoom_start=7)

# Add markers
for s in stops:
    folium.Marker(
        [s["lat"], s["lon"]],
        popup=s["city"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Connect route
points = [(s["lat"], s["lon"]) for s in stops]
folium.PolyLine(points, color="black", weight=2.5).add_to(m)

# Save map
m.save("kyushu_trip_map.html")
print("✅ Map generated: kyushu_trip_map.html")
