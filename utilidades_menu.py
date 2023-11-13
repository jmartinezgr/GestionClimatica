# -*- coding: utf-8 -*-
from utilidades_usuarios import * 

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
    
def menu_principal() -> str:
    '''
    Sinopsis
    --------    
    Función que muestra el menú principal

    Returns
    -------
    str
        string con la opción seleccionada.

    '''
    #limpiar_pantalla()
    print('Menú principal')
    opciones = {
                '1':'Usuario registrado',
                '2':'Usuario invitado',
                '3':'Salir'}
    return menu(opciones)

#----------------------------------------------------------------------------------------------------------- 

def menu_invitado() -> None:
    '''
    Sinopsis
    --------     
    Función que muestra el menú de invitado
    '''
    limpiar_pantalla()
    print('Felicidades, entraste como modo invitado!')
    opciones = {'1':'Menú anterior',
                '2':'Visualizar estadisticas'}
    
    op = '-1'

    while op != '1':
        print('Menu Usuario Invitado')
        op = menu(opciones)
        if op != '1':
            if op == '2':   
                print()
                menu_invitado_estadisticas()
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()
    
def menu_invitado_estadisticas() -> None:
    '''
    Sinopsis
    --------    
    Función que muestra el menú para elegir el rango temporal en el que el usuario invitado quiere visualizar las estadisticas
    '''    
    limpiar_pantalla()
    opciones = {'1':'Menú anterior',
                '2':'7 ultimos dias',
                '3':'30 ultimos dias',
                '4':'Elegir fechas manualmente'}
    
    op = '-1'

    while op != '1':
        print('Menu Usuario Invitado')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                dias = 7
                print()
                limpiar_pantalla()
                variables = elegir_variables()
                print()
                limpiar_pantalla()
                print()
                ciudades = elegir_ciudades()
                limpiar_pantalla()

                if ciudades and variables:
                    menu_analisis_visitante(dias,variables,ciudades)
                else:
                    print('No puedes hacer analisis sin variables y/0 sin ciudades')
            elif op == '3':
                dias = 30
                limpiar_pantalla()
                variables = elegir_variables()
                limpiar_pantalla()
                ciudades = elegir_ciudades()
                limpiar_pantalla()
                if ciudades and variables:
                    menu_analisis_visitante(dias,variables,ciudades)
                else:
                    
                    print('No puedes hacer analisis sin variables y/0 sin ciudades')
            elif op == '4':
                flag = True

                while(flag):
                    dias = input('Ingrese una valor correspondiente a la cantidad de dias del analisis: ')
                    if [is_digit(x) for x in dias]:
                        if(dias != 0):
                            flag = False
                        else:
                            print('No se pueden analizar 0 dias')
                    else:
                        print('Error, numero no valido')
                limpiar_pantalla()
                dias = int(dias)
                limpiar_pantalla()
                variables = elegir_variables()
                limpiar_pantalla()
                ciudades = elegir_ciudades()

                if ciudades and variables:
                    menu_analisis_visitante(dias,variables,ciudades)
                else:
                    limpiar_pantalla()
                    print('No puedes hacer analisis sin variables y/0 sin ciudades')
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_analisis_visitante(dias: int, variables: list ,ciudades: list) -> None:
    '''
    Sinopsis
    --------    
    Función que muestra las opciones de analisis con las variables y ciudades elegidas paa el usuario visitante

    Parameters
    ----------
    dias : itn
        Cantidad de dias anteriores al actual sobre el que se hara el analisis
    variables: list
        Lista de variables sobre las que se hara el analisis
    ciudades: list
        Lista de ciudades sobre las que se hara el analisis

    Returns
    -------
    None.
    '''    
    limpiar_pantalla()
    opciones = {'1': 'Volver al menú anterior',
                '2': 'Visualizar Estadisticas',
                '3':'Exportar Estadisticas'}    

    op = '-1'

    while op != '1':
        print('Menu Usuario Invitado')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                mostrar_estadisticas(dias,variables,ciudades)
                print()
                limpiar_pantalla()
            elif op == '3':

                nombre_archivo = input('Ingresa un nombre para el archivo con tus Solicitudes:')
                print()
                exportar_estadisticas(dias,variables,ciudades,f'{nombre_archivo}.txt')  
                limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()
#-----------------------------------------------------------------------------------------------------------    
    
def menu_operador(usr:str) -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario operador luego de iniciar sesion

    Parameters
    ----------
    usr : str
        Cedula del usuario registrado

    Returns
    -------
    None.
    '''
    print("Felicidades, has ingresado!")
    opciones = {'1':'Menú anterior',
                '2':'Seleccionar Ciudad',
                }    
    op = '-1'

    while op != '1':
        print('Menu Usuario Operador')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                menu_operador_ciudad()
                limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_ciudad() -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones para que el usuario seleccione la ciudad de donde proviene los datos con los que va a inteactuar.
    '''
    opciones = {'1':'Menú anterior',
                '2':'Elegir Ciudad',
                } 
    op = '-1'

    while op != '1':
        limpiar_pantalla()
        print('Menu Usuario Operador: Elegir Ciudad')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                limpiar_pantalla()
                print()
                print('Elige el municipio:')
                municipio = elegir_municipio()
                limpiar_pantalla()
                print()
                menu_operador_estaciones(municipio)
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_estaciones(municipio: str) -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario operador para elegir el centro con el cual va a interactuar

    Parameters
    ----------
    municipio : str
        Nombre de la ciudad elegida

    Returns
    -------
    None.
    '''  
    opciones = {'1':'Menú anterior',
                '2':'Elegir Centro',
                } 
    op = '-1'

    print(municipio)

    while op != '1':
        limpiar_pantalla()
        print('Menu Usuario Operador: Elegir Centro')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                id_estacion = elegir_estacion(municipio)
                if id_estacion != '-1':
                    print()
                    menu_operador_centros(id_estacion)
                    limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_centros(id_estacion: str) -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario operador para interactuar con los datos de una estacion

    Parameters
    ----------
    id_estacion : str
        Identificador unico de la estacion elegida por el usuario

    Returns
    -------
    None.
    ''' 
    limpiar_pantalla()

    opciones = {'1':'Menú anterior',
                '2':'Mostrar Estadisticas',
                '3':'Agregar Registro'
                } 
    op = '-1'

    while op != '1':
        print(f'Menu Usuario Operador: Elegi una accion para el centro con id {id_estacion}')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                mostrar_medidas(id_estacion)
                limpiar_pantalla()
            elif op == '3':
                print()
                agregar_registro(id_estacion)
                limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

#----------------------------------------------------------------------------------------------------------- 

def menu_administrador(usr:str) -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario administrador luego de iniciar sesión

    Parameters
    ----------
    usr : str
        Cedula del usuario registrado

    Returns
    -------
    None.
    ''' 

    print("Felicidades, has ingresado!")
    opciones = {'1':'Menú anterior',
                '2':'Gestionar Estaciones',
                '3':'Gestionar Usuarios',
                '4':'Depuracion de registros inconsistentes'}
    
    op = '-1'

    while op != '1':
        print('Menu Usuario Administrador')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                menu_estaciones()
                limpiar_pantalla()
            elif op == '3':
                print()
                menu_manipulacion_usuarios(usr)
                limpiar_pantalla()
            elif op == '4':
                print()
                depurar_registro()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_estaciones() -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario administrador para interactuar con las estaciones
    ''' 

    opciones = {'1':'Menú anterior',
                '2':'Crear Estacion',
                '3':'Editar Estacion',
                '4':'Eliminar estacion'}
    
    op = '-1'

    while op != '1':
        limpiar_pantalla()
        print("Menu estaciones")
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                crear_estacion()
                limpiar_pantalla()
            elif op == '3':
                print()
                actualizar_estacion()
                limpiar_pantalla()
            elif op == '4':
                print()
                eliminar_estacion()
                limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_manipulacion_usuarios(usr: str) -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario administrador para interactuar con los usuarios

    Parameters
    ----------
    usr : str
        Cedula del usuario registrado

    Returns
    -------
    None.
    ''' 
    opciones = {'1':'Menú anterior',
                '2':'Crear Usuario',
                '3':'Editar Usuario',
                '4':'Eliminar Usuario'}
    
    op = '-1'

    while op != '1':
        limpiar_pantalla()
        print("Menu Usuarios")
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                crear_usuario(usr)
                limpiar_pantalla()
            elif op == '3':
                print()
                actualizar_usuario(usr)
                limpiar_pantalla()
            elif op == '4':
                print()
                eliminar_usuario(usr)
                limpiar_pantalla()
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def depurar_registro() -> None:
    '''
    Sinopsis
    --------       
    Función que muestras las opciones que tiene un usuario administrador para interactuar con la depuracion de datos
    ''' 
    opciones = {'1':'Menú anterior',
                '2':'Registros compartidos',
                '3':'Registos unidos'}
    
    op = '-1'

    while op != '1':
        limpiar_pantalla()
        print("Menu Usuarios")
        op = menu(opciones)
        if op != '1':
            if op == '2':
                print()
                registros_compartidos()
                limpiar_pantalla()
            elif op == '3':
                print()
                registros_unidos()
                limpiar_pantalla()  
            else:
                print()
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()