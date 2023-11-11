# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:14:59 2023

@author: gita2
"""

bd_file = 'registros.txt'

from utilidades_documentos import *

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