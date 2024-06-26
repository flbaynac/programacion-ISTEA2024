# UNIDAD 9


def dic_add() -> None:
    """
    1. Crear un diccionario vacío y agregar elementos:
    Agrega tres entradas al diccionario con nombres de personas como llaves y sus números de teléfono como valores.
    Imprime el diccionario.
    Acceder a elementos del diccionario:
    """


def dic_print() -> None:
    """
    2. Usa el diccionario contactos del ejercicio anterior.
    Imprime el número de teléfono de una persona específica.
    Verifica si una persona no está en el diccionario e imprime un mensaje.
    Eliminar elementos del diccionario:
    """


def dic_del() -> None:
    """
    3. Usa el diccionario contactos.
    Elimina una entrada del diccionario.
    Imprime el diccionario después de la eliminación.
    """


def dic_recorrer() -> None:
    """
    4. Recorrer un diccionario:
    Usa el diccionario contactos.
    Recorre todas las llaves del diccionario y las imprime.
    Recorre todos los valores del diccionario y los imprime.
    Recorre todos los pares llave-valor y los imprime.
    """


def dic_copy() -> None:
    """
    5. Copiar un diccionario:
    Crea una copia del diccionario contactos.
    Modifica la copia y demuestra que el diccionario original no ha cambiado.
    """


def dic_longitud() -> None:
    """
    6. Longitud del diccionario:
    Imprime la cantidad de entradas en el diccionario contactos.
    Actualizar valores del diccionario:
    """


def dic_update() -> None:
    """
    7.Actualiza el número de teléfono de una persona en el diccionario contactos.
    Imprime el diccionario actualizado.
    """


def dic_a_partir_de_dos_listas() -> None:
    """
    8.Crear un diccionario a partir de dos listas:
    Tienes dos listas, una de nombres y otra de números de teléfono.
    Crea un diccionario que asocie cada nombre con su número de teléfono.
    """


def uso_de_get() -> None:
    """
    9.Uso de get para acceso seguro:
    Usa el método get para obtener el número de teléfono de una persona que no está en el diccionario sin generar un error.
    Imprime un mensaje predeterminado si la persona no está en el diccionario.
    """

def combinar_dic() -> None:
    """
    10. Combinar dos diccionarios:
    Crea una lista de frutas y otra lista de precios correspondientes. Luego, escribe un programa que combine ambas listas en un diccionario donde las frutas son las claves y los precios son los valores. Imprime el diccionario resultante.
    """


def contar_ocurrencias_caracteres() -> None:
    """
    1. Contar ocurrencias de caracteres en una cadena:
    Escribe una función que tome una cadena como argumento y devuelva un diccionario con el conteo de cada carácter en la cadena.
    """


def invertir_diccionario() -> None:
    """
    2.Invertir un diccionario:
    Escribe una función que tome un diccionario como argumento y devuelva un nuevo diccionario donde las claves sean los valores y los valores sean las claves.
    """


def agrupar_elementos_por_clave() -> None:
    """
    3. Agrupar elementos por clave:
    Dado un diccionario donde las claves son categorías y los valores son listas de elementos, escribe una función que invierta esta estructura, es decir, agrupe elementos por su categoría.
    """


def filtrar_dic() -> None:
    """
    4.Filtrar un diccionario:
    Escribe una función que tome un diccionario y un valor de umbral como argumentos y devuelva un nuevo diccionario con solo las entradas cuyos valores sean mayores que el umbral.
    """


def mezclar_dos_dic() -> None:
    """
    5. Mezclar dos diccionarios:
    Escribe una función que tome dos diccionarios y devuelva un nuevo diccionario combinando ambos. Si hay claves duplicadas, suma sus valores.
    """


def dic_con_valor_otro_dic() -> None:
    """6.Crea un diccionario donde cada valor es otro diccionario. Escribe funciones para agregar, actualizar y eliminar entradas en los diccionarios anidados."""


def ordenar_dic_por_val() -> None:
    """
    7.Ordenar un diccionario por valores:
    Escribe una función que tome un diccionario y lo devuelva ordenado por sus valores.
    """


def dic_frecuencia_palabra() -> None:
    """8. Escribe una función que tome una cadena de texto y devuelva un diccionario con la frecuencia de cada palabra."""


def conteo_ocurrencias_en_lista() -> None:
    """9. Escribe una función que tome una lista de elementos y devuelva un diccionario con cada elemento de la lista y su conteo de ocurrencias en la lista."""


def main() -> None:
    print("\n--- NIVEL SIMPLE ---\n\n\t#############################\n\t\tEjercicio 1:\n\t#############################\n\n")
    print(dic_add.__doc__)
    dic_add()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 2:\n\t#############################\n\n")
    print(dic_print.__doc__)
    dic_print()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 3:\n\t#############################\n\n")
    print(dic_del.__doc__)
    dic_del()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 4:\n\t#############################\n\n")
    print(dic_recorrer.__doc__)
    dic_recorrer()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 5:\n\t#############################\n\n")
    print(dic_copy.__doc__)
    dic_copy()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 6:\n\t#############################\n\n")
    print(dic_longitud.__doc__)
    dic_longitud()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 7:\n\t#############################\n\n")
    print(dic_update.__doc__)
    dic_update()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 8:\n\t#############################\n\n")
    print(dic_a_partir_de_dos_listas.__doc__)
    dic_a_partir_de_dos_listas()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 9:\n\t#############################\n\n")
    print(uso_de_get.__doc__)
    uso_de_get()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 10:\n\t#############################\n\n")
    print(combinar_dic.__doc__)
    combinar_dic()
    input("Pulse una tecla para continuar")
    
    print("\n--- NIVEL MEDIO ---\n\n\t#############################\n\t\tEjercicio 1:\n\t#############################\n\n")
    print(contar_ocurrencias_caracteres.__doc__)
    contar_ocurrencias_caracteres()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 2:\n\t#############################\n\n")
    print(invertir_diccionario.__doc__)
    invertir_diccionario()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 3:\n\t#############################\n\n")
    print(agrupar_elementos_por_clave.__doc__)
    agrupar_elementos_por_clave()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 4:\n\t#############################\n\n")
    print(filtrar_dic.__doc__)
    filtrar_dic()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 5:\n\t#############################\n\n")
    print(mezclar_dos_dic.__doc__)
    mezclar_dos_dic()
    input("Pulse una tecla para continuar")
    
    print("\n--- DICCIONARIO DE DICCIONARIOS ---\n\n\t#############################\n\t\tEjercicio 6:\n\t#############################\n\n")
    print(dic_con_valor_otro_dic.__doc__)
    dic_con_valor_otro_dic()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 7:\n\t#############################\n\n")
    print(ordenar_dic_por_val.__doc__)
    ordenar_dic_por_val()
    input("Pulse una tecla para continuar")
    
    print("\n--- CONVERTIR LISTAS ANIDADAS A DICCIONARIO ---\n\n\t#############################\n\t\tEjercicio 8:\n\t#############################\n\n")
    print(dic_frecuencia_palabra.__doc__)
    dic_frecuencia_palabra()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 9:\n\t#############################\n\n")
    print(conteo_ocurrencias_en_lista.__doc__)
    conteo_ocurrencias_en_lista()


if __name__ == "__main__":
    main()