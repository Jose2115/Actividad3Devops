import json
import datetime
import os
import sys

def ejecutar_programa():
    # --- Configuración de archivos ---
    archivo_entrada = 'datos.json'  # (Punto a) 
    archivo_salida = 'resultados.json'  # (Punto c) 
    archivo_log = 'backup.log'  # (Punto d) 

    # a. Leer la información (JSON) 
    if not os.path.exists(archivo_entrada):
        print(f"Error: No se encontró el archivo {archivo_entrada}")
        return

    with open(archivo_entrada, 'r') as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            print("Error: El archivo no tiene un formato JSON válido.")
            return

    # b. Procesar la información como un filtro 
    # En este ejemplo, filtramos servidores con estado 'activo'
    datos_filtrados = [item for item in datos if item.get('estado') == 'activo']
    total_filtrados = len(datos_filtrados)

    # c. Generar un archivo con los resultados obtenidos 
    with open(archivo_salida, 'w') as f:
        json.dump(datos_filtrados, f, indent=4)

    # d. Entrada manual de identificador o versión 
    # Nota: En entornos automatizados (Docker/CodeBuild), se puede pasar vía echo
    if sys.stdin.isatty():
        version_id = input("Ingrese el identificador o versión del cambio: ")
    else:
        # Si no hay terminal interactiva, lee de la entrada estándar (pipe)
        version_id = sys.stdin.read().strip()
    
    if not version_id:
        version_id = "v1.0.0-default"

    # d. Registrar actividad y crear backup.log 
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Mensaje de consola requerido: "Se filtró xxxx datos" 
    resultado_msg = f"Se filtró {total_filtrados} datos"
    print(resultado_msg)

    # Formato del log: Fecha y Hora, Nombre archivo, Resultado, Identificador/Versión 
    linea_log = (f"FECHA: {fecha_hora} | "
                 f"ARCHIVO: {archivo_entrada} | "
                 f"RESULTADO: {resultado_msg} | "
                 f"VERSION: {version_id}\n")

    with open(archivo_log, 'a') as log:
        log.write(linea_log)

if __name__ == "__main__":
    ejecutar_programa()