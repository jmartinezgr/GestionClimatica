# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:24:37 2023

@author: gita2
"""

def split(text: str, sep = ' ') -> list:
    '''
    Parametros
    ----------
    text : str
        Texto a combertir en lista.
    sep : str, optional
        Indicador para separar el texto. El valor por defecto es ' '.

    Returns
    -------
    list
        Lista con el texto separado según el separador.
    
    Ejemplo
    -------
    
    >>> split('cama, casa, cosa, comida, candado', ', ')
    ['cama', 'casa', 'cosa', 'comida', 'candado']

    '''   
    
    L = []
    i = 0
    j = len(sep)
    aux = ''
    while j < len(text) + len(sep):
        if sep == text[i:j]:
            L += [aux]
            aux = ''
            i += len(sep) - 1
            j += len(sep) - 1
        else:
            aux += text[i]
        j += 1
        i += 1
    return L + [aux]

def unir(items: list, sep: str) -> str:
    '''
    Combina los elementos de una lista en una cadena usando el separador dado.

    Parameters
    ----------
    items : list
        Lista de elementos a unir.
    sep : str
        Separador para unir los elementos.

    Returns
    -------
    str
        Cadena resultante después de unir los elementos con el separador.
    '''

    resultado = str(items[0])
    for item in items[1:]:
        resultado += str(sep) + str(item)
    return resultado

def is_digit(caracter: str) -> bool:
    '''
    Verifica si el carácter dado es un dígito.

    Parameters
    ----------
    caracter : str
        Carácter a verificar.

    Returns
    -------
    bool
        True si es un dígito, False de lo contrario.

    '''
    numeros =  [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
    ]

    return caracter in numeros

def limpiar_pantalla():
    '''
    Funcion que limpia la pantalla

    Returns
    -------
    None.

    '''
    import os
    os.system('cls')
    
def cargar_info(file_path: str) -> dict:
    '''
    Sinopsis
    --------
    
    Funció que solicita nombre del archivo de la base de datos para organizarla
    en datos estructurados. ESte archivo debe tener la estructura predefinida en
    clase para poder devolver la informacion de manera correcta
    
    Parámetros
    ----------
    file_path : str
        Nombre del archivo txt que contiene la información de los usuarios

    Returns
    -------
    dict
        Diccionario con la información extraída del txt.
        
    Ejemplo
    -------
    
    >>> cargar_info('registros_.txt')
    {
        'centros': {
            '1': {
                'ciudad': 'Medellín',
                'nombre': 'Universidad San Buenaventura'
                },
            ...
        },
        'ciudades': [
            'Medellín',
            'Bello',
            ...
        ],
        'registros': [  
            'PM10[0.0:100.0,ug/m3];PM25[0.0:200.0,ug/m3];Temperatura[-20.0:50.0,°C];Humedad[0.0:100.0,%]',
            {
                'centro_id': '1',
                'datos': ['3.5', '6.2', '27.0', '34.0'],
                'fecha': '2019-07-01 00:00:00'
            },
            {
                'centro_id': '2',
                'datos': ['8.1', '-999.0', '29.0', '37.0'],
                'fecha': '2019-07-01 00:10:00'
            },
            ...
        ],
        'usuarios': [
            {
                'clave': '1234',
                'id': '1010101010',
                'nombre': 'Mariana Montoya',
                'rol': 'Administrador'
            },
            ...
        ]
    }
    '''
    info = {
        'usuarios': [],
        'ciudades': [],
        'centros': {},
        'registros': []
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line.startswith('<'):
                # Información de usuarios
                parts = split(line[1:-1], ';')
                if len(parts) == 4:
                    info['usuarios'].append({
                        'id': parts[0],
                        'nombre': parts[1],
                        'clave': parts[2],
                        'rol': parts[3]
                    })
                else:
                    print(f"Error en el formato de la línea: {line}")

            elif line.startswith(':'):
                # Ciudades permitidas
                info['ciudades'] = split(line[1:], ',')
            elif line.startswith(('PM10', 'PM25', 'Temperatura', 'Humedad')):
                # Rangos y nombres de registros
                info['registros'].append(line)
            elif is_digit(line[0]):
                # Verificar formato antes de interpretar como información de centros
                parts = split(line, ',')
                if len(parts) == 3:
                    info['centros'][parts[0]] = {
                        'nombre': parts[1],
                        'ciudad': parts[2]
                    }
                else:
                    # Datos de registros
                    parts = split(line, ';')
                    if len(parts) == 3:
                        fecha = parts[0]
                        centro_id = (parts[1])
                        datos = parts[2][1:-1].split(',')
                        info['registros'].append({
                            'fecha': fecha,
                            'centro_id': centro_id,
                            'datos': datos
                        })
                    else:
                        print(f"Error en el formato de la línea: {line}")

    return info


def guardar_info(file_path: str, info: dict) -> None:
    '''
    Función que actualiza los datos de un archivo txt

    Parameters
    ----------
    file_path : str
        Nombre del archivo donde se guardan los datos.
    info : dict
        Estructura de datos a guardar.

    Returns
    -------
    None.

    '''
    with open(file_path, 'w', encoding='utf-8') as file:
        for usuario in info['usuarios']:
            file.write(f"<{usuario['id']};{usuario['nombre']};{usuario['clave']};{usuario['rol']}>\n")

        file.write(':'+ unir(info['ciudades'],',') +'\n')

        for centro_id, centro_info in info['centros'].items():
            file.write(f"{centro_id},{centro_info['nombre']},{centro_info['ciudad']}\n")

        file.write(info['registros'][0]+'\n')

        for registro in info['registros'][1:]:
            file.write(f"{registro['fecha']};{registro['centro_id']};{{{unir(registro['datos'],',')}}}\n")