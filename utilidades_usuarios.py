# -*- coding: utf-8 -*-

# Definimos la constante de acceso a los datos
bd_file = 'registros.txt'

from utilidades_documentos import *

## FUNCIONALIDADES GENERALES

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
    
    usuarios = cargar_info(bd_file)['usuarios']
    
    while validar_documento(documento,usuarios=usuarios) == False:
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
    rol = None
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

# FUNCIONALIDADES PROPIAS DE EL USUARIO ADMINISTRADOR

"""
    
    Funcionalidades de la Gestion de los centros

"""

def elegir_municipio() -> str:
    
    info = cargar_info(bd_file)

    opciones = {str(i+1):info['ciudades'][i] for i in range(len(info['ciudades']))}

    return info['ciudades'][int(menu(opciones))-1]

def elegir_estacion(municipio:str = None) -> str:

    if municipio is None:
        info = cargar_info(bd_file)

        centros = info['centros']
        opciones = {str(centro_id): f'Nombre: {centro["nombre"]}  Ciudad: {centro["ciudad"]}' for centro_id, centro in centros.items()}
        
        print('Se listaran los centros con su identificados por su numero de id, elije dicho numero para indicar cual quieres modificar')
        print()
        return menu(opciones)
    else:
        info = cargar_info(bd_file)

        centros = info['centros']
        opciones = {str(centro_id): f'Nombre: {centro["nombre"]}' for centro_id, centro in centros.items() if centro['ciudad']==municipio}
        limpiar_pantalla()
        print(f'Se listaran los centros con su identificados por su numero de id y que pertenecen a la ciudad de {municipio}')

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

def tiene_registros_asociados(centro_id, registros):
    for registro in registros[1:]:
        if 'centro_id' in registro and registro['centro_id'] == centro_id:
            return True
    return False

def elegir_estacion_eliminar():
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

def eliminar_estacion():
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

def elegir_usuario_actualizar(usr:str) -> int:

    info = cargar_info(bd_file)

    usuarios = info['usuarios']

    opciones = {
        str(i+1): f'Nombre: {usuarios[i]["nombre"]}  Rol: {usuarios[i]["rol"]} Documento: {usuarios[i]["id"]}' 
        for i in range(len(usuarios)) 
    }

    print('Se listarán los usuarios con su identificación por su número de ID, elige dicho número para indicar cuál quieres actualizar')
    print()

    return int(menu(opciones))-1

def elegir_nombre_usuario(nombre:str):
    
    print(f'Se te solicitara un nuevo nombre, dale enter si deseas que se mantenga el nombre actual ({nombre})')
    nombre_nuevo = ingresar_nombre()

    return nombre_nuevo if nombre_nuevo != '' else nombre

def actualizar_usuario(usr:str) -> None:

    limpiar_pantalla()

    indice_usuario = elegir_usuario_actualizar(usr)

    info = cargar_info(bd_file)

    usuario = info['usuarios'][indice_usuario]

    nuevo_nombre = elegir_nombre_usuario(usuario['nombre'])

    opciones = {'1':f'Mantener la contraseña ({usuario['clave']}):',
                '2':f'Cambiar la contrasña actual'}

    nueva_constraseña = usuario['clave'] if menu(opciones) == '1' else ingresar_clave()

    opciones = {'1':f'Mantener el rol ({usuario['rol']}):',
                '2':f'Cambiar el rol actual'}

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

def eliminar_usuario(usr):
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

def crear_usuario(usr):
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


# FUNCIONALIDADES PROPIAS DE EL USUARIO ADMINISTRADOR

"""
    
    Funcionalidades de la Gestion de Centros por los operadores

"""

def mostrar_medidas(id_estacion: str) -> None:
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

    limpiar_pantalla()
    print()
    print(f'REGISTROS CENTRO {id_estacion}')


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