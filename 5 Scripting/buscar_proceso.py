import os
import subprocess
import sys

try:
    nombre_proceso_ingresado = sys.argv[1].lower()
except IndexError:
    print("Indique el nombre de un proceso.")
    sys.exit()

p = subprocess.run("processinfo.exe", capture_output=True,
                   encoding="cp850")

# La estructura de la salida en pantalla del comando es la siguiente:
#
#  +------+-------------------------------------+---------------------+
#  | PID  | Process                             | User                |
#  +------+-------------------------------------+---------------------+
#  | 92   | conhost.exe                         | Usuario             |
#  | 604  | CCC.exe                             | Usuario             |
#  +------+-------------------------------------+---------------------+
#  

# Acá vía `strip()` quitamos el salto de línea al final de `p.stdout`.
# Luego separamos cada una de las líneas en elementos de una lista
# con `split("\n")`. Por último sacamos las primeras tres líneas (que
# conforman la cabecera de la tabla y no nos interesan) y la última
# (que son los guiones finales de la tabla) para quedarnos únicamente
# con las líneas que contienen información sobre los procesos.
lineas = p.stdout.strip().split("\n")[3:-1]

for linea in lineas:
    # De cada línea obtenemos las tres columnas por separado a partir
    # del carácter "|". Pero antes, dado que cada línea empieza y
    # termina también con ese carácter, lo sacamos vía *slicing*.
    columnas = linea[1:-1].split("|")
    # Tomamos el nombre del proceso y le sacamos los espacios
    # que lo suceden y preceden vía `strip()`.
    proceso = columnas[1].strip()
    # Chequeamos que el nombre del proceso actual coincida con el
    # que ingresó el usuario. Lo convertimos a minúscula para que
    # no distinga entre mayúsculas y minúsculas.
    if proceso.lower() == nombre_proceso_ingresado:
        pid = columnas[0].strip()
        try:
            usuario = columnas[2].strip()
        except IndexError:
            # En algunos procesos no aparece el usuario.
            usuario = ""
        print(f"PID: {pid}. Usuario: {usuario}.")
