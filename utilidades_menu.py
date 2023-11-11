# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:47:34 2023

@author: gita2
"""
# Definimos la constante de acceso a los datos

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
    print(f'Felicidades, has ingresado')
    opciones = {'1':'Menú anterior',
                '2':'Gestionar Estaciones',
                '3':'Gestionar Usuarios',
                '4':'Depuracion de registros inconsistentes'}
    
    op = -1

    while op != 1:
        op = menu(opciones)
        if op != 1:
            if op == '2':
                menu_estaciones()
            elif op == '3':
                menu_usuarios()
            elif op == '4':
                depurar_registro()
            else:
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')

