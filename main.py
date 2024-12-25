#JSON, Requests, and HTTP methods, APIs
#Geocoding and Weather APIs
import key
import requests
import tkinter as tk

geo_url = key.geo_url+key.api_key

response = requests.get(geo_url)

if response.status_code == 200:
    print(f"OK: {response.status_code}")
else:
    print(f"Failed to fetch data: Code {response.status_code}")

print(response.json())



'''
For weather.gov, the api endpoint for 12hr forecast is formatted like this:
https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast


To get this endpoint without entering/knowing the office name, we use:
https://api.weather.gov/points/{latitude},{longitude}
and go down to properties where 
'forecast', 'forecastHourly', and 'forecastGridData' are keys to url values
the urls appear in the following format (similar to the first link above):
https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
'''

#url = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'
wea_url = 'https://api.weather.gov/points/39.7456,-97.0892'

response = requests.get(wea_url) #response can be same variable because geo response not needed anymore

if response.status_code == 200:
    print(f"OK: {response.status_code}")
else:
    print(f"Failed to fetch data: Code {response.status_code}")

print(response.json())



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

temp = tk.Label(layers, text=f"72 F - Sunny", font=("Ariel", 30))
temp.grid(row=1)

location = tk.Label(layers, text="New York City, NY", font=("Ariel", 30))
location.grid(row=2)

layers.pack()


root.mainloop()