# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:47:34 2023

@author: gita2
"""
from utilidades_documentos import *
from utilidades_usuarios import *

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
    
def menu_principal() -> str:
    '''
    Función que muestra el menú principal

    Returns
    -------
    TYPE
        string con la opción seleccionada.

    '''
    #limpiar_pantalla()
    print('Menú principal')
    opciones = {
                '1':'Usuario registrado',
                '2':'Usuario invitado',
                '3':'Salir'}
    return menu(opciones)

def menu_invitado():
    '''
    Función que muestra el menú de invitado

    Returns
    -------
    None.

    '''
    print('Felicidades, entraste como modo invitado, no puedes hacer nada...')
    opciones = {'1':'Menú anterior'}
    menu(opciones)
    
def menu_operador(usr:str):
    '''
    Función que muestra el menú cuando un usuario se registra

    Parameters
    ----------
    usr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    print(f'Felicidades, has ingresado!')
    opciones = {'1':'Menú anterior',
                '2':'Seleccionar Ciudad',
                }    
    op = '-1'

    while op != '1':
        print('Menu Usuario Operador')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                menu_operador_ciudad()
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_ciudad():
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
                municipio = elegir_municipio()
                limpiar_pantalla()
                menu_operador_estaciones(municipio)
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_estaciones(municipio:str):
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
                menu_operador_centros(id_estacion)
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_operador_centros(id_estacion: str):
    limpiar_pantalla()

    opciones = {'1':'Menú anterior',
                '2':'Mostrar Estdisticas',
                '3':'Agregar Registro'
                } 
    op = '-1'

    while op != '1':
        print(f'Menu Usuario Operador: Elegi una accion para el centro con id {id_estacion}')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                mostrar_medidas(id_estacion)
                limpiar_pantalla()
            elif op == '3':
                id_estacion = elegir_estacion()
                menu_operador_centros(id_estacion)
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()



def menu_administrador(usr:str) -> None:
    '''
    Función que muestra el menú cuando un usuario se registra

    Parameters
    ----------
    usr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    print(f'Felicidades, has ingresado!')
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
                menu_estaciones()
                limpiar_pantalla()
            elif op == '3':
                menu_manipulacion_usuarios(usr)
                limpiar_pantalla()
            elif op == '4':
                depurar_registro()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_estaciones():
    '''
    Función que muestra el menú cuando un usuario se registra

    Parameters
    ----------
    usr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    opciones = {'1':'Menú anterior',
                '2':'Crear Estacion',
                '3':'Editar Estacion',
                '4':'Eliminar estacion'}
    
    op = '-1'

    while op != '1':
        limpiar_pantalla()
        print(f'Menu estaciones')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                crear_estacion()
                limpiar_pantalla()
            elif op == '3':
                actualizar_estacion()
                limpiar_pantalla()
            elif op == '4':
                eliminar_estacion()
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def menu_manipulacion_usuarios(usr:str):
    '''
    Función que muestra el menú cuando un usuario se registra

    Parameters
    ----------
    usr : TYPE
        DESCRIPTION.

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
        print(f'Menu Usuarios')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                crear_usuario(usr)
                limpiar_pantalla()
            elif op == '3':
                actualizar_usuario(usr)
                limpiar_pantalla()
            elif op == '4':
                eliminar_usuario(usr)
                limpiar_pantalla()
            else:
                limpiar_pantalla()
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
                print()
    limpiar_pantalla()

def depurar_registro():
    '''
    Función que muestra el menú cuando un usuario se registra

    Parameters
    ----------
    usr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    pass