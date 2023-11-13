# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:59:27 2023

@author: gita2
"""

from utilidades_menu import menu_invitado,menu_administrador,menu_principal,menu_operador
from utilidades_documentos import limpiar_pantalla
from utilidades_usuarios import login

op = '-1'

limpiar_pantalla()

while op != '3':
    op = menu_principal()
    if op != '3':     
        if op == '2':
            menu_invitado()
        elif op == '1':
            print()
            usr = login()
            print()
            if usr is not None:
                limpiar_pantalla()
                print()
                if usr[1] == 'Operador':
                    print()
                    menu_operador(usr[0])
                else:
                    print()
                    menu_administrador(usr[0])
        else:
            limpiar_pantalla()
            print('Error, has ingresado una opcion no valida, intentalo de nuevo')
            print()
    else:
        print('Gracias por usar el sistema! Nos vemos luego')