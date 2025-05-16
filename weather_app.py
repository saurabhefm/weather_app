import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch and display weather data
def get_weather():
    city = city_entry.get()
    api_key = "your_api_key_here"
    
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            city_name = data['name']
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            result_label.config(text=f"Weather in {city_name}:\n"
                                    f"Temperature: {temperature}°C\n"
                                    f"Weather: {weather_description}\n"
                                    f"Humidity: {humidity}%\n"
                                    f"Wind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found or invalid request. Please check the city name.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Create and place the widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=20)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

