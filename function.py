import os
os.system("cls")

# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.


contacto = []

def agregar_contacto():
    
    nombre = input("Ingrese su nombre:\n")
    
    telefono = 0
    while telefono==0:
        try:
            telefono = int(input("ingrese su numero telefonico:\n"))
           
        except:
            print("debe ingresar numeros")
            
    while not "@" in email:
        email = input("ingrese su email:\n")
        
            
            
        contacto.append(nombre)
        contacto.append(telefono)
        contacto.append(email)

def mostrar_contactos(contacto):
    for i in contacto:
        print(i)