###function 
# 1.	Agregar un contacto: nombre, teléfono, email. X
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
import os
os.system("cls")
# Lista de contactos: cada contacto es una lista [nombre, telefono]
# def buscar_contacto(contacto):
contacto = ["jonas", 1234, "jonas@gmail.com" ]

def buscar_contacto(contacto):
    if len (contacto) == 0:
        print ("No hay contacto registrado")
    else:
        nombre_busqueda = input ("Ingrese el nombre a buscar")
    for i, nombre_busqueda in enumerate (contacto):
        if contacto[i].lower() == nombre_busqueda.lower():
            print (contacto)
            os.system("pause")
            return contacto
    return None

def eliminar(contacto):
    
    if len (contacto) == 0:
        print ("No hay contacto registrado")
    else:
        nombre_busqueda = input ("Ingrese el nombre a buscar para eliminar")
   