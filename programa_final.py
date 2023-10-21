import csv
import numpy as np
import requests

""" Este es un programa demo al que le das una dirección y te devuelve la pdi o comisaria mas cercana,
para calcular la latitud y longitud de la direccion se usa la api de geocode.farm (tiene 1000 consultas 
gratis diarias) """

key = "d3a90d37-7045-11ee-b823-7295962d211c"
link_geocode = "https://api.geocode.farm/forward/"

def distancia(point1,point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

direccion = input("Ingrese una dirección: ")
get_geo = requests.get(link_geocode, params={"key": key, "addr": direccion}).json()
results = get_geo['RESULTS']['result']['coordinates']
lat = float(results['lat'])
lon = float(results['lon'])
latlon = (lat, lon)

resultado = "None"
distancia_minima = 10000000000

pdi_csv = open("pdi_final.csv", "r", encoding="utf-8")
carabineros_csv = open("carabineros_final.csv", "r", encoding="utf-8")


pdi_reader = csv.reader(pdi_csv)
pdi_header = next(pdi_reader)

for linea in pdi_reader:
    latlon2 = (float(linea[3]), float(linea[4]))
    dist = distancia(latlon, latlon2)
    if dist < distancia_minima:
        distancia_minima = dist
        resultado = linea[0] + ". " + linea[1]

carabineros_reader = csv.reader(carabineros_csv)
carabineros_header = next(carabineros_reader)

for linea in carabineros_reader:
    latlon2 = (float(linea[2]), float(linea[3]))
    dist = distancia(latlon, latlon2)
    if dist < distancia_minima:
        distancia_minima = dist
        resultado = linea[0] + ". " + linea[1]

pdi_csv.close()
carabineros_csv.close()

""" Retorna el nombre del lugar. Y la dirección """
""" Eso :) """
print(resultado)