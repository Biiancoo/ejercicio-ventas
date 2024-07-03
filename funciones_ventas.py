import os,time,msvcrt, csv
datos_ventas=[]
total_efectivo=0
total_credito=0
total_debito=0
efectivo=0
credito=0
debito=0

def validar_opc(opciones):
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc in opciones:
                return opc
            else:
                print("Ingrese una opcion valida!")
        except:
            print("Debe ingresar la opcion en valir numerico!")


def registrar_venta():
    os.system("cls")
    while True:
        print("REGISTRAR VENTA")
        producto = input("Ingrese nombre del producto: ")
        if len(producto) >2 and len(producto)<14 and producto.strip and producto.lower():
            print("Poductor guardado!")
            break
        else:
            print("Ingrese el nombre del producto correctamente")

    while True:
        os.system("cls")
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad >=1 and cantidad <=100:
                print("Cantidad guardada!")
                break
            else:
                print("ERROR, debe ingresar una cantidad aceptada (1-100)")


        except:
            print("ERROR,debe ingresar el valor en valor numerico")

    while True:
        os.system("cls")
        try:
            valor = int(input("Ingrese valor del producto: "))
            if valor >=100 and valor <10000000:
                print("Valor guardado!")
                break
            else:
                print("ERROR,debe ingresar una valor dentro del rango (100-10.000.000)")


        except:
            print("ERROR,debe ingresar el valor en numeros enteros")

    precio_total = valor * cantidad
    while True:
        os.system("cls")
        opciones_pago=(1,2,3)
        print("MEDIOS DE PAGO")
        print("1. Efectivo")
        print("2. Credito")
        print("3. Debito")
        tipo_de_pago = validar_opc(opciones_pago)
        print("Metodo de pago guardado")
        break
         
    if tipo_de_pago ==1:
        efectivo = efectivo + 1
        total_efectivo = total_efectivo + precio_total
    elif tipo_de_pago ==2:
        credito = credito + 1
        total_credito = total_credito + precio_total
    else:
        debito = debito + 1
        total_debito = total_debito + precio_total



    datos=[producto,cantidad,valor,precio_total,tipo_de_pago]
    datos_ventas.append(datos)
    

    with open ('registro_ventas.csv','a',newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)
        

    return producto,cantidad,valor,tipo_de_pago,precio_total





def reporte_ventas_historico():
    with open('registro_ventas.csv', 'r', newline="") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(f"Producto: {fila[0]} Cantidad: {fila[1]} Valor del producto: {fila[2]} Tipo de pago: {fila[3]} Precio total de la venta: {fila[4]}")
    
    time.sleep(3)



def reportes_ventas_productos():
    with open('registro_ventas.csv', 'r', newline="") as archivo:
        lector = csv.reader(archivo)
        print("PRODUCTO     Cantidad vendida    Monto vendido")
        for fila in lector:
            print(f"{fila[0]}\t{fila[1]}\t{fila[4]}")

    time.sleep(2)



def forma_pago():
    with open('registro_ventas.csv', 'r', newline="") as archivo:
        lector = csv.reader(archivo)
        print("Forma de pago     Cantidad de ventas    Monto")
        
        print(f"Efectivo\t{efectivo}\t{total_efectivo}")
        print(f"Tarjeta de credito\t{credito}\t{total_credito}")
        print(f"Tarjeta de debito\t{debito}\t{total_debito}")

    time.sleep(2)
