import panda as pd

class Data:
    def __init__(self, csvfile):
        self.df = pd.read_csv(csvfile)
        self.columns = list(self.df.columns.values)


    def plot(self, columns):
        self.df.plot.line(subplots=True,y=columns)
        
    
    def set_index(self, name):
        self.df.set_index(name)
        
    
