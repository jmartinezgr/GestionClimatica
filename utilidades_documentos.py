# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:24:37 2023

@author: gita2
"""

from datetime import datetime
import os

"""

    Funciones propias usadas en las demas funciones, implementadas a mano y usadas en los contexto especificos de la solucion.

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

def is_alpha(char: str) -> bool:
    '''
    Verifica si el carácter dado es una letra (mayúscula o minúscula).
    
    Argumentos:
        char: Carácter a verificar
    return -> Boolean (True or False) si es una letra o no
    '''
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return char in letras

def is_space(char: str) -> bool:
    '''
    Verifica si el carácter dado es un espacio.
    
    Argumentos:
        char: Carácter a verificar
    return -> Boolean (True or False) si es un espacio o no
    '''
    return char == ' '

def mi_max(lista) -> int:
    '''
    Encuentra el numero mayor de una lista numerica
    
    Argumentos:
        list: Lista a verificar
    return -> Integer: Retorna el numero maximo o None si la lista estaba vacia
    '''
    
    if not lista:
        return None

    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

def limpiar_pantalla():
    '''
    Funcion que limpia la pantalla

    Returns
    -------
    None.

    '''
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

"""

    Funciones especificas para la lecutra y el guardado en la base de datos de la informacion

"""   
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

    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")
        return None

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

"""
    
    Funciones especificas de validacion de datos ingresados por el usuario

"""

def validar_nombre(nombre: str) -> bool:
    '''
    Valida nombre válido (solo letras y espacios)
    
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es válido o no
    '''
    return all(is_alpha(char) or is_space(char) for char in nombre)

def validar_documento(documento: str, usuarios: list) -> bool:
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
        usuarios: lista de usuarios para verificar duplicados
    return -> Boolean (True or False) si es válido o no
    '''
    # Verificar longitud y que todos los caracteres sean numéricos
    if len(documento) == 10 and all(is_digit(char) for char in documento):
        # Verificar que el documento no esté repetido en la lista de usuarios
        for usuario in usuarios:
            if 'id' in usuario and usuario['id'] == documento:
                print('Este numero de documento ya existe!')
                return False
        return True
    print('Recuerden que el documento solo puede estar compuesto por numero, y debe tener 10 cifras')
    return False

def validar_fecha(fecha: str) -> bool:
    '''
    Valida que un string corresponda a una fecha válida (con formato yyyy-mm-dd).
    
    Argumentos:
        fecha -> string a validar
    return -> Boolean (True or False) si es válido o no
    '''
    try:
        # Intentar crear un objeto datetime desde la cadena de fecha
        datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        # Capturar la excepción ValueError que se produce si el formato es incorrecto
        return False


"""
    Funciones especificas para el estilado de salidas de informacion

"""

def imprimir_tabla(tabla, ancho, encabezado=None, retornar=False):  
    ''' 
    Retorna una tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
        retornar: Booleano que indica si se retorna el valor o se imprime
    '''

    resultado = ''

    def dividir_fila(ancho, sep='-'):
        linea = ''
        for i in range(len(ancho)):
            linea += ('+' + sep * (ancho[i] - 1))
        linea = linea[:-1] + '+'
        nonlocal resultado
        resultado += linea + '\n'

    def imprimir_celda(texto, impresos, relleno):
        if type(texto) == type(0.0):
            texto = '{:^7.2f}'.format(texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n', ' ').replace('\t', ' ')
        nonlocal resultado
        if impresos + relleno < len(texto):
            resultado += texto[impresos:impresos + relleno]
            impresos += relleno
        elif impresos >= len(texto):
            resultado += ' ' * (relleno)
        else:
            resultado += texto[impresos:]
            resultado += ' ' * (relleno - (len(texto) - impresos))
            impresos = len(texto)
        return impresos

    def imprimir_fila(fila):
        nonlocal resultado
        impresos = []
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto) // (ancho[i] - 4)
            if len(texto) % (ancho[i] - 4) != 0:
                alto1 += 1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            resultado += '| '
            for j in range(len(fila)):
                relleno = ancho[j] - 3
                if j == len(fila) - 1:
                    relleno = ancho[j] - 4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    resultado += ' |\n'
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    resultado += ' | '
    
    if not len(tabla) > 0:
        return resultado
    if not type(tabla[0]) is list:
        return resultado
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho + 3] * ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i] += 3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return resultado
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado is not None:
        dividir_fila(ancho, '=')
        imprimir_fila(encabezado)
        dividir_fila(ancho, '=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)

    if retornar:
        return resultado
    else:
        print(resultado)