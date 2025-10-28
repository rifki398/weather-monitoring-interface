from lib.weather import Weather
from lib.map import Map
from var.data import my_var
from gui.gui import launch

API_KEY_WEATHER = "INSERT_YOUR_API_HERE" # from OpenWeather

weather = Weather(API_KEY_WEATHER)
my_map = Map()

launch(weather,my_map)