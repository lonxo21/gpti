from bs4 import BeautifulSoup
import requests
import csv

def variables(string):
    hola = string.split("[[")[1]
    hola = hola.split("]]")[0]
    hola = hola.split('],[')
    lista = []
    for elem in hola:
        kie = elem.split(",")
        kie.pop(3)
        lista.append(kie)
    for elem in lista:
        elem[0] = int(elem[0].strip().strip("\'"))
        elem[1] = float(elem[1].strip().strip("\'"))
        elem[2] = float(elem[2].strip().strip("\'"))
        elem[3] = elem[3].strip().strip("\'")
    return lista

""" 
source = requests.get('https://www.carabineros.cl/detalleUnidad.php').text

soup = BeautifulSoup(source, 'lxml')

select = soup.find('select', id="region")

regiones = []

for options in select.find_all('option'):
    valor = options["value"].strip()
    regiones.append(valor)

regiones.pop(0)

comunas = []

for region_id in regiones:
    com = requests.post("https://www.carabineros.cl/procedimientos/cargacomuna.php", data={"region": int(region_id)}).text
    soup = BeautifulSoup(com, 'lxml')
    options = soup.find_all('option')
    for opt in options:
        value = opt["value"].strip()
        if value != '':
            comunas.append(int(value))

print("COMUNAAAS")
print(comunas)
 """
comunas = [194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 230, 58, 61, 62, 73, 74, 80, 234, 235, 236, 237, 238, 240, 241, 242, 243, 245, 246, 247, 248, 255, 257]
datos_finales = []
print("DATOOSSS")

for comuna_id in comunas:
    com = requests.post('https://www.carabineros.cl/detalleUnidad.php', data={'comuna':comuna_id}).text
    soup = BeautifulSoup(com, 'lxml')
    script = soup.find('script', src="https://maps.googleapis.com/maps/api/js")
    script = script.find_next('script').text
    datos = variables(script)
    print(comuna_id, datos)
    datos_finales.append(datos)

print(datos_finales)

for dato in datos_finales:
    id_detalle = dato[0]
    com = requests.post('https://www.carabineros.cl/procedimientos/cargadetalleUnidad.php', data={'iddetalle':id_detalle}).text
    soup = BeautifulSoup(com, 'lxml')
    dir = soup.find('div', class_="about-box-text")
    tel = dir.find_next('div', class_="about-box-text")
    dir = dir.text.strip()[11:]
    tel = tel.text.strip()[6:]
    dato.append(dir)
    dato.append(tel)

print(datos_finales)

csv_file = open("carabineros.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nombre', 'Direccion', 'Telefono', 'Latitud', 'Longitud'])
for info in datos_finales:
    csv_writer.writerow((info[3], info[4], info[5], info[1], info[2]))

csv_file.close()

'''
soup2 = BeautifulSoup(hola, 'lxml')

select2 = soup.find('div', id='comunadiv')
print(select2.prettify())
'''