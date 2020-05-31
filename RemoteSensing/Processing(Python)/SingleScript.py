import rasterio as rt
import numpy as np
from matplotlib import pyplot as plt
from rasterio.plot import show
from rasterio.plot import show
from rasterio.mask import mask
from fiona.crs import from_epsg
import pycrs
from osgeo import gdal

image = rt.open('20200526.tif')
meta = image.profile
b = image.read(1)
b = b/10000
g = image.read(2)
r = image.read(3)
r = r/10000
n = image.read(4)
n = n/10000

size = b.shape
L = 1 
C1 = 6
C2 =  7.5

evi = np.true_divide(n-r,L+n+(C1*r)-(C2*b))
evi = evi*2.5
evi_f = np.zeros(size)
#evi_f = evi_f -1
for i in range(size[0]-1):
	for j in range(size[1]-1):
		if evi[i,j] > 0.4  and evi[i,j] < 1:
			evi_f[i,j] = evi[i,j]
		else:pass

meta.update(dtype=rt.float32,count=1,compress='lzw')
with rt.open("evi.tif", 'w', **meta) as create:
    create.write(evi_f.astype(rt.float32),1)

plt.imshow(evi_f)
plt.colorbar()
plt.show()
