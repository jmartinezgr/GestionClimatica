# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:14:59 2023

@author: gita2
"""
# Definimos la constante de acceso a los datos
bd_file = 'registros.txt'

from utilidades_documentos import *

def menu(opciones: dict) -> str:
    '''
    Función que muestra y retorna la opción seleccionada según un lsitado de opciones

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

def ingresar_documento():
    documento = input('ingrese el numero de documento: ')
    while validar_documento(documento) == False:
        print('Documento inválido, por favor verifique que sean solo números y sean 10 cifras.')
        documento = input('ingrese el numero de documento: ')
    return documento

def ingresar_nombre():
    nombre = input('ingrese el nombre: ')
    while validar_nombre(nombre) == False:
        print('Nombre inválido, verifique que solo contenga letras y espacios sencillos.')
        nombre = input('ingrese el nombre: ')
    return nombre

def ingresar_clave():
    clave = ''
    clave2 = ''
    while clave != clave2 or len(clave) < 4:
        if clave != '' or clave2 != '':
            print('Error, confirme que tenga más de 4 caracteres y que sean iguales.')
        clave = input('Ingrese la clave nueva: ')
        clave2 = input('Confirme la clave nueva: ')
    return clave

def ingresar_rol():
    roles = ['Administrador','Operador']
    rol = ''
    while rol not in roles:
        if rol != None:
            print('opción inválida, intente nuevamente')
        print('Elija el rol para este usuario:')
        for i in range(len(roles)):
            print('\t', str(i+1), ') ', roles[i], sep = '')
        rol = input()
        if rol.isnumeric():
            rol = int(rol)-1
            if 0 <= rol < len(roles):
                rol = roles[rol]
    return rol

def crear_usuario(usuarios):
    documento = ingresar_documento()
    if documento in usuarios.keys():
        print('Ese usuario ya existe')
        return False
    nombre = ingresar_nombre()
    clave = ingresar_clave()
    rol = ingresar_rol()

    usuarios[documento] = {}
    usuarios[documento]['nombre'] = nombre
    usuarios[documento]['clave'] = clave
    usuarios[documento]['rol'] = rol
    print(f'Felicidades, {nombre}, te has registrado exitosamente!')
    return True

def login():
    
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

def elegir_municipio() -> str:
    
    info = cargar_info(bd_file)

    opciones = {str(i+1):info['ciudades'][i] for i in range(len(info['ciudades']))}

    return info['ciudades'][int(menu(opciones))-1]

def elegir_estacion() -> str:

    info = cargar_info(bd_file)

    centros = info['centros']
    opciones = {str(centro_id): f'Nombre: {centro["nombre"]}  Ciudad: {centro["ciudad"]}' for centro_id, centro in centros.items()}
    
    print('Se listaran los centros con su identificados por su numero de id, elije dicho numero para indicar cual quieres modificar')
    print()
    return menu(opciones)

def elegir_nombre_estacion(nombre_centro:str) -> str:

    valor = True

    while valor:
        nombre = input(f'Ingresa el nuevo nombre o de enter para mantener el que ya esta ({nombre_centro}):')
        if not is_space(nombre) and not nombre == '':
            valor = validar_nombre(nombre)
            if valor:
                return nombre
        else:
            return nombre_centro

def crear_estacion():

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

def actualizar_estacion():
    limpiar_pantalla()
    print('Actualicemos una estacion')
    print()
    
    id_estacion = elegir_estacion()

    info = cargar_info(bd_file)

    nuevo_nombre = elegir_nombre_estacion(info['centros'][id_estacion]['nombre'])
    print(f'Elige la nueva ciudad, o ingresa el numero de la ciudad en la que esta actualmente ({info['centros'][id_estacion]['ciudad']}) para mantener el estado actual: ')
    print()
    nueva_ciudad = elegir_municipio()

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