import os
from osgeo import gdal
import draw_histogram as hist

path = os.path.join(os.path.expanduser("~"),"Documents")
os.chdir(os.path.join(path))

ptrast = gdal.Open('dem.tif')

band = ptrast.GetRasterBand(1)

hist.histogram(band,10)