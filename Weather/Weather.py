import requests

class City:

    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()


    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={self.lat}&lon={self.lon}&appid=YOUR API KEY")

        except:
            print("No internet connection :( ")

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]


    def temp_print(self):
        print(f"In {self.name} it is currently: {self.temp}° C")
        print(f"Today's High: {self.temp_max}° C")
        print(f"Today's Low: {self.temp_min}° C")


my_city = City("Romania",45.2998,21.8801)
my_city.temp_print()


vacation_city = City("Greece",39.0742,21.8243)
vacation_city.temp_print()
