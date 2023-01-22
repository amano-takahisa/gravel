import dataclasses
import inspect
from dataclasses import dataclass
from typing import Optional

from affine import Affine
from pyproj.crs.crs import CRS
from rasterio.profiles import Profile as RioProfile


@dataclass(frozen=True)
class Profile:
    crs: Optional[CRS] = None


@dataclass(frozen=True)
class RasterProfile(Profile):
    nodata: Optional[float] = None
    transform: Affine = Affine(1, 0, 0, 0, -1, 0)

    @classmethod
    def from_rioprofile(cls, profile: RioProfile):
        if rio_crs := profile.get("crs"):
            profile = profile.copy()
            profile["crs"] = CRS.from_user_input(rio_crs)
        parameters = inspect.signature(cls).parameters
        return cls(**{k: v for k, v in profile.items() if k in parameters})
