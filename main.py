import folium
import pandas as pd
import geopandas as gpd
from branca.colormap import LinearColormap

def main():
    file_path = "data/sum_data.csv"
    df = pd.read_csv(file_path)

    # Load GeoJSON file with country boundaries
    world_geojson_path = 'geo/countries.geojson'  # Change this to the path of your GeoJSON file
    world_geojson = gpd.read_file(world_geojson_path)

    # Merge DataFrame with GeoDataFrame on country code
    df_geo = world_geojson.merge(df, how='left', left_on='ISO_A3', right_on='COUNTRYID')

    # Create a colormap from dark blue to dark red
    colormap = LinearColormap(['green', 'yellow', 'red'], vmin=0, vmax=100)

    # Create a map centered on the world
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Add GeoJSON layer with country boundaries colored by SCREEN_FAIL_PROPORTION
    folium.GeoJson(
        df_geo,
        name='geojson',
        style_function=lambda feature: {
            'fillColor': 'white' if pd.isna(feature['properties']['SCREEN_FAIL_PROPORTION']) else colormap(feature['properties']['SCREEN_FAIL_PROPORTION']),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.5,
        }
    ).add_to(m)

    # Add colorbar
    colormap.add_to(m)

    # Display the map
    m.save('output/heatmap.html')  # Save the map to an HTML file

if __name__ == "__main__":
    main()