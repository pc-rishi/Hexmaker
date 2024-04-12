# Hexagonal Grid Generation: Equal-Sized Hexagons for Each Geographic Row

This repository contains a Python script (`main.py`) that demonstrates how to create a hexagonal grid from a GeoJSON file using GeoPandas and a custom library called `geohexgrid`. The script calculates the area of each hexagon based on the total area of the geometries in the GeoJSON file and then determines the radius of the circumscribed circle for the hexagons. It then uses `geohexgrid` to generate the hexagonal grid and visualizes it on top of the original GeoDataFrame.

## Required Libraries

To run the script, you'll need the following Python libraries installed:

- `geopandas`: For reading and manipulating GeoJSON files and geometries.
- `numpy`: For numerical calculations.
- `shapely`: For geometric operations and calculations.
- `geohexgrid`: A custom library (not included in standard Python libraries) for creating hexagonal grids. You may need to install this library separately from its source or repository.

## Usage

1. Clone or download this repository to your local machine.
2. Install the required libraries using pip:
3. Install `geohexgrid` from its source or repository (if not already installed).
4. Modify the `file_path` variable in `main.py` to point to your GeoJSON file.
5. Run the script using Python:


## Example: Creating Hexagons for Indian States

The `main.py` script allows you to create equal-sized hexagons that match the number of rows you provide as input. For example, if you want to create equal-sized hexagons representing all states of India, you can provide a GeoJSON file containing the geometries of Indian states as input to the script.

## Notes

- Make sure you have a valid GeoJSON file with geometries that you want to convert into a hexagonal grid.
- Ensure that the required libraries (`geopandas`, `numpy`, `shapely`, `geohexgrid`) are installed and accessible in your Python environment before running the script.
