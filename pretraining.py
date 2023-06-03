import pandas as pd
def readCSV(filepath):
    
    f = open(filepath,"r")
    df = pd.read_csv(f)
    f.close()
    return df