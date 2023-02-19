from __future__ import annotations

import dataclasses
import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Optional, Union

import rasterio
from affine import Affine
from pyproj.crs.crs import CRS
from rasterio.profiles import Profile as RioProfile

from gravel.profiles import RasterProfile
from gravel.raster import Raster
from gravel.vector import Vector


def _read_raster_file(
    filename: Union[Path, BinaryIO]
) -> tuple[Raster, RasterFileMetadata]:
    with rasterio.open(filename) as src:
        array = src.read(1)
        rio_profile = src.profile
    nodata = rio_profile.get("nodata")
    profile = RasterProfile.from_rioprofile(rio_profile)
    metadata = RasterFileMetadata.from_rioprofile(rio_profile)
    return Raster(array=array, nodata=nodata, profile=profile), metadata


def _read_vector_file(filename) -> Vector:
    raise NotImplemented


@dataclass(frozen=True)
class RasterFileMetadata:
    driver: str
    dtype: str
    width: int
    height: int
    count: int
    transform: Affine
    blockxsize: int
    blockysize: int
    tiled: bool
    nodata: Optional[float] = None
    crs: Optional[CRS] = None

    def __repr__(self):
        # use .to_string() for CRS
        return "\n".join(
            [
                f"{f.name}: {getattr(self, f.name).to_string()}"
                if f.name == "crs" and self.crs is not None
                else f"{f.name}: {getattr(self, f.name).__repr__()}"
                for f in dataclasses.fields(self)
            ]
        )

    @classmethod
    def from_rioprofile(cls, profile: RioProfile):
        if rio_crs := profile.get("crs"):
            profile = profile.copy()
            profile["crs"] = CRS.from_user_input(rio_crs)
        parameters = inspect.signature(cls).parameters
        return cls(**{k: v for k, v in profile.items() if k in parameters})
