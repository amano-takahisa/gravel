"""Tests for `raster` module."""

from gravel import Raster


class TestRaster:
    def test_raster(self):
        raster = Raster()
        assert hasattr(raster, "to_numpy")
