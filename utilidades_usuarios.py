# -*- coding: utf-8 -*-

# Definimos la constante de acceso a los datos
bd_file = 'registros.txt'
bd_file2 = 'registrosv2.txt' 

from datetime import datetime
from utilidades_documentos import *


## FUNCIONALIDADES GENERALES|

def menu(opciones: dict) -> str:
    '''
    Sinopsis
    -------- 
    Función que muestra y retorna la opción seleccionada según un listado de opciones

    Parameters
    ----------
    opciones : dict
        Diccionioario que contiene como key las opciones posibles y de value las descripciones de estas opciones.

    Returns
    -------
    str
        string con la opción selccionada.

    '''
    while True:
        for k,v in opciones.items():
            print(k+') '+v)
        op = input("Elije la opcion que deseas: ")
        if op in opciones.keys():
            return op
        else:
            print("\nOpción no válida, intenta nuevamente")

def obtener_tiempo_actual() -> str:
    '''
    Sinopsis
    --------     
    Esta funcion retorna el tiempo actual formateado como un string de la manera: YYYY-MM-DD HH:MM:SS

    Returns
    -------
    str
        Retorna un string con la fecha de actual formateada.

    '''    
    
    # Obtener la fecha y hora actual
    tiempo_actual = datetime.now()

    # Formatear la fecha y hora según tus especificaciones
    formato = "%Y-%m-%d %H:%M:%S"
    tiempo_formateado = tiempo_actual.strftime(formato)

    return tiempo_formateado

def convertir_fecha(fecha_str: str) -> datetime:
    '''
    Sinopsis
    -------- 
    Función que recibe un string en formato YYYY-MM-DD HH:MM:SS y retorna un objeto datetime con la fecha recibida

    Parameters
    ----------
    fecha_str : str
        Fecha en formato YYYY-MM-DD HH:MM:SS

    Returns
    -------
    datetime
        Objeto datetime con la fecha ingresada por el usuario
    '''   
    # Convierte una cadena de fecha a un objeto datetime
    return datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')

def ingresar_documento() -> str:
    '''
    Sinopsis
    --------     
    Funcion que sirve para recolectar el documento del usuario y confirmar que cumpla las condiciones validandolo, 
    y retornarlo cuando sea un documento valido

    Returns
    -------
    str
        String con el documento del usuario verificado como documento valido

    '''

    documento = input('ingrese el numero de documento: ')
    
    usuarios = cargar_info(bd_file)['usuarios']
    
    while validar_documento(documento,usuarios=usuarios) == False:
        documento = input('ingrese el numero de documento: ')
    return documento

def ingresar_nombre():
    '''
    Sinopsis
    --------       
    Funcion que sirve para recolectar el nombre del usuario y confirmar que cumpla las condiciones validandolo, 
    y retornarlo cuando sea un nombre valido

    Returns
    -------
    str
        String con el  nombre del usuario verificado como nombre valido

    '''

    nombre = input('ingrese el nombre: ')
    while validar_nombre(nombre) == False:
        print('Nombre inválido, verifique que solo contenga letras y espacios sencillos.')
        nombre = input('ingrese el nombre: ')
    return nombre

def ingresar_clave():
    '''
    Sinopsis
    --------       
    Funcion que sirve para recolectar la clave del usuario y confirmar que cumpla las condiciones validandolo, 
    y retornarlo cuando sea una clave valido

    Returns
    -------
    str
        String con la clave del usuario verificado como ujna clave valido

    '''

    clave = ''
    clave2 = ''
    while clave != clave2 or len(clave) < 4:
        if clave != '' or clave2 != '':
            print('Error, confirme que tenga más de 4 caracteres y que sean iguales.')
        clave = input('Ingrese la clave nueva: ')
        clave2 = input('Confirme la clave nueva: ')
    return clave

def ingresar_rol():
    '''
    Sinopsis
    --------       
    Funcion que sirve para recolectar el rol del usuario y confirmar que cumpla las condiciones validandolo, 
    y retornarlo cuando sea un rol valido

    Returns
    -------
    str
        String con el rol del usuario verificado como ujna clave valido

    '''    
    
    roles = ['Administrador','Operador']
    rol = None
    while rol not in roles:
        if rol != None:
            print('opción inválida, intente nuevamente')
        print('Elija el rol para este usuario:')
        for i in range(len(roles)):
            print('\t', str(i+1), ') ', roles[i], sep = '')
        rol = input('Elija una opcion que deseas: ')
        if is_digit(rol):
            rol = int(rol)-1
            if 0 <= rol < len(roles):
                rol = roles[rol]
    return rol

def id_digit(valor: str) -> bool:
    '''
    Sinopsis
    --------      
    Verifica si el valor dado es un dígito o es 'ND'.

    Parameters
    ----------
    valor : str
        Valor a verificar.

    Returns
    -------
    bool
        True si es un dígito o 'ND', False de lo contrario.
    '''
    if valor == 'ND':
        return True

    dot_count = 0
    minus_count = 0

    for i, char in enumerate(valor):
        if char == '.':
            dot_count += 1
        elif char == '-':
            # Verificar que el guión esté solo al inicio
            if i != 0:
                return False
            minus_count += 1
        elif not char.isdigit():
            return False

    # Verificar que haya máximo un punto y el guión solo esté al inicio
    return dot_count <= 1 and minus_count <= 1


def ingresar_dato(ini: float, fin: float, name: str = '') -> float:
    '''
    Sinopsis
    --------        
    Funcion que recolecta los datos de los registros de variables ambientales verificando que este en el rango [ini,fin]

    Parameters
    ----------
    ini : float
        Valor inferior del dominio de la variable, la variable recolectada no puede ser menor a este valo
    fin : float
        Valor superior del dominio de la variable, la variable recolectada no puede ser mayor a este valor    
    name: str, optional
        Nombre de la variable que va a ser recolectada, por defecto es un string vacio
    
    Returns
    -------
    float
        Variable float que contiene el dato ingresado que cumple con pertenecer al dominion especifico

    '''    
    
    flag = True
    while flag:
        valor = input(f'Ingrese el valor de {name}, recuerde ingresar valores entre {ini} y {fin} o ND si no está disponible: ')

        if valor != 'ND':
            if id_digit(valor):
                valor_float = float(valor)
                if ini <= valor_float <= fin:
                    flag = False
                else:
                    print(f'El valor debe estar entre {ini} y {fin}. Inténtelo de nuevo.')
            else:
                print('Por favor, ingrese un valor numérico válido o "ND". Inténtelo de nuevo.')
        else:
            return -999.0
    return valor_float

"""

    Funciones referentes al acceso de usuarios registrados

"""


def login() -> list:
    '''
    Sinopsis
    --------     
    Funcion que sirve para iniciar sesion, recolecta la cedula y la clave para iniciar sesion, si se logra iniciar sesion antes de 
    3 intentos retorna el nombre y el rol del usuario, sino, retorna None

    Returns
    -------
    List
        [Nombre : str, Rol : str] Se retorna una lista con el nombre del usuario que inicio sesion y su rol, o None en caso de no haber podido acceder 

    '''

    info = cargar_info(bd_file)

    usuarios = info['usuarios']
    
    for i in range(3):
        usuario = input('Ingrese el documento del usuario: ')
        clave = input('Ingrese la contraseña del usuario: ')
        
        for user in usuarios:
            if user['id'] == usuario:
                if user['clave'] == clave:
                    return [usuario,user['rol']]
                else:
                   print(f'Error, la clave no corresponde, te quedan {3-i-1} intentos')   
        print(f'Error, los datos no corresponden a un usuario registrado, te quedan {3-i-1} intentos')  
    
    return None

# FUNCIONALIDADES PROPIAS DE EL USUARIO ADMINISTRADOR

"""
    
    Funcionalidades de la Gestion de los centros

"""

def elegir_municipio() -> str:
    '''
    Sinopsis
    --------       
    Función que permite al usuario elegir un municipio de una lista predefinida.

    Returns
    -------
    str
        Nombre del municipio seleccionado por el usuario.

    '''
    info = cargar_info(bd_file)

    # Crear un diccionario de opciones donde las claves son números y los valores son nombres de municipios
    opciones = {str(i+1): info['ciudades'][i] for i in range(len(info['ciudades']))}

    # Utilizar la función menu para que el usuario elija un número correspondiente a un municipio
    return info['ciudades'][int(menu(opciones)) - 1]

def elegir_estacion(municipio: str = None) -> str:
    '''
    Sinopsis
    --------    
    Función que permite al usuario elegir una estación de monitoreo, ya sea de todas las estaciones disponibles o solo de aquellas pertenecientes a un municipio específico.

    Parameters
    ----------
    municipio : str, optional
        El nombre del municipio del cual se quieren listar las estaciones, por defecto es None.

    Returns
    -------
    str
        El identificador de la estación seleccionada.

    '''

    if municipio is None:
        info = cargar_info(bd_file)

        centros = info['centros']
        opciones = {str(centro_id): f'Nombre: {centro["nombre"]}  Ciudad: {centro["ciudad"]}' for centro_id, centro in centros.items()}
        
        print('Se listarán los centros con su identificador por su número de id. Elige dicho número para indicar cuál quieres seleccionar.')
        print()
        return menu(opciones)
    else:
        info = cargar_info(bd_file)

        centros = info['centros']
        opciones = {str(centro_id): f'Nombre: {centro["nombre"]}' for centro_id, centro in centros.items() if centro['ciudad'] == municipio}
        limpiar_pantalla()
        
        if opciones:
            print(f'Elige el centro en la ciudad de {municipio}: ')
            print('Se listarán los centros con su identificador por su número de id.')

            return menu(opciones)
        else:
            print(f'No hay centros relacionados a la ciudad de {municipio}!')
            opciones = {'1': 'Volver al menú anterior'}
            
            menu(opciones)

            return '-1'

def elegir_nombre_estacion(nombre_centro:str) -> str:
    '''
    Sinopsis
    --------
    Función que permite al usuario elegir un nuevo nombre para una estación de monitoreo o mantener el nombre actual.

    Parameters
    ----------
    nombre_centro : str
        El nombre actual de la estación de monitoreo.

    Returns
    -------
    str
        El nuevo nombre seleccionado por el usuario o el nombre actual si no se ingresa ninguno.

    '''
    valor = True

    while valor:
        nombre = input(f'Ingresa el nuevo nombre o de enter para mantener el que ya esta ({nombre_centro}):')
        if not is_space(nombre) and not nombre == '':
            valor = validar_nombre(nombre)
            if valor:
                return nombre
        else:
            return nombre_centro

def crear_estacion() -> None:
    '''
    Sinopsis
    --------    
    Función que guía al usuario para crear una nueva estación de monitoreo, solicitando el nombre y la ciudad.
    '''
    limpiar_pantalla()
    print('Creemos una nueva estacion!')
    
    nombre = ingresar_nombre()
    ciudad = elegir_municipio()

    info = cargar_info(bd_file)

    # Encontrar la mayor clave existente
    mayores_claves = [int(clave) for clave in info['centros']]
    nueva_clave = str(mi_max(mayores_claves) + 1) if mayores_claves else '1'

    centro = {
        'ciudad': ciudad,
        'nombre': nombre
    }

    # Agregar el nuevo centro al diccionario
    info['centros'][nueva_clave] = centro

    # Guardar la información actualizada en el archivo
    guardar_info(bd_file, info)
    limpiar_pantalla()
    print(f"Centro agregado con éxito. Clave: {nueva_clave}")
    print()
    opciones = {'1':'Volver al menu anterior'}

    menu(opciones)

def actualizar_estacion() -> None:
    '''
    Sinopsis
    --------
    Función que guía al usuario para actualizar una estación de monitoreo existente, permitiendo cambiar su nombre y ciudad.
    '''
    limpiar_pantalla()
    print('Actualicemos una estacion')
    print()
    
    id_estacion = elegir_estacion()

    limpiar_pantalla()

    info = cargar_info(bd_file)

    nuevo_nombre = elegir_nombre_estacion(info['centros'][id_estacion]['nombre'])
    limpiar_pantalla()
    print(f"Elige la nueva ciudad, o ingresa el numero de la ciudad en la que esta actualmente ({info['centros'][id_estacion]['ciudad']}) para mantener el estado actual: ")
    print()
    nueva_ciudad = elegir_municipio()

    limpiar_pantalla()

    info['centros'][id_estacion] = {
        'ciudad': nueva_ciudad,
        'nombre': nuevo_nombre
    }

    guardar_info(bd_file,info)

    limpiar_pantalla()
    print(f"Centro modificado con éxito. Clave: {id_estacion} Nombre: {nuevo_nombre} Ciudad: {nueva_ciudad}")
    print()
    opciones = {'1':'Volver al menu anterior'}

    menu(opciones)

def tiene_registros_asociados(centro_id: str, registros:str ) -> bool:
    '''
    Sinopsis
    --------
    Verifica si un centro de monitoreo tiene registros asociados en la lista de registros proporcionada.

    Parameters
    ----------
    centro_id : str
        Identificador único del centro de monitoreo que se verificará.
    registros : list
        Lista de registros donde se buscará la asociación con el centro de monitoreo.

    Returns
    -------
    bool
        True si hay registros asociados al centro de monitoreo, False en caso contrario.

    '''    
    for registro in registros[1:]:
        if 'centro_id' in registro and registro['centro_id'] == centro_id:
            return True
    return False

def elegir_estacion_eliminar() -> str:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada según un listado de opciones de centros de monitoreo que no tienen registros asociados.

    Returns
    -------
    str or None
        Retorna el identificador de la estación seleccionada o None si no hay estaciones sin registros asociados.

    '''   
    info = cargar_info(bd_file)
    
    centros = info['centros']
    registros = info['registros']

    opciones = {
        str(centro_id): f'Nombre: {centro["nombre"]}  Ciudad: {centro["ciudad"]}' 
        for centro_id, centro in centros.items() 
        if not tiene_registros_asociados(str(centro_id), registros)
    }

    if not opciones:
        print("No hay estaciones sin registros asociados.")
        return None

    print('Se listaran los centros que no tienen registros relacionados con su identificados por su numero de id, elije dicho numero para indicar cual quieres eliminar')
    print('Si pretendia borrar un centro que no esta en la lista, primero debe eliminar los registros relacionados a este y volver a este menu')
    print()
    return menu(opciones)

def eliminar_estacion() -> None:
    '''
    Sinopsis
    --------
    Muestra y elimina una estación seleccionada que no tiene registros asociados.
    '''  
    limpiar_pantalla()
    print('Eliminemos una estación')
    print()

    id_estacion = elegir_estacion_eliminar()

    if id_estacion is None:
        # No hay estaciones sin registros asociados
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)
        return

    info = cargar_info(bd_file)

    nombre_estacion = info['centros'][id_estacion]['nombre']

    # Eliminar la estación del diccionario de centros
    del info['centros'][id_estacion]

    # Guardar la información actualizada en el archivo
    guardar_info(bd_file, info)

    limpiar_pantalla()
    print(f"Estación eliminada con éxito. Clave: {id_estacion} Nombre: {nombre_estacion}")
    print()
    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)


"""

    Funcionalidades de la Gestion de los usuarios

"""

def elegir_usuario_actualizar(_usr: str) -> int:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para actualizar un usuario según un listado de opciones.

    Parameters
    ----------
    usr : str
        Nombre del usuario actual.

    Returns
    -------
    Integer
        Índice del usuario seleccionado para actualizar.
    '''
    info = cargar_info(bd_file)

    usuarios = info['usuarios']

    opciones = {
        str(i+1): f'Nombre: {usuarios[i]["nombre"]}  Rol: {usuarios[i]["rol"]} Documento: {usuarios[i]["id"]}' 
        for i in range(len(usuarios)) 
    }

    print('Se listarán los usuarios con su identificación por su número de ID, elige dicho número para indicar cuál quieres actualizar')
    print()

    return int(menu(opciones))-1

def elegir_nombre_usuario(nombre: str) -> str:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para el nuevo nombre de usuario, con la opción de mantener el nombre actual.

    Parameters
    ----------
    nombre : str
        Nombre actual del usuario.

    Returns
    -------
    str
        Nuevo nombre seleccionado o nombre actual si se mantiene.
    '''
    limpiar_pantalla()
    print(f'Se te solicitará un nuevo nombre. Presiona enter si deseas mantener el nombre actual ({nombre})')
    nombre_nuevo = ingresar_nombre()

    return nombre_nuevo if nombre_nuevo != '' else nombre

def actualizar_usuario(usr:str) -> None:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para actualizar la información de un usuario.

    Parameters
    ----------
    usr : str
        Nombre del usuario que está realizando la actualización.

    Returns
    -------
    None
    '''
    limpiar_pantalla()

    indice_usuario = elegir_usuario_actualizar(usr)

    info = cargar_info(bd_file)

    usuario = info['usuarios'][indice_usuario]

    nuevo_nombre = elegir_nombre_usuario(usuario['nombre'])
    limpiar_pantalla()
    opciones = {'1':f"Mantener la contraseña ({usuario['clave']}):",
                '2':'Cambiar la contrasña actual'}

    nueva_constraseña = usuario['clave'] if menu(opciones) == '1' else ingresar_clave()
    
    limpiar_pantalla()
    opciones = {'1':f"Mantener el rol ({usuario['rol']}):",
                '2':'Cambiar el rol actual'}

    nuevo_rol = usuario['rol'] if menu(opciones) == '1' else ingresar_rol()

    info['usuarios'][indice_usuario] = {
        'id':usuario['id'],
        'nombre':nuevo_nombre,
        'clave':nueva_constraseña,
        'rol':nuevo_rol
    }

    # Guardar la información actualizada en el archivo
    guardar_info(bd_file, info)

    limpiar_pantalla()
    print(f"Usuario actualizado con éxito. ID: {usuario['id']} Nombre: {nuevo_nombre}")
    print()
    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)

def elegir_usuario_eliminar(usr) -> int:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para eliminar la información de un usuario.

    Parameters
    ----------
    usr : str
        Nombre del usuario actual que no se debe incluir en las opciones.

    Returns
    -------
    Integer
        Índice del usuario seleccionado para eliminar.
    '''    
    info = cargar_info(bd_file)

    usuarios = info['usuarios']

    opciones = {
        str(i+1): f'Nombre: {usuarios[i]["nombre"]}  Rol: {usuarios[i]["rol"]} Documento: {usuarios[i]["id"]}' 
        for i in range(len(usuarios)) 
        if usuarios[i]['id'] != usr
    }

    if not opciones:
        print("No hay usuarios disponibles para eliminar, solo existe el usuario actual.")
        return None

    print('Se listarán los usuarios con su identificación por su número de ID, elige dicho número para indicar cuál quieres eliminar, si nota un salto en las opciones es porque el usuario actual no se tiene en cuenta')
    print()

    return int(menu(opciones))-1

def eliminar_usuario(usr: str) -> None:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para eliminar la información de un usuario.

    Parameters
    ----------
    usr : str
        Nombre del usuario actual que no se debe incluir en las opciones.

    Returns
    -------
    None
    '''    
    limpiar_pantalla()
    print('Eliminemos un usuario')
    print()

    indice_usuario = elegir_usuario_eliminar(usr)

    if indice_usuario is None:
        # No hay usuarios disponibles para eliminar, o el usuario actual
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)
        return

    info = cargar_info(bd_file)

    usuario = info['usuarios'][indice_usuario]

    nombre_usuario = usuario['nombre']
    id_usuario = usuario['id']
    info['usuarios'].pop(indice_usuario)

    # Guardar la información actualizada en el archivo
    guardar_info(bd_file, info)

    limpiar_pantalla()
    print(f"Usuario eliminado con éxito. ID: {id_usuario} Nombre: {nombre_usuario}")
    print()
    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)

def crear_usuario(_usr: str) -> None:
    '''
    Sinopsis
    --------
    Muestra y retorna la opción seleccionada para crear un nuevo usuario.

    Parameters
    ----------
    usr : str
        Nombre del usuario actual que se está utilizando como referencia.

    Returns
    -------
    None
    '''  
    limpiar_pantalla()
    print('Creemos un usuario')
    
    nombre = ingresar_nombre()
    documento = ingresar_documento()
    rol = ingresar_rol()
    clave = ingresar_clave()

    info = cargar_info(bd_file)

    info['usuarios'].append(
        {
            'clave':clave,
            'id':documento,
            'nombre':nombre,
            'rol':rol
        }
    )

    # Guardar la información actualizada en el archivo
    guardar_info(bd_file, info)

    limpiar_pantalla()
    print(f"Usuario creado con éxito. ID: {documento} Nombre: {nombre}")
    print()
    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)

"""

    Depuracion de datos

"""

def registros_compartidos() -> None:
    '''
    Sinopsis
    --------    
    Grafica los registros compartidos entre dos archivos similares
    '''    
    info1 = cargar_info(bd_file)
    info2 = cargar_info(bd_file2)

    if info2 is not None:
        registros1 = info1['registros'][1:]
        registros2 = info2['registros'][1:]

        registros_compartidos=[
            [registro['centro_id'],registro['fecha']]+[dato for dato in registro['datos']]
            for registro in registros1+registros2 
            if registro in registros1 and registro in registros2
        ]

        registros_unicos = []
        for registro in registros_compartidos:
            if registro not in registros_unicos:
                registros_unicos.append(registro)

        print()
        print('REGISTROS COMPARTIDOS')

        nombres_unidades=[]
        linea = split(info1['registros'][0],';')
        for i in range(4):
            nombre, info = split(linea[i],'[')

            rango,unidad = split(info[:-1],',')

            nombres_unidades.append(f'{nombre} : {unidad}')

        # Construir la tabla
        encabezado = ['Centro ID','Fecha']+nombres_unidades

        # Imprimir la tabla usando la función imprimir_tabla
        imprimir_tabla(registros_unicos,[9,20,12,12,17,12],encabezado)


        print('Se imprimieron los registros duplicados!')
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

    else:
        print('NO EXISTE EL ARCHIVO DUPLICADO!')
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

def registros_unidos() -> None:
    '''
    Sinopsis
    --------    
    Grafica los registros unicos entre dos archivos similares
    '''    
    info1 = cargar_info(bd_file)
    info2 = cargar_info(bd_file2)

    if info2 is not None:
        registros1 = info1['registros'][1:]
        registros2 = info2['registros'][1:]

        registros_unidos = [
            [registro['centro_id'], registro['fecha']] + [dato for dato in registro['datos']]
            for registro in registros1 + registros2
        ]

        # Eliminar registros duplicados
        registros_unicos = []
        for registro in registros_unidos:
            if registro not in registros_unicos:
                registros_unicos.append(registro)

        print()
        print('REGISTROS UNIDOS')

        nombres_unidades = []
        linea = split(info1['registros'][0], ';')
        for i in range(4):
            nombre, info = split(linea[i], '[')

            rango, unidad = split(info[:-1], ',')

            nombres_unidades.append(f'{nombre} : {unidad}')

        # Construir la tabla
        encabezado = ['Centro ID', 'Fecha'] + nombres_unidades

        # Imprimir la tabla usando la función imprimir_tabla
        imprimir_tabla(registros_unicos, [9, 20, 12, 12, 17, 12], encabezado)

        print('Se imprimieron todos los registros unidos!')
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

    else:
        print('NO EXISTE EL ARCHIVO DUPLICADO!')
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

# FUNCIONALIDADES PROPIAS DE EL USUARIO OPERADOR

"""
    
    Funcionalidades de la Gestion de Centros por los operadores

"""

def mostrar_medidas(id_estacion: str) -> None:
    '''
    Sinopsis
    --------     
    Muestra los registros de medidas para una estación específica.

    Parameters
    ----------
    id_estacion : str
        Identificador de la estación para la cual se mostrarán los registros.

    Returns
    -------
    None
    '''    
    info = cargar_info(bd_file)

    registros = info['registros']

    # Filtrar registros para obtener solo aquellos relacionados con la estación específica
    registros_estacion = [ 
        [registro['centro_id'],registro['fecha']]+[dato for dato in registro['datos']]
        for registro in registros[1:] 
        if registro['centro_id'] == id_estacion]

    if not registros_estacion:
        print("No hay registros para mostrar.")
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

        return

    print()
    print(f'REGISTROS CENTRO CON ID: {id_estacion}')

    # Obtener nombres y unidades desde el primer elemento de la lista de registros
    nombres_unidades=[]
    linea = split(registros[0],';')
    for i in range(4):
        nombre, info = split(linea[i],'[')

        rango,unidad = split(info[:-1],',')

        nombres_unidades.append(f'{nombre} : {unidad}')

    # Construir la tabla
    encabezado = ['Centro ID','Fecha']+nombres_unidades

    # Imprimir la tabla usando la función imprimir_tabla
    imprimir_tabla(registros_estacion,[9,20,12,12,17,12],encabezado)

    print('Se ha impreso la informacion disponible para este centro!')
    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)

def agregar_registro(id_estacion: str) -> None:
    '''
    Sinopsis
    --------     
    Agrega un nuevo registro de medidas para una estación específica.

    Parameters
    ----------
    id_estacion : str
        Identificador de la estación para la cual se agregarán los registros.

    Returns
    -------
    None
    '''    
    info = cargar_info(bd_file)

    limpiar_pantalla()

    registros = info['registros']
    nombres_unidades=[]
    linea = split(registros[0],';')
    for i in range(4):
        nombre, infos = split(linea[i],'[')

        rango,unidad = split(infos[:-1],',')

        rango_inf, rango_sup = split(rango,':')

        nombres_unidades.append(ingresar_dato(float(rango_inf),float(rango_sup),nombre))

    info['registros'].append({
        'fecha': obtener_tiempo_actual(),
        'centro_id': id_estacion,
        'datos': nombres_unidades
    })

    guardar_info(bd_file,info)
    
    limpiar_pantalla()

    print('Se ha guardado en nuevo registro para el centro!')

    opciones = {'1': 'Volver al menú anterior'}
    menu(opciones)

#Usuario Invitado

"""

    Funciones dedicadas al uso de los usuarios invitados en la aplicacion

"""

def elegir_variables() -> list:
    '''
    Sinopsis
    --------     
    Muestra y retorna las variables seleccionadas para el análisis.

    Returns
    -------
    list
        Lista de índices de las variables seleccionadas.
    '''    
    info = cargar_info(bd_file)

    limpiar_pantalla()

    registros = info['registros']
    variables_elegidas=[]
    linea = split(registros[0],';')
    for i in range(4):
        nombre, infos = split(linea[i],'[')

        rango,unidad = split(infos[:-1],',')

        rango_inf, rango_sup = split(rango,':')

        print(f'Deseas analizar la variable {nombre}')

        opciones = {'1':'Si',
                    '2':'No'}
        
        if menu(opciones) == '1':
            variables_elegidas.append(i)

    return variables_elegidas

def elegir_ciudades() -> list:
    '''
    Sinopsis
    --------     
    Muestra y retorna las ciudades seleccionadas para el análisis.

    Returns
    -------
    list
        Lista de índices de las variables seleccionadas.
    '''   
    info = cargar_info(bd_file)
    
    ciudades = info['ciudades']

    ciudades_elegidas = []

    for ciudad in ciudades:
        print(f'Deseas analizar la ciudad {ciudad}')

        opciones = {'1':'Si',
                    '2':'No'}
        
        if menu(opciones) == '1':
            ciudades_elegidas.append(ciudad)

    return ciudades_elegidas

def mostrar_estadisticas(dias:int, variables:list ,ciudades:list) -> None:
    '''
    Sinopsis
    --------     
    Muestra estadísticas de las variables seleccionadas en un periodo de días y ciudades específicas.

    Parameters
    ----------
    dias : int
        Número de días hacia atrás desde la fecha actual para incluir en las estadísticas.
    variables : list
        Lista de índices de las variables a incluir en las estadísticas.
    ciudades : list
        Lista de nombres de ciudades para incluir en las estadísticas.

    Returns
    -------
    None
    '''      
    info = cargar_info(bd_file)

    registros = info['registros']
    centros = info['centros']

    fecha_actual = datetime.now()

    nombre_variables = []
    unidades_variables = []
    linea = split(registros[0],';')
    for i in range(4):

        nombre, infos = split(linea[i],'[')
        rango,unidad = split(infos[:-1],',')
        rango_inf, rango_sup = split(rango,':')

        if i in variables:
            nombre_variables.append(nombre)
            unidades_variables.append(unidad)


    registros_filtrados = [
        registro for registro in registros[1:]
        if (fecha_actual - convertir_fecha(registro['fecha'])).days <= dias and 
        centros[registro['centro_id']]['ciudad'] in ciudades
    ] 
    
    if registros_filtrados:
        for i in range(len(variables)):
            variable = variables[i]
            nombre = nombre_variables[i]

            menor = 1000
            mayor = -1000
            promedio = 0
            centros_re = ['', '']
            fechas = ['', '']
            suma = 0

            for registro in registros_filtrados:
                datos = registro['datos']
               
                if float(datos[variable]) > mayor:
                    mayor = float(datos[variable])
                    centros_re[0] = centros[registro['centro_id']]['nombre']
                    fechas[0] = registro['fecha']

                if float(datos[variable]) < menor and float(datos[variable]) != -999.0:
                    menor = float(datos[variable]) 
                    centros_re[1] = centros[registro['centro_id']]['nombre']
                    fechas[1] = registro['fecha']

                promedio += float(datos[variable]) if float(datos[variable]) != -999.0 else 0
                suma += 1 if float(datos[variable]) != -999.0 else 0
            encabezados = [nombre, 'Valor', 'Centro', 'Fecha']
            data = []

            suma = 1 if suma == 0 else suma
            data.append(['Minimo', menor, centros_re[1], fechas[1]])
            data.append(['Maximo', mayor, centros_re[0], fechas[0]])
            data.append(['Promedio', promedio / suma, 'NA', 'NA'])
 
            imprimir_tabla(data, [8, 8, 25, 25], encabezados)
            print()
    
        print('Se han mostrado las estadisticas')

        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)
    else:
        print('No se han encontrado datos para mostrar con tus peticiones!')
        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)

def exportar_estadisticas(dias: int, variables: list, ciudades: list, archivo_salida: str) -> None:
    '''
    Sinopsis
    --------     
    Muestra estadísticas de las variables seleccionadas en un periodo de días y ciudades específicas.

    Parameters
    ----------
    dias : int
        Número de días hacia atrás desde la fecha actual para incluir en las estadísticas.
    variables : list
        Lista de índices de las variables a incluir en las estadísticas.
    ciudades : list
        Lista de nombres de ciudades para incluir en las estadísticas.
    archivo_salida :str
        Nombre que se le pondra al documento o del documento que se sobreescribira con las estadisticas especificas

    Returns
    -------
    None
    '''
    info = cargar_info(bd_file)

    registros = info['registros']
    centros = info['centros']

    fecha_actual = datetime.now()

    nombre_variables = []
    unidades_variables = []
    linea = split(registros[0], ';')
    for i in range(4):
        nombre, infos = split(linea[i], '[')
        rango, unidad = split(infos[:-1], ',')
        rango_inf, rango_sup = split(rango, ':')

        if i in variables:
            nombre_variables.append(nombre)
            unidades_variables.append(unidad)

    registros_filtrados = [
        registro for registro in registros[1:]
        if (fecha_actual - convertir_fecha(registro['fecha'])).days <= dias and
        centros[registro['centro_id']]['ciudad'] in ciudades
    ]

    if registros_filtrados:
        with open(archivo_salida, 'w',encoding='utf-8') as file:
            file.write('Estadisticas Solicitas: '+ '\n\n')
            for i in range(len(variables)):
                variable = variables[i]
                nombre = nombre_variables[i]

                menor = 1000
                mayor = -1000
                promedio = 0
                centros_re = ['', '']
                fechas = ['', '']
                suma = 0

                for registro in registros_filtrados:
                    datos = registro['datos']

                    if float(datos[variable]) > mayor:
                        mayor = float(datos[variable])
                        centros_re[0] = centros[registro['centro_id']]['nombre']
                        fechas[0] = registro['fecha']

                    if float(datos[variable]) < menor and float(datos[variable]) != -999.0:
                        menor = float(datos[variable])
                        centros_re[1] = centros[registro['centro_id']]['nombre']
                        fechas[1] = registro['fecha']

                    promedio += float(datos[variable]) if float(datos[variable]) != -999.0 else 0
                    suma += 1 if float(datos[variable]) != -999.0 else 0

                encabezados = [nombre, 'Valor', 'Centro', 'Fecha']
                data = []

                suma = 1 if suma == 0 else suma
                data.append(['Minimo', menor, centros_re[1], fechas[1]])
                data.append(['Maximo', mayor, centros_re[0], fechas[0]])
                data.append(['Promedio', promedio / suma, 'NA', 'NA'])

                tabla = imprimir_tabla(data, [8, 8, 25, 25], encabezados, retornar=True)
                file.write(tabla + '\n\n')

        print(f'Se han exportado las estadísticas a {archivo_salida}')

        opciones = {'1': 'Volver al menú anterior'}
        menu(opciones)
    else:
        print('No se han encontrado datos para exportar con tus peticiones!')