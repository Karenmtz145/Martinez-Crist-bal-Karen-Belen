import json

# Nombre del archivo JSON
nombre_archivo = "informacion_sistema.json"

# Cargar el JSON desde el archivo
with open(nombre_archivo, 'r') as archivo:
    data = json.load(archivo)

# Imprimir el JSON cargado
print(data)