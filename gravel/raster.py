class Raster:
    def __init__(self):
        pass

    def to_numpy(self):
        """Returns pixel values as 2D numpy ndarray"""
        pass

    @property
    def crs(self):
        """Returns raster's CRS as a pyproj.crs.CRS object"""
        pass

    @property
    def shape(self):
        """Returns raster's height and width as pixel number"""
        pass
