import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser
import webview
import time
aa=tk.Tk()
aa.title("goals")
aa.geometry("500x500")



def  hsp():
    """ search """
    gt=search.get()
    """ price least"""
    gtprc=float(price.get())
    """ price most """
    gtprcone=float(priceone.get())
    
    """  url """
    hb=f"https://www.hepsiburada.com/ara?q={gt}&filtreler=VariantList.VariantListing.BuyboxPrice:{gtprc}- {gtprcone}"
    ty=f"https://www.trendyol.com/sr?q={gt}&qt={gt}&st={gt}&os=1&prc={gtprc}- {gtprcone}"
    amz=f"https://www.amazon.com.tr/s?k={gt}&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=KRELF70G1RQD&sprefix=f%C4%B1nd%C4%B1k%2Caps%2C181&ref=nb_sb_noss_1&low-price={gtprc}&high-price={gtprcone}"
    gogle=f"https://www.google.com/search?q={gt}"
    
    webbrowser.open(hb)
    time.sleep(1)
    webbrowser.open(ty)
    time.sleep(1)
    webbrowser.open(amz)
    time.sleep(1)
    webbrowser.open(gogle)
""" search """
search=tk.Entry(aa)
search.pack()

""" price scala least """
price=tk.Entry(aa)
price.pack()

""" price scala most """
priceone=tk.Entry(aa)
priceone.pack()


cal = tk.Button(aa, text="find", command=hsp)
cal.pack()







aa.mainloop()