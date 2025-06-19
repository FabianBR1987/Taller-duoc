# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
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
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

import os
from function import *
os.system("cls")

option = None
contacto = []

while option != 5:
    print("\t\t----Menu Mini agenda de contactos----")
    print("1) Agregar contacto")
    print("2) Listar contacto")
    print("3) Buscar contacto")
    print("4) Eliminar contacto")
    print("5) Salir")
    try:
        option = int(input("Seleccione opcion: \n"))
        if option < 1 or option > 5:
            print("ERROR: Opcion elegida debe ser entre 1 y 5\n")
        else:
            if option == 1:
                os.system("cls")
                agregar_contacto()
                os.system("pause")
            elif option == 2:
                os.system("cls")
                mostrar_contacto(contacto)
                os.system("pause")
            elif option == 3:
                os.system("cls")
                print(option)
                os.system("pause")
            elif option == 4:
                os.system("cls")
                print(option)
                os.system("pause")
            elif option == 5:
                os.system("cls")
                print("saliendo del sistema")
                os.system("pause")                    
             
    except:
        print("La opcion debe ser numero entero\n")    
print("Haz salido del sistema")
    