import re
import os

def buscar_y_generar_reporte(archivo, cadenas_buscadas):
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()

    # Inicializar el reporte
    reporte = "# Informe de Búsqueda\n\n"

    for cadena_buscada in cadenas_buscadas:
        # Buscar ocurrencias y contarlas
        ocurrencias = [(m.start(), m.end()) for m in re.finditer(cadena_buscada, contenido, re.IGNORECASE)]
        cantidad_ocurrencias = len(ocurrencias)

        # Agregar al informe
        reporte += f"## Resultados para '{cadena_buscada}' ({cantidad_ocurrencias} ocurrencias)\n\n"

        for i, (inicio, fin) in enumerate(ocurrencias, 1):
            contexto_inicio = max(0, inicio - 50)
            contexto_fin = min(len(contenido), fin + 50)

            contexto = contenido[contexto_inicio:contexto_fin].replace('\n', ' ')
            enlace = f"[Contexto]({archivo}#L{i}): ...{contexto}..."

            reporte += f"### Ocurrencia {i}\n"
            reporte += f"{enlace}\n\n"

    # Guardar el informe en un archivo Markdown
    with open('informe_busqueda.md', 'w', encoding='utf-8') as reporte_file:
        reporte_file.write(reporte)

# Ruta del archivo de exportación
ruta_del_archivo = 'ruta_del_archivo.txt'

# Cadenas que estás buscando
cadenas_buscadas = ['cadena1', 'cadena2', 'cadena3']

# Realizar la búsqueda y generar el informe
buscar_y_generar_reporte(ruta_del_archivo, cadenas_buscadas)
