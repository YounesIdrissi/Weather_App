#JSON, Requests, and HTTP methods, APIs
#Geocoding and Weather APIs
import key
import requests
import tkinter as tk

'''
First Request.
We must use json stdlib parsing to extract required data.
Required geocoding data: results --> navigation_points --> location
We utilize the direct access method (explicit traversal) using brackets [][][]
There are many more (and better) methods of traversal
'''

geo_url = key.geo_url

response = requests.get(geo_url)

latitude = None
longitude = None #declaring these so we can later check if they obtained a valid value

if response.status_code == 200:
    print(f"OK: {response.status_code}")
    try:
        latitude = response.json()['results'][0]['navigation_points'][0]['location']['latitude']
        longitude = response.json()['results'][0]['navigation_points'][0]['location']['longitude']
        print(latitude)
        print(longitude)
    except: #OK status BUT index doesn't exist because of faulty user input
        print(f"Error: {response.json()['status']}")
else:
    print(f"Failed to fetch data: Code {response.status_code}")

#print(response.json()) #print response, if any (for troubleshooting purposes)





'''
Second Request.
For weather.gov, the api endpoint for 12hr forecast is formatted like this:
https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
example --> url = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'


To get this endpoint without entering/knowing the office name, we use:
https://api.weather.gov/points/{latitude},{longitude}
and go down to properties where 
'forecast', 'forecastHourly', and 'forecastGridData' are keys to url values
the urls appear in the following format (similar to the first link above):
https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast
'''

forecast_url = None #declaring this so we can later check if they obtained a valid value

if latitude and longitude: #if latitude and longitude exist, then execute (avoids error)
    wea_url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = requests.get(wea_url) #'response' can be same variable because geo 'response' not needed anymore

    if response.status_code == 200:
        print(f"OK: {response.status_code}")
        forecast_url = response.json()['properties']['forecast']
    else:
        print(f"Failed to fetch data: Code {response.status_code}")

    #print(response.json()) #print response, if any (for troubleshooting purposes)

'''
The last request (weather.gov API), using the forecast_url
7 Day Forecast: properties --> periods (contains all weather data)
We need the following data from each period:
- 'number' (to process data --> increment all by 1, floor divide by 2, decrement all by 1
(this is an example of algebraic (data) manipulation); day 0 is today, day 1 is tmrw, etc)
- 'name' (direct implementation)
- 'temperature'
- 'detailedForecast'
'''

if forecast_url:

    response = requests.get(forecast_url)

    if response.status_code == 200:
        print(f"OK: {response.status_code}")
        #now we need to extract large data
        weather_data = {}
        #n = 0 #we use this for number keys (see notes in book)
        for i in response.json()['properties']['periods']:
            print(i)
    else:
        print(f"Failed to fetch data: Code {response.status_code}")

    #print(response.json()) #print response, if any (for troubleshooting purposes)



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