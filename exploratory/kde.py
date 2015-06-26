# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
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


coord = alldf.loc[:,["X","Y"]]
coord = coord.loc[0:1000,:]
coord= np.array(coord).transpose()
kernel = scipy.stats.gaussian_kde(coord)




minx=min(clipsize[0])
maxx=max(clipsize[0])
miny=min(clipsize[1])
maxy=max(clipsize[1])
nx=500 #number of xgrid points
ny=500 #number of ygrid points

x_grid = np.arange(minx,maxx, abs(minx-maxx)/nx) #x-axis
y_grid = np.arange(miny,maxy, abs(miny-maxy)/ny) #y-axis
x,y = np.meshgrid(x_grid,y_grid) #create each node of the grid for evaluate
grid_coords = np.append(x.reshape(-1,1),y.reshape(-1,1),axis=1) #reshape in (#npoints,#ndim)
kde = kernel(grid_coords.T) #evaluate kernel at each point
z = kde.reshape(np.size(x_grid),np.size(y_grid)) #reshape it to intuitive grid



plt.figure()
plt.imshow(mapdata, cmap=plt.get_cmap('gray'), extent=lon_lat_box)
plt.imshow(z,alpha=0.4,cmap="Blues",extent=lon_lat_box)
plt.show()

# ###PROCESSING
# for subset in np.unique(df.Category == "Category"):

    
#     z = np.ones()

#     plt.figure()

#     ##make the plot
#     plt.savefig("./figures/kde_"+subset+".pdf")


