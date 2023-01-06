from dataclasses import dataclass
from typing import Optional

from affine import Affine
from pyproj.crs.crs import CRS


@dataclass(frozen=True)
class Profile:
    crs: Optional[CRS] = None


@dataclass(frozen=True)
class RasterProfile(Profile):

    nodata: Optional[float] = None
    transform: Affine = Affine(1, 0, 0, 0, -1, 0)
