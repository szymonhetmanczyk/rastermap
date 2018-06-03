from osgeo import gdal, osr
import numpy as np
import os

class BuildRaster():
    'klasa przechowujaca metody oraz dane do zbudowania rastra'
    def __init__(self, epsg, array, north, east, res):
        self.epsg = epsg
        self.north = north
        self.east = east
        self.res = res
        self.array = array
            
    def setSpatialRef(epsg):
        spatialRef = osr.SpatialReference()
        spatialRef.ImportFromEPSG(epsg) 
        return spatialRef

    def createTarget(north, east, res, array, spatialRef):
        drv=gdal.GetDriverByName('GTiff')
        target = drv.Create("raster.tif", array.shape[0],array.shape[1], 1, gdal.GDT_Float32)
        target.SetProjection(spatialRef.ExportToWkt())
        target.SetGeoTransform((north, res, 0, east, 0, -res))
        return target

    def tband(target, array):
        tband=target.GetRasterBand(1)
        tband.SetNoDataValue(-9999)
        tband.WriteArray(array)
        tband.FlushCache()
        tband.ComputeStatistics(True)
        tband=None

def target(inputraster):
    spatialRef = BuildRaster.setSpatialRef(inputraster.epsg)
    target = BuildRaster.createTarget(inputraster.north, inputraster.east, inputraster.res, inputraster.array, spatialRef)
    return target

def writeRaster(inputtarget, inputraster):
        BuildRaster.tband(inputtarget, inputraster.array)

path = os.path.join(os.path.expanduser("~"),"Documents")
os.chdir(os.path.join(path))
array = np.loadtxt(("map.txt"),dtype='float')
raster = BuildRaster(2180,array,450000, 520000, 30)
target = target(raster)
writeRaster(target,raster)