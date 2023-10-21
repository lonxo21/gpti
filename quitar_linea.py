import csv

""" file = open('carabineros_final.csv', 'r', encoding="utf-8")
file_write = open("carab.csv", "w", newline='', encoding="utf-8", errors='ignore')
reader = csv.reader(file)
writer = csv.writer(file_write)

for linea in reader:
    if len(linea) == 0:
        continue
    else:
        writer.writerow(linea)

file.close()
file_write.close()
 """
uwu = open('carabineros_final.csv', 'a', encoding="utf-8")
ola = csv.writer(uwu)
ola.writerow([12,12,12,56])
ola.writerow(['uwu','uwu','uwu','uwu'])
uwu.close()