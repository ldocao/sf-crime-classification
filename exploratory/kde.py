import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy
import numpy as np
import pdb


sys.path.append("/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/")
import inputdata
import processing



###LOAD DATA
##crime data
trainfile = "train"
datadir="/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/data/"
alldf = inputdata.read_zipfile(trainfile,dir=datadir)


##background grayscale map
mapdata = np.loadtxt(datadir+"sf_map_copyright_openstreetmap_contributors.txt")
lon_lat_box = (-122.5247, -122.3366, 37.699, 37.8299)
clipsize = [[-122.5247, -122.3366],[ 37.699, 37.8299]]






# ###PROCESSING
# for subset in np.unique(df.Category == "Category"):

    
#     z = np.ones()

#     plt.figure()
#     plt.imshow(mapdata, cmap=plt.get_cmap('gray'), extent=lon_lat_box)
#     ##make the plot
#     plt.savefig("./figures/kde_"+subset+".pdf")


