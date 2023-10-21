import csv

lista_final = []

csv_file = open("carabineros.csv", "w", newline='', encoding="utf-8", errors='ignore')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['iddetalle', 'Nombre', 'Latitud', 'Longitud'])

with open("datos.txt", "r", encoding='utf-8',errors='ignore') as file:
    while True:
        linea = file.readline()
        if len(linea) == 0:
            break
        linea = linea.split("[[")[1]
        linea = linea.split("]]")[0]
        lista = linea.split("], [")
        for elem in lista:
            lista_c = elem.split(",")
            lista_c[0] = int(lista_c[0].strip())
            lista_c[1] = float(lista_c[1].strip())
            lista_c[2] = float(lista_c[2].strip())
            lista_c[3] = lista_c[3].strip().strip("\'")
            lista_final.append(lista_c)

for dato in lista_final:
    csv_writer.writerow((dato[0], dato[3], dato[1], dato[2]))
csv_file.close()