import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

def inicio():
    system("clear")
    print('-' * 50)
    print('-' * 5 +" Bienvenido al administrador de recetas " + '-' * 5)
    print('-' * 50 )
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción: ")
        print('''
        [1] - Leer receta
        [2] - Crear recete nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        ''')
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("categorias")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def elegir_recetas(lista):
    eleccion_recetas = 'x'
    while not eleccion_recetas.isnumeric() or int(eleccion_recetas) not in range(1,len(lista) + 1):
        eleccion_recetas = input("\n Elige una receta: ")
    return lista[int(eleccion_recetas) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe :(")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe :( ")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n Precione v para volver al menu: ")

finalizar_programa = False


while not finalizar_programa:
    # Mostrar el menu de inicio
    menu = inicio()
    if menu == 1:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar rectas
        mis_recetas = mostrar_recetas(mi_categoria)
        # elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        # leer recetas
        leer_receta(mi_receta)
        # volver al inicio
        volver_inicio()

    elif menu == 2:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categorias
        mi_categoria = elegir_categoria(mis_categorias)
        # crear receta nueva
        crear_receta(mi_categoria)
        # volver inicio
        volver_inicio()

    elif menu == 3:
        # crear categoria
        crear_categoria(mi_ruta)
        # volver inicio
        volver_inicio()
    elif menu == 4:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar rectas
        mis_recetas = mostrar_recetas(mi_categoria)
        # elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        # eliminar recetas
        eliminar_receta(mi_receta)
        # volver al inicio
        volver_inicio()

    elif menu == 5:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar categoria
        eliminar_categoria(mi_categoria)
        # volver inicio
        volver_inicio()

    elif menu == 6:
        # finalizar el programa
        finalizar_programa = True
