import pandas as pd
import inputdata
import numpy as np
import matplotlib.pyplot as plt
import scipy
import processing
import pdb


trainfile = "train"
datadir="/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/data/"
df = inputdata.read_zipfile(trainfile,dir=datadir)





###PROCESSING
#crime = processing.subset_one(df,"Category","WARRANTS")


mapdata = np.loadtxt(datadir+"sf_map_copyright_openstreetmap_contributors.txt")
lon_lat_box = (-122.5247, -122.3366, 37.699, 37.8299)
clipsize = [[-122.5247, -122.3366],[ 37.699, 37.8299]]




plt.figure()
plt.imshow(mapdata, cmap=plt.get_cmap('gray'), extent=lon_lat_box)

#overplot density of each type of crime
#for a given time
plt.show()




    






