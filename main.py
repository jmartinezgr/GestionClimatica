# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:59:27 2023

@author: gita2
"""

from utilidades_menu import *
from utilidades_documentos import *
from utilidades_usuarios import *

op = '-1'

while op != '3':
    op = menu_principal()
    if op != '3':     
        if op == '2':
            menu_invitado()
        elif op == '1':
            print()
            usr = login()
            if usr is not None:
                limpiar_pantalla()
                if usr[1] == 'Operador':
                    menu_operador(usr[0])
                else:
                    menu_administrador(usr[0])
        else:
                print('Error, has ingresado una opcion no valida, intentalo de nuevo')
    else:
        print('Gracias por usar el sistema! Nos vemos luego')