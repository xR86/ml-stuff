'''
Visualizer for CMU 2009 ZBJ HW1.pr4 data
http://profs.info.uaic.ro/~ciortuz/ML.ex-book/implementation-exercises/CMU.2009s.ZBJ.HW1.pr4.linRegr.insulin.data.NO-code/

'''

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
#from matplotlib import style

import Tkinter as tk
import ttk


LARGE_FONT= ("Verdana", 12)
#style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    fd = open("matplot-text.txt","r")
    pullData = fd.read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    data_typeList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y, data_type = eachLine.split(' ')
            xList.append(float(x))
            yList.append(float(y))
            data_typeList.append(int(data_type))
    fd.close()
    
    fd2 = open("matplot-output.txt","r")
    pullData = fd2.read()
    dataList = pullData.split('\n')

    x2List = []
    y2List = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(' ')
            x2List.append(float(x))
            y2List.append(float(y))


    a.clear()
    index_change = data_typeList.index(2) #find training data index
    # a.plot(xList, yList)
    #a.scatter(xList, yList, c="#FF0000")
    a.scatter(xList[:index_change], yList[:index_change], c="#FF0000")
    a.scatter(xList[index_change:], yList[index_change:], c="#0000FF")
    a.plot(x2List, y2List, c="#00FF00")

    
            

class DataClient(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Data visualizer")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = PageThree(container, self)
        self.frames[PageThree] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageThree)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Red = train\nBlue = test", font=LARGE_FONT)
        label.pack(pady=10,padx=10,side=tk.RIGHT)

        '''
        check_button_train_var = tk.IntVar()
        check_button_train = tk.Checkbutton(self, text="Show Train Data", variable=check_button_train_var, \
                            onvalue=1, offvalue=0, height=5, \
                            width=20)
        check_button_train.pack(side = tk.RIGHT) # pady=5, padx=5,

        check_button_test_var = tk.IntVar()
        check_button_test = tk.Checkbutton(self, text="Show Test Data", variable=check_button_test_var, \
                                            onvalue=1, offvalue=0, height=5, \
                                            width=20)
        check_button_test.pack(side=tk.RIGHT)
        '''

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = DataClient()
ani = animation.FuncAnimation(f, animate, frames=20, interval=1000)
app.mainloop()
