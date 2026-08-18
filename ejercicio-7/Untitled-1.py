#!/usr/bin/env python3

def analizar_temperaturas(registro):
    minimini = min(registro)
    maximo = max(registro)
    promedio = sum(registro) / len(registro)
    tupla = (maximo, minimini, promedio)
    return tupla

temperaturas = [12,55,55,23,44,55]
temp_max, temp_min, temp_promedio = analizar_temperaturas(temperaturas)
print(f"La temperatura maxima fue {temp_max}, la minima {temp_min}, el promedio {temp_promedio}")
      