import tkinter as tk
import requests
from tkinter import ttk

# API Key (Replace with your valid OpenWeather API Key)
API_KEY = "78a1d66b8498f6592ed1978267b05f48"
URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=78a1d66b8498f6592ed1978267b05f48"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Weather App")
        self.root.geometry("400x300")
        self.root.configure(bg="#F5F5F5")

        # UI Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 12), background="#F5F5F5")

        # City Input
        self.label_city = ttk.Label(root, text="Enter City Name:")
        self.label_city.pack(pady=10)

        self.entry_city = ttk.Entry(root, font=("Arial", 12))
        self.entry_city.pack(pady=5)

        self.button_get = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get.pack(pady=10)

        self.label_result = ttk.Label(root, text="", font=("Arial", 14, "bold"))
        self.label_result.pack(pady=20)

    def get_weather(self):
        city_name = self.entry_city.get()
        response = requests.get(URL.format(city_name, API_KEY))
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            weather_condition = data["weather"][0]["description"].capitalize()

            self.label_result.config(text=f"{city_name} | {weather_condition}\nTemp: {temp}°C\nHigh: {temp_max}°C | Low: {temp_min}°C")
        else:
            self.label_result.config(text="City not found!")

# Run App
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()