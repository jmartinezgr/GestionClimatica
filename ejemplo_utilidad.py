# -*- coding: utf-8 -*-

from utilidades_documentos import imprimir_tabla
A = []
fila = [1,2,3,4]
A.append(fila)
fila = [10,20,30,40]
A.append(fila)
fila = [100,200,300,400]
A.append(fila)
print('tabla con celdas de 8(+2) caracteres de ancho')
imprimir_tabla(A,8)
print('tabla con celdas de 10(+2) caracteres de ancho')
imprimir_tabla(A,10)
#A=[]
print('tabla con celdas de distinto ancho')
imprimir_tabla(A,[6,8,4,2])
print('tabla con celdas de distinto ancho ancho y encabezado')
encabezado = ['Variable1','Variable2','Variable3','Variable4']
imprimir_tabla(A,[12,10,8,6],encabezado)

B=[]
B.append(['Variable1', 30.3])
B.append(['Variable2', 100.3])
B.append(['Variable3', 120.32])
imprimir_tabla(B,10)
imprimir_tabla(B,[10,7])