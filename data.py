import pandas as pd
import matplotlib.pyplot as plt

class Data:
    def __init__(self, csvfile):
        self.df = pd.read_csv(csvfile, skipinitialspace = True)
        self.columns = list(self.df.columns.values)

    def set_index(self, name):
        self.df.set_index(name)
        
        
    def plot_series(self, listofcolumns):
        n = len(listofcolumns)

        self.df.plot(subplots=True, nrows=10, ncols=1, y=listofcolumns, figsize=(6, 6), xlabel="Time[s]")
        #self.df.plot(subplots=True, y=['AOA','NZ'], figsize=(6, 6), xlabel="Time[s]")
        plt.legend(loc='best')
        
res=Data("flsim_th.txt")
listofcolumns=["AOA","NZ","FZWB","FZHT"]
res.set_index("TIME")
res.plot_series(listofcolumns)

        
    
