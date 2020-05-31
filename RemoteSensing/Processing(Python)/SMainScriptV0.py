import rasterio as rt
import numpy as np
from matplotlib import pyplot as plt
from rasterio.plot import show
from rasterio.plot import show
from rasterio.mask import mask
from fiona.crs import from_epsg
import pycrs

# Index coefficients
L = 1 
C1 = 6
C2 =  7.5
G = 2.5
#datasets names
datasets = ('20191207','20191217','20200425','20200106') 
amount = len(datasets)
def read():
	global b,r,n,meta, size
	blue = rt.open('S_'+datasets[dataset]+'_B02.tif')
	red = rt.open('S_'+datasets[dataset]+'_B04.tif')
	nir = rt.open('S_'+	datasets[dataset]+'_B08.tif')
	meta = blue.meta.copy()
	meta.update(dtype=rt.float32,count=1,compress='lzw')

	b = blue.read(1)
	b = b/10000
	#g = image.read(2)
	r = red.read(1)
	r = r/10000
	n = nir.read(1)
	n = n/10000
	size = b.shape


def index():
	global evi, evi_f
	evi = np.true_divide(n-r,L+n+(C1*r)-(C2*b))
	evi = evi*G
	evi_f = np.zeros(size)
	for i in range(size[0]-1):
		for j in range(size[1]-1):
			if evi[i,j] >= 0  and evi[i,j] <= 1:
				evi_f[i,j] = evi[i,j]
			else:pass

	with rt.open('S_'+datasets[dataset]+'_EVI.tif', 'w', **meta) as create:
	   create.write(evi_f.astype(rt.float32),1)
	plt.imshow(evi)
	plt.colorbar()
	plt.show()

dataset = 0
while dataset != amount:
	read()
	index()
	dataset = dataset + 1

