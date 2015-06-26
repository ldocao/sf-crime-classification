import shapefile as shp #download at https://github.com/GeospatialPython/pyshp
#import urllib
import zipfile
import pdb
import matplotlib.pyplot as plt


### GET POPULATION DENSITY FILE
##download file
##i dont know why the file doesnt download completely
#url = "https://data.sfgov.org/download/ea9w-4zvc/SHAPEFILE/SanFranciscoPopulation.zip"
destdir = "/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/data/"
name = "SanFranciscoPopulation"
destfile = destdir+name+".zip"
#urllib.urlretrieve(url, destfile)

zfile = zipfile.ZipFile(destfile)
zfile.extractall(destdir)


sf = shp.Reader(destdir+name)

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y,"b")
plt.show()
