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

def obtener_tiempo_actual():
    # Obtener la fecha y hora actual
    tiempo_actual = datetime.now()

    # Formatear la fecha y hora según tus especificaciones
    formato = "%Y-%m-%d %H:%M:%S"
    tiempo_formateado = tiempo_actual.strftime(formato)

    return tiempo_formateado

def convertir_fecha(fecha_str: str) -> datetime:
    # Convierte una cadena de fecha a un objeto datetime
    return datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')

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
        rol = input('Elija una opcion que deseas: ')
        if is_digit(rol):
            rol = int(rol)-1
            if 0 <= rol < len(roles):
                rol = roles[rol]
    return rol

def id_digit(valor: str) -> bool:
    '''
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
        
        if opciones:
            print('Elige el centro: ')
            print(f'Se listaran los centros con su identificados por su numero de id y que pertenecen a la ciudad de {municipio}')

            return menu(opciones)
        else:
            print('No hay centros relacionados a esa ciudad!')
            opciones = {'1':'Volver al menú anterior'}
            
            menu(opciones)

            return '-1'

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

    limpiar_pantalla()

    info = cargar_info(bd_file)

    nuevo_nombre = elegir_nombre_estacion(info['centros'][id_estacion]['nombre'])
    limpiar_pantalla()
    print(f'Elige la nueva ciudad, o ingresa el numero de la ciudad en la que esta actualmente ({info['centros'][id_estacion]['ciudad']}) para mantener el estado actual: ')
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
    limpiar_pantalla()
    print(f'Se te solicitara un nuevo nombre, dale enter si deseas que se mantenga el nombre actual ({nombre})')
    nombre_nuevo = ingresar_nombre()

    return nombre_nuevo if nombre_nuevo != '' else nombre

def actualizar_usuario(usr:str) -> None:

    limpiar_pantalla()

    indice_usuario = elegir_usuario_actualizar(usr)

    info = cargar_info(bd_file)

    usuario = info['usuarios'][indice_usuario]

    nuevo_nombre = elegir_nombre_usuario(usuario['nombre'])
    limpiar_pantalla()
    opciones = {'1':f'Mantener la contraseña ({usuario['clave']}):',
                '2':f'Cambiar la contrasña actual'}

    nueva_constraseña = usuario['clave'] if menu(opciones) == '1' else ingresar_clave()
    
    limpiar_pantalla()
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

def agregar_registro(id_estacion:str) -> None:
    
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

def mostrar_estadisticas(dias:int, variables:list ,ciudades:list):
    
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

def exportar_estadisticas(dias: int, variables: list, ciudades: list, archivo_salida: str):
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