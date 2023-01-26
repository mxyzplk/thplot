import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class Th(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Time History Analyser")
        
        self.geometry("450x250")
        self.resizable(0,0)
        self.config(bg="skyblue")
        
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (MainFrame, DataFrame, ConfigFrame):
        
            frame = F(container, self)
        
            self.frames[F] = frame
        
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainFrame)
        
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        

                
class MainFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__ (self, parent)
        
        menubar = tk.Menu(controller)
        menubar.add_command(label="Data", command=lambda: controller.show_frame(DataFrame))
        menubar.add_command(label="Plot Config", command=lambda: controller.show_frame(ConfigFrame))
        controller.config(menu=menubar)   
        

class DataFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__ (self, parent)
        
        menubar = tk.Menu(controller)
        menubar.add_command(label="Data", command=lambda: controller.show_frame(DataFrame))
        menubar.add_command(label="Plot Config", command=lambda: controller.show_frame(ConfigFrame))
        controller.config(menu=menubar)
             
        self.iniUI()
   
    def iniUI(self):

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)        
        
        analysis_label = tk.Label(self, text="Analysis", font=LARGE_FONT)
        analysis_label.grid(column=0, row=0, columnspan=2, padx=5, pady=10)
        analysis_label.grid_columnconfigure(0,weight=2)
        
        file_label = tk.Label(self, text="File", font=LARGE_FONT)
        file_label.grid(column=0, row=1, columnspan=2, padx=5, pady=10)
        
        group_label = tk.Label(self, text="Group", font=LARGE_FONT)
        group_label.grid(column=1, row=1, columnspan=1, padx=5, pady=10)
        
        analysis_entry = tk.Entry(self, font=LARGE_FONT)
        analysis_entry.grid(column=1, row=0, columnspan=1, padx=20, pady=10)
        
        file1_entry = tk.Entry(self, font=LARGE_FONT)
        file1_entry.grid(column=0, row=2, columnspan=2, padx=5, pady=10)
        
        group1_entry = tk.Entry(self, font=LARGE_FONT)
        group1_entry.grid(column=1, row=2, columnspan=1, padx=5, pady=10)
        
        file2_entry = tk.Entry(self, font=LARGE_FONT)
        file2_entry.grid(column=0, row=3, columnspan=2, padx=5, pady=10)
        
        group2_entry = tk.Entry(self, font=LARGE_FONT) 
        group2_entry.grid(column=1, row=3, columnspan=1, padx=5, pady=10)
        
        file3_entry = tk.Entry(self, font=LARGE_FONT)
        file3_entry.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
        
        group3_entry = tk.Entry(self, font=LARGE_FONT)
        group3_entry.grid(column=1, row=4, columnspan=1, padx=5, pady=10)
        
        save_button = tk.Button(self, text="Save")
        save_button.grid(column=0, row=5, columnspan=3, padx=5, pady=5)
        
        
        

class ConfigFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__ (self, parent)
        
        menubar = tk.Menu(controller)
        menubar.add_command(label="Data", command=lambda: controller.show_frame(DataFrame))
        menubar.add_command(label="Plot Config", command=lambda: controller.show_frame(ConfigFrame))
        controller.config(menu=menubar)   
        
    
            

app = Th()
app.mainloop()
        
