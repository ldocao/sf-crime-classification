import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy


sys.path.append("/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/")
import inputdata
import processing




trainfile = "train"
datadir="/Users/ldocao/Documents/Professionnel/Data Science/Kaggle/2015 06 SF Crime Classification/data"
df = inputdata.read_zipfile(trainfile,dir=datadir)



###PROCESSING
categories = ["Category","DayOfWeek","PdDistrict"]
for cat in categories:
    grouped = df.groupby(cat)
    count = grouped.count()


### PLOT
    plt.figure()
    count.sort(columns="Dates",ascending=1)["Dates"].plot(kind="barh")
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.tight_layout()
    plt.savefig("figures/"+"barh_"+cat+".pdf")



    






