import geopandas as gpd
import numpy as np
from shapely.geometry import Polygon
import math
import geohexgrid as ghg

def create_hex_grid_from_geojson(file_path):
    # Load GeoDataFrame from GeoJSON file
    gdf = gpd.read_file(file_path)

    # Calculate Area
    total_area = gdf.geometry.area.sum()

    # Number of rows in the GeoDataFrame
    num_rows = len(gdf)

    # Calculate the area of each hexagon
    hexagon_area = total_area / num_rows

    apothem = 3 * math.sqrt(3) / 2  # Calculate the apothem

    radius = math.sqrt(hexagon_area / apothem)

    # Create Grids
    grid = ghg.make_grid_from_gdf(gdf, R=(radius * 1.28))

    # Plot
    base = gdf.plot(color="black", figsize=(10, 10), aspect="equal")
    grid.plot(ax=base, color="white", edgecolor="red", alpha=0.5)
    return grid

if __name__ == "__main__":
    # Specify the path to your GeoJSON file
    file_path = r"TN_Districts_4326.geojson"

    # Call the function to create hex grids and plot
    hex_grid = create_hex_grid_from_geojson(file_path)

    # Show the plot (optional)
    import matplotlib.pyplot as plt
    plt.show()
