import numpy as np
from matplotlib.image import AxesImage
from pyproj import CRS

from gravel.profiles import RasterProfile
from gravel.raster import Raster


class TestRaster:
    def test_raster(self):
        raster = Raster()
        assert hasattr(raster, "to_numpy")

    def test_to_numpy(self):
        array = np.arange(0, 12).reshape((3, 4))
        raster = Raster(array=array)
        assert isinstance(raster.to_numpy(), np.ndarray)

    def test_profile(self):
        raster = Raster()
        assert isinstance(raster.profile, RasterProfile)

    def test_crs(self):
        raster = Raster()
        assert raster.profile.crs is None
        raster.set_crs(CRS.from_epsg(code=4326))
        assert isinstance(raster.profile.crs, CRS)

    def test_nodata(self):
        raster = Raster()
        assert raster.nodata is None
        raster.nodata = 0.0
        assert raster.nodata == 0.0

    def test_shape(self):
        raster = Raster()
        assert raster.shape == (0, 0)
        array = np.arange(0, 12).reshape((3, 4))
        raster = Raster(array=array)
        assert raster.shape == (3, 4)
