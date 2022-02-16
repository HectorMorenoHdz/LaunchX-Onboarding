# Kata del modulo 1
from datetime import date

print("Today's date is: ", date.today())

parsecs = input("Introduzca los parsecs: ")

lightyears = int(parsecs) * 3.26156

print("Conversión- " + str(parsecs) + " parsecs equivalen a: " + str(lightyears) + " año luz.")