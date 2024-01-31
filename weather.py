from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Learning to Code")
root.iconbitmap("Images/BensonHillIngredients.ico")
root.geometry("400x50")



#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=63146&distance=25&API_KEY=35A760D5-17F1-418D-A7B6-A22AEF823FB2

def zipLookup():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=25&API_KEY=35A760D5-17F1-418D-A7B6-A22AEF823FB2")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI'] 
        category = api[0]['Category']['Name']


        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
        
    except Exception as e:
        api = "Error..."










zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root,text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0,column=1, sticky=W+E+N+S)


root.mainloop()