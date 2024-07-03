import time,os,msvcrt,csv
from funciones_ventas import *

while True:
    os.system("cls")
    print("SISTEMA DE VENTAS")
    print("1. Registrar nueva venta")
    print("2. Reporte de ventas historico")
    print("3. Reporte de ventas por producto")
    print("4. Reporte por formas de pago")
    print("5. Salir")
    opciones = (1,2,3,4,5)
    opc = validar_opc(opciones)
    if opc == 1:
        producto,cantidad,valor,tipo_de_pago,precio_total = registrar_venta()

    elif opc ==2:
        reporte_ventas_historico()
    elif opc ==3:
        reportes_ventas_productos()
    elif opc ==4:
        forma_pago()
    else:
        print("ADIOOOOS!!!")
        break
