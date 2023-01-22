from importlib import metadata

__version__ = metadata.version(__package__)


from gravel.io import _read_raster_file as read_raster_file  # noqa
from gravel.io import _read_vector_file as read_vector_file  # noqa
