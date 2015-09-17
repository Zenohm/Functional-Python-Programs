def weather():
	import pywapi
	wi = pywapi.get_weather_from_noaa('KFWA')
	print("Temperature : " + wi['temp_c']+" C"+"\nWeather Condition : " + wi['weather']+"\nRelative Humidity : " + wi['relative_humidity']+"\nPressure : " + wi['pressure_string']+"\nWindchill : " + wi['windchill_c']+" C"+"\nWind Direction : " + wi['wind_dir']+"\nWind Speed : " + wi['wind_mph']+" MPH")
