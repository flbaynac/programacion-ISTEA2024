# UNIDAD 3


def imprimir_nombre_edad() -> None:
    """1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga "¡Hola, `[nombre]`! Tienes `[edad]` años."""
    nombre:str = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    if edad.isdigit() and not nombre.isdigit():
        print(f"¡Hola, {nombre}! Tienes {edad} años.")
    else:
        print("No ha ingresado un nombre o edad válida")


def imprimir_figura() -> None:
    """
    2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings):

    +***************+
    *               *
    *               *
    *               *
    +***************+

    +---+
    |   |
    |   |
    |   |
    +---+

    ###################################
    ###################################
    ##                               ##
    ##                               ##
    ##                               ##
    ###################################
    ###################################
    """
    print(f"+***************+\n"
           "*               *\n"
           "*               *\n"
           "*               *\n"
           "+***************+\n"
           "\n"
           "+---+\n"
           "|   |\n"
           "|   |\n"
           "|   |\n"
           "+---+\n"
           "\n"
           "###################################\n"
           "###################################\n"
           "##                               ##\n"
           "##                               ##\n"
           "##                               ##\n"
           "###################################\n"
           "###################################\n")


def division_float() -> None:
    """3. Solicita al usuario que ingrese dos números enteros. Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado."""
    num1 = input("Ingrese un número entero: ")
    num2 = input("Ingrese otro número entero: ")
    if num2 != '0' and num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        resultado = num1 / num2
        print(f"El resultado de la división entre los dos números es: {resultado:.2f}")
    elif num2 == '0':
        print("No puede dividir por cero.")
    else:
        print("No ha ingresado un número válido")


def sumar_10() -> None:
    """4. Pide al usuario que ingrese una cadena que represente un número entero. Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado."""
    num = input("Ingrese un número entero: ")
    if num.isdigit():
        num = int(num)
        num += 10
        print(f"Sumando 10 da como resultado: {num}")
    else:
        print("No ha ingresado un número válido")


def mayor_menor_igual() -> None:
    """5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10, imprime "El número es mayor que 10". Si es igual a 10, imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10"."""
    num = input("Ingrese un número entero: ")
    if num.isdigit():
        num = int(num)
        if num > 10:
            print("\nEl número es mayor a 10")
        elif num == 10:
            print("\nEl número es igual a 10")
        else:
            print("\nEl número es menor que 10")
    else:
        print("No ha ingresado un número válido")


def mayor_o_menor_edad() -> None:
    """6a. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad"."""
    edad = input("Ingrese su edad: ")
    if edad.isdigit() and int(edad) >= 18:
        print("Eres mayor de edad")
    elif edad.isdigit():
        print("Eres menor de edad")
    else:
        print("No ha ingresado un número válido")


def hervor_agua() -> None:
    """6b. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario, imprime "El agua está en estado líquido"."""
    temperatura = input("Ingrese una temperatura en Celsius: ")
    if temperatura.isdigit() and float(temperatura) >= 100:
        print("El agua está hirviendo")
    elif temperatura.isdigit():
        print("El agua está en estado líquido")
    elif temperatura.lstrip("-").isdigit():
        print("El agua está congelada")
    else:
        print("No ha ingresado un número válido")


def numero_positivo_negativo_cero() -> None:
    """7. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo". Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero"."""
    num = input("Ingrese un número entero(positivo o negativo): ")
    if num == '0':
        print("El número es cero")
    elif num.isdigit(): 
        print("El número es positivo")
    elif num.lstrip("-").isdigit(): # Es un poco trampa pero es la forma que encontré de verificar si es un número y no un caracter sin un try catch, de paso ya sé si es negativo
        print("El número es negativo")
    else:
        print("No ha ingreaso un número válido")


def dia_de_la_semana() -> None:
    """8. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido"."""
    num = input("Ingrese un número entero del 1 al 7: ")
    if num.isdigit() and int(num) <= 7:
        num = int(num)
        if num == 1:
            print("\nEl día de la semana es Lunes")
        elif num == 2:
            print("\nEl día de la semana es Martes")
        elif num == 3:
            print("\nEl día de la semana es Miércoles")
        elif num == 4:
            print("\nEl día de la semana es Jueves")
        elif num == 5:
            print("\nEl día de la semana es Viernes")
        elif num == 6:
            print("\nEl día de la semana es Sábado")
        else:
            print("\nEl día de la semana es Domingo")
    else:
        print("No ha ingresado un número válido del 1 al 7")


def main() -> None:
    print("\n\t#############################\n\t\tEjercicio 1:\n\t#############################\n\n")
    print(imprimir_nombre_edad.__doc__)
    imprimir_nombre_edad()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 2:\n\t#############################\n\n")
    print(imprimir_figura.__doc__)
    imprimir_figura()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 3:\n\t#############################\n\n")
    print(division_float.__doc__)
    division_float()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 4:\n\t#############################\n\n")
    print(sumar_10.__doc__)
    sumar_10()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 5:\n\t#############################\n\n")
    print(mayor_menor_igual.__doc__)
    mayor_menor_igual()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 6a:\n\t#############################\n\n")
    print(mayor_o_menor_edad.__doc__)
    mayor_o_menor_edad()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 6b:\n\t#############################\n\n")
    print(hervor_agua.__doc__)
    hervor_agua()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 7:\n\t#############################\n\n")
    print(numero_positivo_negativo_cero.__doc__)
    numero_positivo_negativo_cero()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 8:\n\t#############################\n\n")
    print(dia_de_la_semana.__doc__)
    dia_de_la_semana()


if __name__ == "__main__":
    main()