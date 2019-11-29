import pyowm

owm = pyowm.OWM('8b02f1beea4840f1ae5c3736e3ea68d3', language = "ru")

place = input("Погода. Введите город: ")

# Search for current weather in Novorossiysk (Russia)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

speed = w.get_wind()["speed"] #["deg"]
deg = w.get_wind()["deg"]
# humidity = w.get_humidity()["humidity"]

print( "В городе " + place + " сейчас " + w.get_detailed_status())
print( "   Температура сейчас " + str(temp) + "⁰C")
#print( "Ветер сейчас " + str(speed) + " м/сек, " + " Направление ветра " + str(deg) + "⁰C")

if deg >= 0 and deg <= 22.5:
	#deg = deg
	print("   Ветер - Северный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

elif deg > 22.5 and deg <= 67.5:
	print("   Ветер - Северо-Восточный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")
elif deg > 67.5 and deg <= 112.5:
	print("   Ветер - Восточный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

elif deg > 112.5 and deg <= 157.5:
	print("   Ветер - Юго-Восточный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")
elif deg > 157.5 and deg <= 202.5:
	print("   Ветер - Южный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

elif deg > 202.5 and deg <= 247.5:
	print("   Ветер - Юго-Западный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

elif deg > 247.5 and deg <= 292.5:
	print("   Ветер - Западный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

elif deg > 292.5 and deg <= 337.5:
	print("   Ветер - Северо-Западный, " + str(speed) + " м/сек., " + " Направление ветра " + str(deg) + "⁰")

else:
	print("	  Штиль " + str(deg) + ' м/сек')
# print("   Влажность воздуха - " + humidity + "%")
print('Справочно: ветер дует в компаc, течение из компаса :)')
#Direction of the wind

input()