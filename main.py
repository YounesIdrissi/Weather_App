#JSON, Requests, and HTTP methods
import json
import requests
import tkinter as tk

root = tk.Tk()

root.geometry("700x700")
#root.minsize(width=700, height=700)
#root.maxsize(width=700, height=700)
root.resizable(width=False, height=False)
root.title("Weather App")



layers =  tk.Frame(root)

layers.columnconfigure(0, weight=1)#one column, three rows

img = tk.Label(layers, text="Image goes here", font=("Ariel", 30))
img.grid(row=0)

layers.pack()


root.mainloop()