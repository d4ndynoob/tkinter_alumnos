# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist
# "r+" - Reads and write

# from distutils.command.clean import clean
# usadas para clean y sleep
from os import system, name
from time import sleep  

RUTA = "C:/Users/danie/Escritorio/UPP/2do Cuatrimestre/Estructuras de Datos/1er Parcial/Python/RegistroAlumnosBlocDeNotas/alumnos.txt"

# Funcion para limpiar consola
def clear():
    if name == 'nt':
        _ = system('cls')

# Funcion para validar numero
def validarNumero(mensaje):
    valido = False
    while(valido == False):
        numero = input(mensaje)
        if(numero.isnumeric() == True):
            valido = True
    return numero
    
entra = True
while(entra == True):
    clear()
    # pregunta
    print("* * * * * * * * * * * M E N Ú * * * * * * * * * * *\n")
    print("[1] - Agregar alumno")
    print("[2] - Mostrar alumnos")
    print("[3] - Salir")
    print("[4] - Filtrar")
    resp = input("Escribe el número de una opción: ")
    
    # Agregar
    if(resp == '1'):
        repetir_agregar = True
        while(repetir_agregar):
            clear()
            datos = [validarNumero("MATRICULA: "), input("NOMBRE: "), validarNumero("EDAD: "), input("SEXO [masculino/femenino]: "), input("CIUDAD: "), validarNumero("C.P: "), "\n"]
            
            with open(RUTA, 'a') as file:
                datos_formateados = " ".join(datos)
                file.write(datos_formateados)
            clear()
            print("Alumno agregado con éxito")
            
            #pregunta
            rep_agregar_resp = input("\n\n¿Quieres agregar otro alumno? [ si / no ]: ")
            if(rep_agregar_resp == 'SI' or rep_agregar_resp == "si" or rep_agregar_resp == "Si" or rep_agregar_resp == "sI"):
                repetir_agregar = True
            else:
                repetir_agregar = False
        
    # Mostrar
    elif(resp == '2'):
        clear()
        # juego con la consola
        print("Buscando...")
        sleep(2)
        clear()
        with open(RUTA, 'r') as file:
            for linea in file:
                print(linea, end='')
        
    # Salir
    elif(resp == '3'):
        clear()
        print('Adios')
        entra = False
        
    # Filtrar
    elif(resp == '4'):
        repetir_filtrar = True
        while(repetir_filtrar):
            clear()
            palabra = input("Buscar: ")
            
            lista_alumnos = []
            resultados = []
            existe = False
            
            with open(RUTA, 'r') as file:
                for line in file:
                    lista_reglon = line.split()    #crea una lista de las palabras en la linea
                    lista_alumnos.append(lista_reglon)
            
            for i in range(0, len(lista_alumnos)):
                if(lista_alumnos[i][0] == palabra or lista_alumnos[i][1] == palabra or lista_alumnos[i][2] == palabra or lista_alumnos[i][3] == palabra or lista_alumnos[i][4] == palabra or lista_alumnos[i][5] == palabra):
                    existe = True
                    resultados_formateados = " ".join(lista_alumnos[i])
                    resultados.append(resultados_formateados)
                    
            # juego con la consola
            clear()
            print("Buscando...")
            sleep(2)
            clear()
            
            if(existe == True):
                for x in range(0, len(resultados)):
                    print(resultados[x])
            else:
                print("No se encontraron resultados")
            #pregunta
            rep_filtrar_resp = input("\n\n¿Quieres filtrar por otra palabra? [ si / no ]: ")
            if(rep_filtrar_resp == 'SI' or rep_filtrar_resp == "si" or rep_filtrar_resp == "Si" or rep_filtrar_resp == "sI"):
                repetir_filtrar = True
            else:
                repetir_filtrar = False
    else:
        print("Opción no válida.")
    
    if(resp != '3'):
        x = input("\n\n¿Quieres realizar otra operación? [ si / no ]: ")
        if(x == "Si" or x == "sI" or x == "SI" or x == "si"):
            entra = True
        else: 
            entra = False