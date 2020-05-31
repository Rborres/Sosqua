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
datasets = ('20191201','20191207','20191217','20191225','20200106','20200129','20200212','20200221','20200302_m','20200308','20200316','20200325','20200402','20200414_m','20200425','20200512','20200526') 
amount = len(datasets)
maskRaster = rt.open('Mask.tif')
mask = maskRaster.read(1)
amountFarm = 4
eviData = np.zeros((amountFarm+1,amount))

def read():
	global b,r,n,meta,size
	image = rt.open(datasets[dataset]+'.tif')
	meta = image.meta.copy()
	meta.update(dtype=rt.float32,count=1,compress='lzw')

	b = image.read(1)
	b = b/10000
	#g = image.read(2)
	r = image.read(3)
	r = r/10000
	n = image.read(4)
	n = n/10000
	size = b.shape


def index():
	global evi
	evi = np.true_divide(n-r,L+n+(C1*r)-(C2*b))
	evi = evi*G
	#with rt.open(datasets[dataset]+'_EVI.tif', 'w', **meta) as create:
	#    create.write(evi.astype(rt.float32),1)

def applyMask():
	farmer = 1
	while farmer >= amountFarm:
		count = 0
		value = 0
		for i in range(size[0]-2):
			for j in range(size[1]-2):
				if mask[i,j] == farmer:
					value = evi[i,j] + value
					count += 1
				else:pass
		eviData[farmer-1, dataset] = value/count
		farmer += 1


def saveData():
	np.savetxt('EVI_Data.csv',eviData, delimiter=',')


dataset = 0
while dataset != amount:
	read()
	index()
	applyMask()
	dataset += 1

saveData()
