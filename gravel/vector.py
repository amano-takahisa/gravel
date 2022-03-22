from typing import Tuple
import geopandas as gpd
from pyproj.crs import CRS
class Vector:
    def __init__(self):
        pass

    def to_gdf(self) -> gpd.GeoDataFrame:
        """Returns vector as a geopandas.GeoDataFrame object"""
        pass

    @property
    def crs(self) -> CRS:
        """Returns vector's CRS as a pyproj.crs.CRS object"""
        pass

    @property
    def shape(self) -> Tuple[int, int]:
        """Return a tuple representing the dimensionality of the DataFrame."""
        pass
