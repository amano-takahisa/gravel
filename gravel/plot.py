from typing import Optional

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
