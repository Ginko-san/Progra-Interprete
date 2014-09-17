__author__ = 'Salchi Man'
# Name: Andres Garcia
# Work's Date: 26/ 08/ 2014  | 16 y 17  /08/2014
# Work's Hours: 6.15 pm 9 pm |  11.00 pm - 6:00 am
import Logic  # Importa el modulo Logic del proyecto.

'''
Menu del Sistema Interprete, se encarga de mostrar las opciones a elegir, si se elige cualquier diferente,
dicho le mostrara otra vez las opciones y le pedira que la ingrese de nuevo. Ademas dependiendo de la opcion realizada
realiza lectura de lineas de codigo si ingresa un nuevo archivo, encambio si ingresa "Compile", realiza lectura de
lineas en un archivo de texto.
'''


def menu():
    print("     SGL Simulator in Pyhton.\nMenu:")
    print(" 1. New File. \n 2. Compile. \n 3. Exit")
    opt = input("   Select: # ")

    while opt != "3":

        lista1 = []
        trad_list = []

        if opt == "1":
            file_name = input("File name: ")  # Lectura del nombre por asignar al archivo
            print("Type your code in SGL. Enter 'END' for finish")
            Logic.read_lines(lista1)  # Lextura de Lineas
            trad_list = Logic.loop_lines(lista1, Logic.var_type)  # comparacion con matrizes
            trad_list = Logic.loop_lines(trad_list, Logic.loop)
            trad_list = Logic.loop_lines(trad_list, Logic.function)
            trad_list = Logic.loop_lines(trad_list, Logic.conditional)
            Logic.new_file_py(file_name)  # Creacion de ARCHIVO
            Logic.save_data_file(trad_list, file_name)  # Ingreso de lineas de codigo en python al archivo

            # en prueba "Error de codigo"
            #if not Logic.compare_lists(trad_list, lista1):
            #    print("\n Error code online, incorrect or missing command syntax or operands!")

            opt = input("Finish...\nRequires to perform another operation? y/n:")  # Verifica si necesita realizar mas operaciones.
            if opt == "n":
                opt = "3"
            elif opt == "N":
                opt = "3"
            else:
                opt = "4"

        elif opt == "2":
            print("Put your file into ' generate_files ' folder and enter the name of the file to compile . ")
            try:
                file_name = input("File name: ")
                trad_list = Logic.open_compile(file_name)  # Lectura del nombre por asignar al archivo
                trad_list = Logic.loop_lines(trad_list, Logic.var_type)  # comparacion con matrizes
                trad_list = Logic.loop_lines(trad_list, Logic.loop)
                trad_list = Logic.loop_lines(trad_list, Logic.function)
                trad_list = Logic.loop_lines(trad_list, Logic.conditional)
                Logic.new_file_py(file_name)  # Creacion de ARCHIVO
                Logic.save_data_file(trad_list, file_name)  # Ingreso de lineas de codigo en python al archivo
                print("Successfully compiled file")
            except:
                print("\n", FileNotFoundError, "Check File's Name")
            opt = input("Finish...\nRequires to perform another operation? y/n:")  # Verifica si necesita realizar mas operaciones.
            if opt == "n":
                opt = "3"
            elif opt == "N":
                opt = "3"
            else:
                opt = "4"

        elif opt == "4":  # si la opcion fue 4 significa que desean seguir trabajando
            print("\n\n")
            print("     SGL Simulator in Pyhton.\nMenu:")
            print(" 1. New File. \n 2. Compile. \n 3. Exit")
            opt = input("   Select: # ")


        else:  # si digitan un digito fuera de las opciones lanza de nuevo el menu.
            print("Invalid option. Choose again.\n\n")
            print("     SGL Simulator in Pyhton.\nMenu:")
            print(" 1. New File. \n 2. Compile. \n 3. Exit")
            opt = input("   Select: # ")

menu()