class Vector:
    def __init__(self):
        pass

    def to_gdf(self):
        """Returns vector as a geopandas.GeoDataFrame object"""
        pass

    @property
    def crs(self):
        """Returns vector's CRS as a pyproj.crs.CRS object"""
        pass

    @property
    def shape(self):
        """Return a tuple representing the dimensionality of the DataFrame."""
        pass
