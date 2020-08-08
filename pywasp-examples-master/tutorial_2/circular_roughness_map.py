"""Create a pywasp roughness map with only a single circular roughness change"""
# coding: utf-8
#pylint: disable=multiple-statements

#################
# Load libraries
#################
# Python standard library:
from math import radians, sin, cos

# Third party:
from collections import defaultdict
import geopandas as gpd
from shapely.geometry import Point, LineString

# Constants
NSECS = 12
EPSG = 3035

def circular_roughness_map(radius, z01, z02):
    """
    Make a roughness map with a single circular roughness change

    Parameters
    -----------
    radius : float
        Radius of circle
    z01 : float
        Inner roughness length
    z02 : float
        Outer roughness length

    Returns
    -------
        Vector representation of the map.
    """
    # Add an additional point to close the circle
    n_pts = NSECS + 1

    # Get the center-angle for each sector for calculating the distance
    step = 360.0 / (n_pts - 1.)
    angs = [x * step for x in range(n_pts)]

    # Create a list of points going around the circle
    pts = []
    for ang in angs:
        x = radius * sin(radians(ang))
        y = radius * cos(radians(ang))
        pts.append(Point(x, y))

    # Populate a dictionary that will be used for creating the GeoDataFrame
    # It is important to use defaultdict here as the GeoDataFrame expects a
    # list for each value of the dict
    data = {
        "z0_left": [z02],
        "z0_right": [z01],
        "geometry": [LineString(pts)],
    }
    
    # generate the GeoDataFrame of the circle
    return gpd.GeoDataFrame(data, geometry="geometry", crs=EPSG) 
