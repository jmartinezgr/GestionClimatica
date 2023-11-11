from utilidades_documentos import *
from utilidades_usuarios import elegir_municipio
from pprint import pprint


# Ejemplo de uso
file_path = 'registros.txt'
info = cargar_info(file_path)

pprint(info)

# Agregar nuevos usuarios, ciudades, centros o registros según tus necesidades
info['ciudades'].append('Marinilla')

# Aquí puedes agregar nuevos registros
info['registros'].append({
                'centro_id': '1',
                'datos': [1.0,2.0,3.0,4.0],
                'fecha': '2023-02-01 00:00:00'
            })

guardar_info(file_path, info)
"""
print(elegir_municipio())
"""