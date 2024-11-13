import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser

aa=tk.Tk()
aa.title("goals")
aa.geometry("500x500")



def  hsp():
    gt=search.get()
    
    """  url """
    hb=f"https://www.hepsiburada.com/ara?q={gt}"
    ty=f"https://www.trendyol.com/sr?q={gt}&qt={gt}&st={gt}&os=1"
    amz=f"https://www.amazon.com.tr/s?k={gt}&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=KRELF70G1RQD&sprefix=f%C4%B1nd%C4%B1k%2Caps%2C181&ref=nb_sb_noss_1"
    gogle=f"https://www.google.com/search?q={gt}"
    
    webbrowser.open(hb)
    
  

search=tk.Entry(aa)
search.pack()


cal = tk.Button(aa, text="find", command=hsp)
cal.pack()







aa.mainloop()