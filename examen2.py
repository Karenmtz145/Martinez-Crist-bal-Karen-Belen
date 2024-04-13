import requests

url = "http://127.0.0.1:5000/tasks"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud exitosa')
else:
    print('Error en la solicitud' , response.text)

print(data)