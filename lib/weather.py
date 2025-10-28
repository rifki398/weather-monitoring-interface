import requests
from var.data import my_var as my_data

class Weather():
    def __init__(self,API_KEY):
        self._api_key = API_KEY

    def run(self,city_name="Jakarta",report_type="current"):
        if report_type == "current":
            # Current Weather
            complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self._api_key}&units=metric"
            response = requests.get(complete_url)
            data = response.json()
            self._current_weather(data)
        elif report_type == "forecast":
            # 5-day / 3-hour forecast API
            complete_url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={self._api_key}&q={city_name}"
            response = requests.get(complete_url)
            data = response.json()
        else: 
            raise ValueError('Please fill the correct report type. Default is: current')   

        self._data = data

    def check_data(self):
        '''check the data's key. Call this method after `run()`'''
        for key,_ in self._data.items():
            print(key)

    def _current_weather(self,data): 
        # "404", means city is found otherwise,
        if data["cod"] != "404":
            y = data["main"]
            z = data["weather"]

            my_data.lon = data['coord']['lon']
            my_data.lat = data['coord']['lat']

            my_data.city = data['name']
            my_data.temp_max = y["temp_max"]
            my_data.temp_min = y["temp_min"]
            my_data.feels_like = y["feels_like"]
            my_data.temp = y["temp"]
            my_data.pressure = y["pressure"]
            my_data.humidity = y["humidity"]
            my_data.sea_level = y['sea_level']
            my_data.ground_level = y['grnd_level']

            my_data.weather = z[0]['main']
            my_data.weather_description = z[0]["description"]

            # print following values
            # print(f"City Name: {data['name']}")
            # print(" Temperature = " +
            #                 str(temp) + "\u00b0 C (feels like: " + str(feels_like) + "\u00b0 C )"
            #     "\n atmospheric pressure = " +
            #                 str(pressure) + " hPa"
            #     "\n humidity = " +
            #                 str(humidity) + " %"
            #     "\n description = " +
            #                 str(weather_description))
        else:
            print(" City Not Found ")