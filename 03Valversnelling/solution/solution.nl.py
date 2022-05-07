input = input("Wat is de hoogte van de val?")
valhoogte = float(input)
g = 9.81

valkwadraat = 2 * valhoogte / g
valtijd = valkwadraat ** 0.5

valsnelheidkwadraat = 2 * valhoogte * g
valsnelheid = valsnelheidkwadraat ** 0.5


print("De val duurt " + str(valtijd) + "s.")
print("De snelheid bij neerkomen is " + str(valsnelheid) + "m/s.")
