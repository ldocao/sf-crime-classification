import pandas as pd
import zipfile
import os


        
def read_zipfile(rootname,dir="./"):
    """Return a data frame of all data from zip file

    Parameters:
    ----------
    file: string
        full path to zip csv file
    """
    datadir=os.path.join(dir, '') ##add trailing slash if necessary
    z = zipfile.ZipFile(datadir+rootname+".csv.zip")
    df = pd.read_csv(z.open(rootname+'.csv'), parse_dates=['Dates'])

    return df




def split_time(alldf):
    """Split Dates into date and time columns
    """
    
    df = alldf.iloc[:,0:1] #subset date only
    df = df.set_index("Dates")
    alldf["Time"] = df.index.time
    alldf["Dates"] = df.index.date

    return alldf
    
