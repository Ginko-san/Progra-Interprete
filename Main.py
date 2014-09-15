__author__ = 'Salchi Man'
# Name: Andres Garcia
# Work's Date: 26/ 08/ 2014
# Work's Hours: 6.15 pm 9 pm
import Logic


def menu():
    print("     SGL Simulator in Pyhton.\nMenu:")
    print(" 1. New File. \n 2. Compile.")
    opt = input("   Select: #")

    lista1 = []
    trad_list = []

    if opt == "1":
        file_name = input("File name: ")
        print("Type your code in SGL. Enter 'END' for finish")
        Logic.read_lines(lista1)
        trad_list = Logic.loop_lines(lista1, Logic.var_type)
        trad_list = Logic.loop_lines(trad_list, Logic.loop)
        trad_list = Logic.loop_lines(trad_list, Logic.function)
        trad_list = Logic.loop_lines(trad_list, Logic.conditional)
        Logic.new_file_py(file_name)
        Logic.save_data_file(trad_list, file_name)

    elif opt == "2":
        print("Put your file into ' generate_files ' folder and enter the name of the file to compile . ")
        file_name = input("File name: ")
        trad_list = Logic.open_compile(file_name)
        trad_list = Logic.loop_lines(trad_list, Logic.var_type)
        trad_list = Logic.loop_lines(trad_list, Logic.loop)
        trad_list = Logic.loop_lines(trad_list, Logic.function)
        trad_list = Logic.loop_lines(trad_list, Logic.conditional)
        Logic.new_file_py(file_name)
        Logic.save_data_file(trad_list, file_name)
menu()