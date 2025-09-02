##https://github.com/steffanic/streamlit-geolocation

##https://folium.streamlit.app/
## pip install folium
##pip install streamlit_folium
##pip install streamlit_geolocation
##pip install streamlit

## Estaciones de servicio
## https://geoportalgasolineras.es/geoportal-instalaciones/DescargarFicheros

import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import folium
from streamlit_folium import st_folium
import pandas as pd

def glp_maps():
    location_current = streamlit_geolocation()

    st.write("Latitude: " + str(location_current["latitude"]))
    st.write("Longitude: " + str(location_current["longitude"]))

    m = folium.Map(location=[str(location_current["latitude"]),str(location_current["longitude"])], zoom_start=9)
    folium.Marker([float(location_current["latitude"]),float(location_current["longitude"])], popup="Casa", tooltip="Ubicacion", icon=folium.Icon(color="blue", icon="star")).add_to(m)

    ## GLP
    df = pd.read_csv('./data/GLP.csv',sep='|')

    for record in df.values:
        #print(f"Valores {record[4]}, {record[5]}")
        folium.Marker(location=[record[4],record[5]],icon=folium.Icon(color="red", icon="flag")).add_to(m)

    #Call to render Folium map in Streamlit

    st_data = st_folium(m, width=725)

if __name__ == '__main__':
    glp_maps()





