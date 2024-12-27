!pip install streamlit
!pip install folim
!pip install streamlit_folium
import streamlit as st
import folium
from streamlit_folium import st_folium

# Sample data for tourist attractions in Malaysia with types
tourist_attractions = [
    {"name": "Petronas Twin Towers", "description": "Iconic twin skyscrapers with a skybridge.", "latitude": 3.15785, "longitude": 101.7123, "type": "historical"},
    {"name": "Batu Caves", "description": "Limestone hill with temples and shrines.", "latitude": 3.2379, "longitude": 101.6831, "type": "natural"},
    {"name": "Langkawi Sky Bridge", "description": "Curved pedestrian bridge with scenic views.", "latitude": 6.3810, "longitude": 99.6653, "type": "natural"},
    {"name": "George Town", "description": "Historic city with colonial architecture.", "latitude": 5.4141, "longitude": 100.3288, "type": "historical"},
    {"name": "Mount Kinabalu", "description": "Tallest mountain in Malaysia.", "latitude": 6.0754, "longitude": 116.5584, "type": "natural"}
]

# Create a map centered around Malaysia
map_malaysia = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Create feature groups for different types of attractions
historical_fg = folium.FeatureGroup(name='Historical Sites')
natural_fg = folium.FeatureGroup(name='Natural Wonders')
amusement_fg = folium.FeatureGroup(name='Amusement Parks')

# Add markers for each tourist attraction with different colors based on type
for attraction in tourist_attractions:
    if attraction["type"] == "historical":
        folium.Marker(
            location=[attraction["latitude"], attraction["longitude"]],
            popup=f"<b>{attraction['name']}</b><br>{attraction['description']}",
            tooltip=attraction["name"],
            icon=folium.Icon(color='blue')
        ).add_to(historical_fg)
    elif attraction["type"] == "natural":
        folium.Marker(
            location=[attraction["latitude"], attraction["longitude"]],
            popup=f"<b>{attraction['name']}</b><br>{attraction['description']}",
            tooltip=attraction["name"],
            icon=folium.Icon(color='green')
        ).add_to(natural_fg)
    elif attraction["type"] == "amusement":
        folium.Marker(
            location=[attraction["latitude"], attraction["longitude"]],
            popup=f"<b>{attraction['name']}</b><br>{attraction['description']}",
            tooltip=attraction["name"],
            icon=folium.Icon(color='red')
        ).add_to(amusement_fg)

# Add feature groups to the map
historical_fg.add_to(map_malaysia)
natural_fg.add_to(map_malaysia)
amusement_fg.add_to(map_malaysia)

# Add layer control to toggle different types of attractions on and off
folium.LayerControl().add_to(map_malaysia)

# Add a feature to display the total number of attractions on the map
total_attractions = len(tourist_attractions)
folium.Marker(
    location=[4.2105, 101.9758],
    popup=f"Total number of attractions: {total_attractions}",
    icon=folium.DivIcon(html=f"""<div style="font-size: 24pt; color: black;">{total_attractions}</div>""")
).add_to(map_malaysia)

# Display the map in Streamlit
st.title("Malaysia Tourist Attractions Map")
st_folium(map_malaysia, width=700, height=500)
