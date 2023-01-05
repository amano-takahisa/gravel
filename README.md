# GRAVEL
a Geospatial RAster and VEctor data processing Library.
## Usage
### Install

Requirements
```bash
sudo apt install gdal-bin libgdal-dev python3-pip
```
Install
```bash
git clone --depth=1 https://github.com/amano-takahisa/gravel
pip install gravel
```
Some dependencies are not installed by default to reduce package size, such as matplotlib for `.plot()`.
Add extra groups to pip to use them.
```bash
pip install gravel[plot]
```

### Use

## Development
### Basic design policy

This library forcus to interface between raster and vector data.

Following features are/will be provided.
- Raster
    - [ ] I/O files
    - [ ] Get/set metadata
    - [ ] Create from/export to numpy array
    - [ ] Clip by Vector
    - [ ] Extract pixel values by Vector
    - [ ] Vectorize
    - [ ] Warp to other CRS
    - [ ] Plot
- Vector
    - [ ] I/O files
    - [ ] Get/set metadata
    - [ ] Create from/export to (Geo)Pandas
    - [ ] Clip by Vector
    - [ ] Rasterize
    - [ ] Warp to other CRS
    - [ ] Plot
