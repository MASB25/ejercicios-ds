#!/usr/bin/env python3
pasaje = int(input("Costo pasaje: "))
alojamiento = int(input("Costo alojamiento: "))
noches = int(input("Cantidad de noches: "))
dinero = int(input("Dinero disponible: "))
total = alojamiento * noches    
total+= pasaje
if dinero >= total:
   logico = True
else:
   logico = False

if logico:
   print(f"Te alcanza re bien crack")
else:
   print(f"Segui participando")

    
