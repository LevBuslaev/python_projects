import pyowm

owm = pyowm.OWM('8b02f1beea4840f1ae5c3736e3ea68d3', language = "ru")

place = input("Погода. Введите город: ")

# Search for current weather in Novorossiysk (Russia)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

speed = w.get_wind()["speed"] #["deg"]
deg = w.get_wind()["deg"]

print( "В городе " + place + " сейчас " + w.get_detailed_status())
print( "Температура сейчас " + str(temp) + " градус(ов) Цельсия")
print( "Ветер сейчас " + str(speed) + " м/сек, " + " Направление ветра " + str(deg) + " градусов")

input()