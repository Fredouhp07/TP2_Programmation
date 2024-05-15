import json
import csv

# Fonction de conversion
def complexe_en_csv(nombre_complexe):
    return [nombre_complexe.real, nombre_complexe.imag]

# Création du fichier json
with open('data.json', 'r') as fichier_json:
    data = json.load(fichier_json)

# Conversion nombres complexes en csv
data_csv = complexe_en_csv(complex(nombre_complexe[0], nombre_complexe[1])) for nombre_complexe in data]

# Écriture des données
with open('output.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['réel', 'imaginaire']) # En-tête
    writer.writerows(data_csv)