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
