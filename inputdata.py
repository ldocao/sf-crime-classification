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
    dir=os.path.join(dir, '') ##add trailing slash if necessary
    z = zipfile.ZipFile(dir+rootname+".csv.zip")
    df = pd.read_csv(z.open(rootname+'.csv'), parse_dates=['Dates'])

    return df




    
