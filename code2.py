from tkinter import *
import tkinter as tk
import requests
import pytz
import json
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
from PIL import Image, ImageTk


root=Tk()
root.title('Weather Checking Application')
root.config(bg='#E1F6FF')
root.geometry('1200x650')
root.resizable(False,False)
def getweather():
    city=entryfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")

    clock.config(text=current_time)
    c.config(text="CURRENT WEATHER")
    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=24d4b1f66fd4dae8f2ec1b8e04207a9e"
    json_data =requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,'°'))
    c.config(text=(condition,'|','Feels','like',temp,'°'))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

    forecast_api = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid=24d4b1f66fd4dae8f2ec1b8e04207a9e"
    forecast_json_data = requests.get(forecast_api).json()

    # Extract forecast data (example: first forecast data)
    forecast_condition = forecast_json_data['list'][0]['weather'][0]['main']
    forecast_description = forecast_json_data['list'][0]['weather'][0]['description']
    forecast_temp = int(forecast_json_data['list'][0]['main']['temp'] - 273.15)
    forecast_time = forecast_json_data['list'][0]['dt_txt']

    # Display forecast data in your GUI
    forecast_label.config(text=f"Forecast: {forecast_condition} | {forecast_description} | {forecast_temp}° at {forecast_time}")



def get_forecast():
    city = entryfield.get()
    url = 'https://wttr.in/{}'.format(city)
    response = requests.get(url)

    try:
        response.raise_for_status()  # Raise an HTTPError for bad responses
        weather_ascii = response.text

        # Display ASCII art in a new window or a messagebox
        # Replace this part with the appropriate Tkinter widget for your application
        messagebox.showinfo("Weather Forecast", weather_ascii)

    except requests.RequestException as req_error:
        # Handle request-related errors
        print(f"Request error: {req_error}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
    #btn_forecaste.config(
        
def reset():
    entryfield.delete(0, END)
    c.config(text=" ")
    t.config(text="0")
    w.config(text="0")
    h.config(text="0")
    d.config(text="0")
    p.config(text="0")
    forecast_label.config(text=' ')

    
img_icon=PhotoImage(file='images/icon.png')
root.iconphoto(False,img_icon)
f_box = PhotoImage(file='images/f1.png',height=150,width=300)
Label(root,image=f_box,bg="black").place(x=480,y=300)
#Label
label1=Label(root,text='Temperature',font=('Audela',12),fg='white',bg='black')
label1.place(x=525,y=320)
    
label1=Label(root,text='Pressure',font=('Audela',12),fg='white',bg='black')
label1.place(x=525,y=340)
    
label1=Label(root,text='Humidity',font=('Audela',12),fg='white',bg='black')
label1.place(x=525,y=360)
    
label1=Label(root,text='Windspeed',font=('Audela',12),fg='white',bg='black')
label1.place(x=525,y=380)
    
label1=Label(root,text='Description',font=('Audela',12),fg='white',bg='black')
label1.place(x=525,y=400)
# Search Box
ser_img=PhotoImage(file="images/Copy of search.png")
simg=Label(image=ser_img,bg="#57adff")
simg.place(x=370,y=120)
#....
entryfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
entryfield.place(x=470,y=140)
entryfield.focus()

Search_icon = PhotoImage(file="images/Copy of search_icon.png",height=50)
s_img=Button(image=Search_icon,borderwidth=5,cursor="hand2",bg="#203243",command=getweather)
s_img.place(x=770,y=130)
                   
btn_reset = Button(root,text='RESET',font=18,bg='#E1F6FF',command=reset)
btn_reset.place(x=560,y=500)

btn_forecast = Button(root,text='FORECAST',font=18,bg='#E1F6FF',command=get_forecast)
btn_forecast.place(x=540,y=550)
# clock
clock = Label(root,font=("Audela",30,'bold'),fg="black",bg="#E1F6FF")
clock.place(x=1000,y=50)
#timezone
timezone = Label(root,font=("Audela",20,'bold'),fg="white",bg="#E1F6FF")
timezone.place(x=40,y=80)
#longitude
long_lat = Label(root,font=("Audela",10,'bold'),fg="white",bg="#E1F6FF")
long_lat.place(x=1000,y=100)

forecast_label = Label(root,font=("Audela",10,'bold'),fg="black",bg="#E1F6FF")
forecast_label.place(x=450,y=470)


c=Label(root,font=("Audela",18),fg="black",bg="#E1F6FF")
c.place(x=520,y=250)
t=Label(root,font=("Audela",11),fg="white",bg="black")
t.place(x=630,y=320)
p=Label(root,font=("Audela",11),fg="white",bg="black")
p.place(x=630,y=340)
h=Label(root,font=("Audela",11),fg="white",bg="black")
h.place(x=630,y=360)
w=Label(root,font=("Audela",11),fg="white",bg="black")
w.place(x=630,y=380)
d=Label(root,font=("Audela",11),fg="white",bg="black")
d.place(x=630,y=400)


root.mainloop()




























