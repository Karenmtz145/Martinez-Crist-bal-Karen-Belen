import urllib.request
import json

def obtener_chiste_aleatorio(tipo_chiste):
    url = f'https://v2.jokeapi.dev/joke/Any?type={tipo_chiste}&lang=es'
    with urllib.request.urlopen(url) as respuesta:
        datos = json.loads(respuesta.read().decode())

    if not datos['error']:
        if datos['type'] == 'single':
            chiste = datos['joke']
            return chiste
        elif datos['type'] == 'twopart':
            setup = datos['setup']
            entrega = datos['delivery']
            return f"{setup}\n{entrega}"
    else:
        return '¡No se pudo obtener un chiste hoy!'

def main():
    print("¡Bienvenido a la aplicación de chistes!")
    tipo_chiste = input("¿Qué tipo de chiste prefieres? (single/twopart): ").lower()

    if tipo_chiste == 'single' or tipo_chiste == 'twopart':
        chiste = obtener_chiste_aleatorio(tipo_chiste)
        print("\nAquí tienes tu chiste:")
        print(chiste)
    else:
        print("Tipo de chiste no válido. Por favor, elija 'single' o 'twopart'.")

if __name__ == "__main__":
    main()
