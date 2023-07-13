import requests
import tkinter as tk

API_KEY = "2eab4787193d8f84f016acd745ad77cd"
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    return data

def show_weather():
    city = city_entry.get()
    weather_data = get_weather_data(city)
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    result_label["text"] = f"The temperature in {city} is {temperature}°C. Weather: {description}"

# Create the main window
window = tk.Tk()
window.title("Weather Detection")

# Create and place GUI components
city_label = tk.Label(window, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

weather_button = tk.Button(window, text="Get Weather", command=show_weather)
weather_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()