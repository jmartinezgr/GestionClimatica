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
    
def menu_administrador(usr:str):
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
    print(f'Felicidades, has ingresado')
    opciones = {'1':'Menú anterior'}
    menu(opciones)

def menu_operador(usr:str) -> None:
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
    print(f'Felicidades, has ingresado')
    opciones = {'1':'Menú anterior',
                '2':'Gestionar Estaciones',
                '3':'Gestionar Usuarios',
                '4':'Depuracion de registros inconsistentes'}
    
    op = '-1'

    while op != '1':
        print('Menu Usuario Operador')
        op = menu(opciones)
        if op != '1':
            if op == '2':
                menu_estaciones()
                limpiar_pantalla()
            elif op == '3':
                menu_manipulacion_usuarios(usr)
            elif op == '4':
                depurar_registro()
            else:
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
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
                depurar_registro()
            else:
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
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
    pass

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