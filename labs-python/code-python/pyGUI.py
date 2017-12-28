""" 
Simple Tkinter Python GUI app
"""

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

#button with message box callback
def helloCallBack():
	tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()


#canvas with circle arc
C = Tkinter.Canvas(top, bg="#4433FF", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()

#set window transparency
top.attributes("-alpha", .95)

top.mainloop()

"""
import ttk
s=ttk.Style()
print(s.theme_names())
# winnative
# clam
# alt
# default
# classic
# xpnative

s.theme_use('clam')
print(s.theme_use())
""" 