import platform
import sys
import json
import subprocess
sistemaop = sys.platform  
sistema = platform.system()  
version = platform.win32_ver()  
hostname = platform.node()
marca_cpu = platform.processor()
info = {
    "sistema": sistema,
    "version": version,
    "tipo_so": sistemaop,
    "hostname": hostname,
    "marca_cpu": marca_cpu
}
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
info["direccion_ip_local"] = local
with open('informacion_sistema.json', 'w') as archivo:
    json.dump(info, archivo, indent=4)
print("La información del sistema se ha guardado en 'info_del-sistema.json'.")