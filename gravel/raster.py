from typing import Tuple
# import numpy as np
from pyproj.crs import CRS
class Raster:
    def __init__(self):
        pass

    # def to_numpy(self) -> np.ndarray:
    def to_numpy(self):
        """Returns pixel values as 2D numpy ndarray"""
        pass

    @property
    def crs(self) -> CRS:
        """Returns raster's CRS as a pyproj.crs.CRS object"""
        pass

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns raster's height and width as pixel number"""
        pass
