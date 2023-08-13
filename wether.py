from tkinter import *
from tkinter import ttk  # importing tkinter libary
import requests
root = Tk()  # making the root of tkinter
root.geometry("550x400")
root.config(bg="black")
root.title("Whether forcasting")
def data_get():
    city=city_name.get() 
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3eb9ee5761b793c83dbc0312ca25e288").json()
    DataOfWC.config(text=data["weather"][0]["main"])
    humiData.config(text=data["weather"][0]["description"])
    descrpData.config(text=str(data["main"]["temp"]-273.15))


state_name=["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
    "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
top =Label(root, text="Wheter Forcasting API")
top.place(x=50, y=50, height=30, width=450)

city = Label(root, text="City")
city.place(x=50, y=100, height=30, width=200)

city_name=StringVar()
City_name =ttk.Combobox(root, text="City Name",values=state_name,textvariable=city_name)
City_name.place(x=300, y=100, height=30, width=200)


done = Button(root, text="Get information",command=data_get)
done.place(x=235, y=150, height=30, width=80)

WetherCond = Label(root, text="Wether Condition")
WetherCond.place(x=50, y=200, height=30, width=200)
DataOfWC = Label(root, text="")
DataOfWC.place(x=300, y=200, height=30, width=200)

Humi = Label(root, text="Humidity")
Humi.place(x=50, y=250, height=30, width=200)
humiData = Label(root, text="")
humiData.place(x=300, y=250, height=30, width=200)

temp = Label(root, text="Temperature")
temp.place(x=50, y=300, height=30, width=200)
descrpData = Label(root, text="")
descrpData.place(x=300, y=300, height=30, width=200)


root.mainloop()
