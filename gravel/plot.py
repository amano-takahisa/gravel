from typing import Optional

import numpy as np
import rasterio.plot
from matplotlib.axis import Axis
from matplotlib.image import AxesImage

from gravel.raster import Raster


def plot_rgb(
    r: Optional[Raster] = None,
    g: Optional[Raster] = None,
    b: Optional[Raster] = None,
) -> AxesImage:
    """
    Plot rasters as RGB image

    """
    raise NotImplementedError


def plot_raster(
    raster: Raster, ax: Optional[Axis] = None, title: Optional[str] = None
) -> AxesImage:
    array = raster.to_numpy()
    nodata = raster.nodata
    if nodata is None:
        pass
    elif np.isnan(nodata):
        pass
    else:
        if array.dtype.kind != "f":
            array = array.astype("float32")
        array[array == nodata] = np.nan
    return rasterio.plot.show(
        source=array,
        with_bounds=True,
        contour=False,
        contour_label_kws=None,
        ax=ax,
        title=title,
        transform=raster.profile.transform,
        adjust=False,
    )
