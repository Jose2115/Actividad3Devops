import json
import os
from datetime import datetime

def procesar_datos():
    input_file = 'datos.json'
    log_file = 'backup.log'
    output_file = 'resultados.json'
    version = "1.0.0-manual" 

    if not os.path.exists(input_file):
        with open(input_file, 'w') as f:
            json.dump([{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}], f)

    with open(input_file, 'r') as f:
        data = json.load(f)

    filtrados = [item for item in data if item['status'] == 'active']
    mensaje_ejecucion = f"Se filtro {len(filtrados)} datos"
    print(mensaje_ejecucion) 

    with open(output_file, 'w') as f:
        json.dump(filtrados, f)

    log_entry = (
        f"{datetime.now()} | Archivo: {input_file} | "
        f"Resultado: {mensaje_ejecucion} | Versión: {version}\n"
    )
    
    with open(log_file, 'a') as f:
        f.write(log_entry)

if __name__ == "__main__":
    procesar_datos()