import os
lista=[]
def existe(cod):
    for i,z in lista:
        if i==cod:
            return (True,z)
    return (False,'')


def alta():
    cod='1'
    while cod!='0':
        cod=input("Introduce cod:")
        if cod=='0':
            continue
        articulo=input("Introduce articulo:")
        lista.append([cod,articulo])
    return

def baja():
    cod='1'
    while cod!='0':
        cod=input("Introduce cod:")
        if cod=='0':
            continue
        ex,ar=existe(cod)
        indice=[cod,ar]
        if ex:
            lista.remove(indice)
        else:
            print("no existe")
    return





def modificacion():
    cod='1'
    while cod!='0':
        cod=input("Introduce cod:")
        if cod=='0':
            continue
        ex,ar=existe(cod)
        indice=[cod,ar]
        if ex:
            des=input("Introduce artículo:")
            indice = [cod, ar]
            nuevovalor=[cod, des]
            lista.remove(indice)
            lista.append(nuevovalor)
        else:
            print("no existe")
    return




def listar():
    for i in lista:
        print(i)
    return


def principal():
    cod='1'
    while cod!='0':
        print("1. Alta")
        print("2. Baja")
        print("3. Modificación")
        print("4. Listar")
        print("0. Salir")
        cod=input("introduce opción:")
        if cod=='1':
            alta()
        if cod=='2':
            baja()
        if cod=='3':
            modificacion()
        if cod=='4':
            listar()
    return




principal()



