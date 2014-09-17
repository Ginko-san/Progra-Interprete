__author__ = 'Salchi Man'

# Name: Andres Garcia
# Work's Date: 26/ 08/ 2014  | 16 y 17  /08/2014
# Work's Hours: 6.24 pm - 9.pm |  11.00 pm - 6:00 am

var_type = [["ent", "int"], ["flot", "float"], ["cad", "str"], ["char", "chr"], ["boolen", "bool"]]
conditional = [["@", "   "], ["{", ":"], [";", ""], ["^^", ","], ["}", "\n"], ["sino", "elif"], ["si", "if"], ["hacer", "else"], ["END", ""]]
loop = [["mientras", "while"], ["para", "for"], ["en", "in"]]
function = [["desde", "from"], ["importe", "import"], ["funcion", "def"], ["devuelve", "return"], ["escribir", "print"]]

# Codigo encargado de leer las lineas de entrada del Usuario en SGL.
def read_lines(cod_list):
    while True:
        line = input()
        if line == "END":
            return cod_list
        cod_list.append(line)


# funcion que toma la matriz con codigo en SGL y la matriz con sintaxis por parametro, para comparar.
def loop_lines(cod_list, list_x):
    trad_list = []
    for x in cod_list:
        t = translate_line(x, list_x)
        if t == False:
            trad_list.append(x)
        else:
            trad_list.append(t)
    return trad_list

# Funcion encargada de tomar la linea a traducir y ir comparando en orden con secciones de las matrices.
def translate_line(SGL_line, list_x):
    trad_line = SGL_line
    for y in list_x:
        d, amount = search(SGL_line, y[0])
        if d:
            trad_line = trad_line.replace(y[0], y[1], amount)
    if trad_line != SGL_line:
        return trad_line
    return False

# Funcion encargada de comparar cadenas de codigo contra secciones de las matrices que se asignan por parametro.
def search(cad, dat):
    listax = cad.split(" ")
    for x in listax:
        y, amount = find_bool(x, dat)
        if x == dat:
            return True, 1
        elif y:
            return True, amount
    return False, 0

# Funcion que busca valores como el @ que se encuentran pegados aveces a palabras.
def find_bool(var, dat):
    x = var.find(dat)
    pos = []
    while x >= 0:
        pos.append(x)
        var = var.replace(dat, "", 1)
        x = var.find(dat)
    if len(pos) > 0:
        return True, len(pos)
    return False, 0

# funcion encargada de crear un archivo con el nombre por parametro.
def new_file_py(name):
    file = open('generate_files/' + name + '.py', 'w')
    file.close()

# Funcion encargada de ingresar los datos traducidos al archivo creado con la funcion anterior.
def save_data_file(trad_list, name):
    file = open('generate_files/' + name + '.py', 'a')

    for x in trad_list:
        file.write(x + "\n")

    file.close()

# Funcion encargada de tomar el nombre por parametro de un archivo txt y buscarlo en la carpeta "Compile_files"
def open_compile(name):
    file = open('compile_files/' + name + '.txt', 'r')
    lines = file.readlines()
    return lines

# codigo para prueba de error de sintaxis.
def compare_lists(lista, listb):
    x = 0
    while x < len(lista) - 1:
        if lista[x] == listb[x]:
            return False
        x += 1
    return True

