from io import open
import os


def leer_libros():
    """

    lee los libros y crea listas segun las categorias, ademas de clasificar los datos individuales de los textos
    :return: Lista categorias

    """

    matematicas = []
    areas_practicas = []
    fisica = []
    ciencias_naturales = []

    libros = ["matematicas.txt", "areas_practicas.txt", "fisica.txt", "ciencias_naturales.txt"]
    categorias = [matematicas, areas_practicas, fisica, ciencias_naturales]

    for i in range(len(libros)):
        archivo = open(libros[i], "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            campos = linea.split(";")
            libro = {"autor": campos[0], "fecha": campos[1], "titulo": campos[2], "lugar": campos[3],
                     "editorial": campos[4], "cantidad": campos[5], "cita": campos[6]}
            categorias[i].append(libro)

    return categorias


def main():
    biblioteca = leer_libros()
    """
    for elemento in biblioteca:
        for l in elemento:
            #print(l["autor"], l["fecha"], l["titulo"], l["lugar"],l["editorial"], l["cantidad"])
            print(l["cantidad"])
            print()
    """
    for elemento in biblioteca:
        for l in elemento:
            if l["titulo"] == "Variable compleja y aplicaciones":
                print(l["cita"])

    """ 
    for l in biblioteca[1]:
        print(l["autor"], l["fecha"], l["titulo"], l["lugar"],l["editorial"], l["cantidad"])
        print()
    """


main()

----------------------------------------------------------------------------------------------------------

def disponibilidad(libros):
    #cantidad=libros[i]
    disponible=True
    if cantidad != 0:
        disponible = True
        print('El libro {} está listo para encontrar su nuevo dueño temporal :)'.format(libro[i]))
    else:
        print('Lo sentimos, el libro {} que solicitaste está agotado por el momento, pero seguro dentro de un par de días estará disponible. Esperamos verte pronto.'.format(libro[i]))
        disponible=False
    return disponible

def prestamo(libros):
    disponibilidad(libros)
    if disponible:
        cantidad-=1
    return cantidad

def citacion(libros):
    prestamos(libro)
    print(l["cita"])
    #print('{}, {}, {}, {}'.format(libros[0],libros[1],libros[2],libros[3]))

def main():
    citacion(libro)

main()
