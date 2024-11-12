import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk

aa=tk.Tk()
aa.title("goals")
aa.geometry("500x500")

secenek=["ev","araba","para biriktirme"]
ılk=tk.StringVar()
ılk.set(secenek[0])

oc=tk.OptionMenu(aa ,ılk ,*secenek )
oc.pack()
""" price """
one=tk.Entry(aa )
one.pack()
"how much mounth"
two=tk.Entry(aa)
two.pack()

tri=tk.Entry(aa)
tri.pack()

bb=tk.Label(aa)
bb.pack()
def  hsp():
    al=one.get()
    bb.config(text=al)
    



cal = tk.Button(aa, text="calculate", command=hsp)
cal.pack()







aa.mainloop()