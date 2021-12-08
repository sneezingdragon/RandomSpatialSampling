from mmap import ACCESS_READ
import random
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import fiona
import math
random.seed(0)
layers = fiona.listlayers('C:/Users/sneez/OneDrive/Documents/lab3.gpkg')
print(layers)
for layer in layers:
    huc8 = gpd.read_file(r'C:/Users/sneez/OneDrive/Documents/lab3.gpkg', layer = 'wdbhuc8')
    huc12 = gpd.read_file(r'C:/Users/sneez/OneDrive/Documents/lab3.gpkg', layer = 'wdbhuc12')
    ssurgo = gpd.read_file(r'C:/Users/sneez/OneDrive/Documents/lab3.gpkg', layer = 'ssurgo_mapunits_lab3')
for district in huc8:
    Fellowshipofthearea = huc8.area/1000000
for district in huc12:
    Returnofthearea = huc12.area/1000000
print('Random X between 0 and 10:', random.uniform(0, 10))
print('Random Y between 0 and 10:', random.uniform(0,10))
huc8_bounds = huc8.total_bounds
huc12_bounds = huc12.total_bounds
for idx, row in huc8.iterrows():
    print(huc8.bounds)   
# print(f"{row['name']} extent => {row['geometry'], bounds}")
Point_total = Fellowshipofthearea * (.05)
round(Point_total)
Point_total12 = Returnofthearea * (.05)
Rounditup = round(Point_total12)
rando_points = {'point_id': [], 'geometry': []}
for idx, row in huc8.iterrows():
    point = Point(0, 0)
    intersects = False
    
    while intersects == False:
        x = random.uniform(huc8_bounds[0], huc8_bounds[2])
        y = random.uniform(huc8_bounds[1], huc8_bounds[3])
        point = Point(x, y)
    
        results = huc8['geometry'].intersects(point)
   
        if True in results.unique():
            rando_points['geometry'].append(Point((x,y)))
            rando_points['point_id'].append(idx)
            
            intersects = True
rando_points
rando_points_gdf = gpd.GeoDataFrame(rando_points, crs=huc8.crs)
huc8_dots = gpd.overlay(rando_points_gdf, huc8, how='intersection')
rando_points12 = {'point_id': [], 'geometry': []}
for idx, row in huc12.iterrows():
    point = Point(0, 0)
    intersects = False
    
    while intersects == False:
        x = random.uniform(huc12_bounds[0], huc12_bounds[2])
        y = random.uniform(huc12_bounds[1], huc12_bounds[3])
        point = Point(x, y)
    
        results = huc12['geometry'].intersects(point)
   
        if True in results.unique():
            rando_points12['geometry'].append(Point((x,y)))
            rando_points12['point_id'].append(idx)
            
            intersects = True
rando_points12
rando_points12_gdf = gpd.GeoDataFrame(rando_points12, crs=huc12.crs)
huc12_dots = gpd.overlay(rando_points12_gdf, huc12, how='intersection')
import rasterio
from rasterio.plot import show
huc12_points = gpd.overlay(huc12_dots, ssurgo, how='intersection')
grouping12 = huc12_points.groupby(by='point_id').mean()
mean12 = grouping12['aws0150'].mean()
print(mean12)
huc8_points = gpd.overlay(huc8_dots, ssurgo, how='intersection')
grouping8 = huc8_points.groupby(by='point_id').mean()
mean8 = grouping8['aws0150'].mean()
print(mean8)