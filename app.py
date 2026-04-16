
import json
import datetime
import os

def ejecutar_filtro():
    input_file = 'datos.json'
    log_file = 'backup.log'
    output_file = 'resultados.json'
    
    # 1. Leer información [cite: 3]
    try:
        with open(input_file, 'r') as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}")
        return

    # 2. Procesar (Filtro de datos) [cite: 4]
    # Ejemplo: Filtramos solo los registros con valor 'importante'
    filtrados = [d for d in datos if d.get('prioridad') == 'alta']
    cantidad = len(filtrados)

    # 3. Generar archivo de resultados [cite: 5]
    with open(output_file, 'w') as f:
        json.dump(filtrados, f, indent=4)

    # 4. Entrada manual de versión 
    version_id = input("Ingrese identificador o versión del cambio: ")

    # 5. Registro en backup.log 
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"{fecha_hora} | Archivo: {input_file} | "
                 f"Resultado: Se filtraron {cantidad} datos | Versión: {version_id}\n")
    
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    print(f"Ejecución completada. Se filtraron {cantidad} datos.")

if __name__ == "__main__":
    ejecutar_filtro()