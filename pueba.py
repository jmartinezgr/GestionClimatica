from utilidades_documentos import *
from pprint import pprint

# Ejemplo de uso
file_path = 'registros_.txt'
info = cargar_info(file_path)

pprint(info)

# Agregar nuevos usuarios, ciudades, centros o registros según tus necesidades
info['ciudades'].append('Marinilla')

# Aquí puedes agregar nuevos registros
info['registros'].append('2023-02-01 00:00:00;1;{1.0,2.0,3.0,4.0}')

guardar_info(file_path, info)
