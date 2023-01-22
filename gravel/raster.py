from __future__ import annotations

import dataclasses
from typing import Any, Optional

import numpy as np
from affine import Affine
from pyproj import CRS

from gravel.profiles import RasterProfile


class Raster:
    def __init__(
        self,
        array: Optional[np.ndarray] = None,
        profile: Optional[RasterProfile] = None,
    ):
        """Create Raster object from 2D array"""
        if array is not None:
            self._array = array.copy()
        else:
            self._array = np.empty(shape=(0, 0))
        if profile is None:
            transform = Affine(1, 0, 0, 0, -1, self._array.shape[0])
            profile = RasterProfile(transform=transform)
        self._profile = profile

    def _update_profile(self, key: str, value: Any):
        self._profile = dataclasses.replace(self._profile, **{key: value})

    def to_numpy(self) -> np.ndarray:
        """Returns pixel values as 2D numpy ndarray"""
        return self._array

    @property
    def profile(self) -> RasterProfile:
        """
        Return a Raster's metadata as a Profile object
        """
        return self._profile

    @property
    def crs(self) -> Optional[CRS]:
        """Returns raster's CRS as a pyproj.crs.CRS object"""
        return self.profile.crs

    @crs.setter
    def crs(self, crs: Optional[CRS] = None):
        """
        Setter of CRS
        """
        self._update_profile(key="crs", value=crs)

    @property
    def nodata(self) -> Optional[float]:
        """
        Returns raster's nodata value
        """
        return self.profile.nodata

    @nodata.setter
    def nodata(self, nodata: Optional[float] = None):
        self._update_profile(key="nodata", value=nodata)

    @property
    def shape(self) -> tuple[int, int]:
        """Returns raster's height and width as pixel number"""
        return self.to_numpy().shape

    def plot(self):
        import matplotlib.pyplot as plt

        return plt.imshow(self.to_numpy(), interpolation="nearest")
