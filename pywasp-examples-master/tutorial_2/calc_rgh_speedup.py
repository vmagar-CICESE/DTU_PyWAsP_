
# coding: utf-8
#pylint: disable=multiple-statements

#################
# Load libraries
#################


# Third party:
import pywasp as pw
from circular_roughness_map import circular_roughness_map

# Constants
NSECS = 12
LOC_X = 0
LOC_Y = 0

def calc_rgh_speedup(test):
    """
    Calculates roughness induced speed ups.

    Parameters
    ----------
    test : panda Series
        pd Series containing single row of 6 elements.

    Returns
    -------
        roughness induced speedup in the first sector

    Note
    ----
    Since we are creating circular roughness change the roughness induced
    speedups in all sectors should be the same.

    """
    rgh_map = circular_roughness_map(test['radius'], test['z01'], test['z02'])
    rgh_bbox = pw.BBox.from_cornerpts(*list(rgh_map.bounds.values[0]), rgh_map.crs)
    elev_map = pw.create_flat_vectormap(bbox=rgh_bbox, crs=rgh_map.crs)
    topo_map = pw.wasp.TopographyMap(elev_map, rgh_map)

    conf = pw.wasp.Config()
    conf.terrain.putpar(40, test['p40'])
    conf.terrain.putpar(41, test['p41'])
    conf.terrain.putpar(65, 1)
    conf.terrain.putpar(82, 0)
    topo_pt = topo_map.to_point(LOC_X, LOC_Y, NSECS, test['height'], conf)

    return topo_pt.site_factors.speedups.roughness[0]
