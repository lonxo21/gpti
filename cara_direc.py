import csv
import requests

key = "d3a90d37-7045-11ee-b823-7295962d211c"

csv_file = open("carabineros.csv", "r", encoding="utf-8")
csv_result = open("carabineros_final.csv", "w", newline='', encoding="utf-8", errors='ignore')
csv_reader = csv.reader(csv_file)
next(csv_reader)
csv_writer = csv.writer(csv_result)
csv_writer.writerow(['Nombre','Direccion','Latitud','Longitud'])

for i in range(977):
    linea = next(csv_reader)
    if len(linea) == 0:
        break
    nom = linea[1]
    lat = float(linea[2])
    lon = float(linea[3])
    try:
        hola = requests.get("https://api.geocode.farm/reverse/", params={"key": key, "lat": lat, "lon": lon}).json()
        resultado = hola['RESULTS']['result'][0]
        direccion = resultado['formatted_address']
    except:
        direccion = "None"
    csv_writer.writerow([nom, direccion, lat, lon])


csv_file.close()
csv_result.close()