def getWeatherData():
    import pywapi,random
    weather = pywapi.get_weather_from_weather_com('46776')
    conditions = []
    app = conditions.append
    if weather['current_conditions']['wind']['speed'] == 'calm':
        app(0)
    else:
        app(float(weather['current_conditions']['wind']['speed']))
    
    app(float(weather['current_conditions']['wind']['direction']))
    app(float(weather['current_conditions']['feels_like']))
    app(float(weather['current_conditions']['humidity']))
    app(float(weather['current_conditions']['uv']['index']))
    app(float(weather['current_conditions']['temperature']))
    app(float(weather['current_conditions']['visibility']))
    app(float(weather['current_conditions']['dewpoint']))
    app(float(weather['current_conditions']['barometer']['reading']))
    app(float(weather['current_conditions']['icon']))
    conditions = [item + random.random()/100000 for item in conditions[:]]
    return conditions
