from bs4 import BeautifulSoup
import requests
import csv

link_geocode = "https://api.geocode.farm/forward/"
key = "738eaf82-6fbe-11ee-b823-7295962d211c"

source = requests.get('https://www.pdichile.cl/pdi-mas-cercano').text

soup = BeautifulSoup(source, 'html.parser')


csv_file = open("pdi.csv", "w", newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nombre', 'Direccion', 'Telefono', 'Latitud', 'Longitud'])

for div in soup.find_all('div', class_='cardBaseItem contenidoPdimascercano'):
    nom = div.find('h3').text.strip().strip("\"")
    dir = div.find('div', class_='direccion').text.strip().strip("\"")[10:]
    if "@" in dir:
        continue
    tel = div.find('div', class_='telefono').text.strip().strip("\"")[9:]
    try:
        get_geo = requests.get(link_geocode, params={"key": key, "addr": dir}).json()
        results = get_geo['RESULTS']['result']['coordinates']
        lat = results['lat']
        lon = results['lon']
    except:
        lat = "None"
        lon = "None"
    csv_writer.writerow((nom, dir, tel, lat, lon))
csv_file.close()