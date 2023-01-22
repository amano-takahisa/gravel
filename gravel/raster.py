from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Any, Optional

import numpy as np
from affine import Affine
from pyproj import CRS

from gravel.profiles import RasterProfile

if TYPE_CHECKING:
    from matplotlib.image import AxesImage


class Raster:
    def __init__(
        self,
        array: Optional[np.ndarray] = None,
        nodata: Optional[float] = None,
        profile: Optional[RasterProfile] = None,
    ):
        """Create Raster object from 2D array"""
        if array is not None:
            self._array = array.copy()
        else:
            self._array = np.empty(shape=(0, 0), dtype="uint8")

        self._nodata: Optional[float] = nodata

        if profile is None:
            transform = Affine(1, 0, 0, 0, -1, self._array.shape[0])
            profile = RasterProfile(transform=transform)
        self._profile = profile

    def __str__(self):
        return "\n".join(
            [
                self.to_numpy().__str__(),
                "nodata: " + self.nodata.__str__(),
                self.profile.__str__(),
            ]
        )

    def __repr__(self):
        return "\n".join(
            [
                self.to_numpy().__repr__(),
                "nodata: " + self.nodata.__repr__(),
                self.profile.__repr__(),
            ]
        )

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

    def set_crs(self, crs: Optional[CRS] = None):
        """
        Setter of CRS
        """
        self._update_profile(key="crs", value=crs)

    @property
    def nodata(self) -> Optional[float]:
        return self._nodata

    @nodata.setter
    def nodata(self, nodata: Optional[float] = None):
        if nodata is None:
            self._nodata = nodata
            return

        array_dtype = self.to_numpy().dtype
        if array_dtype.kind == "i" and isinstance(nodata, float):
            raise ValueError(f"nodata is float. array is {array_dtype.name}.")
        if array_dtype.kind == "f":
            if np.isnan(nodata):
                self._nodata = nodata
                return
            dtype_min = np.finfo(array_dtype).min
            dtype_max = np.finfo(array_dtype).max
        else:
            dtype_min = np.iinfo(array_dtype).min
            dtype_max = np.iinfo(array_dtype).max

        if not (dtype_min <= nodata <= dtype_max):
            raise ValueError(
                "nodata value overflow dtype of array. Array dtype is"
                f" {array_dtype.name}"
            )
        self._nodata = nodata

    @property
    def shape(self) -> tuple[int, int]:
        """Returns raster's height and width as pixel number"""
        return self.to_numpy().shape

    def plot(self) -> AxesImage:
        from gravel.plot import plot_raster

        return plot_raster(self)
