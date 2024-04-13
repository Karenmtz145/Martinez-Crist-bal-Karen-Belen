from flask import Flask, jsonify
import platform
import subprocess

local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
hostname = platform.node()

# Crear la aplicación Flask con el nombre del módulo actual (__name__)
app = Flask(__name__)

# Definir la lista de tareas con la información de IP y hostname
tasks = [{'ip': local, 'hostname': hostname}]

# Definir la ruta para obtener las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Ejecutar la aplicación Flask si este script es el punto de entrada principal
if __name__ == '__main__':
    app.run(debug=True)
