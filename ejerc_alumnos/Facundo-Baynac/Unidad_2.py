# UNIDAD 2


import math  # Para ejercicio 4


def area_rectangulo() -> None:
    """Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado."""
    altura_rectangulo = 3
    base_rectangulo = 5
    area = altura_rectangulo * base_rectangulo
    print(f"El área de un rectángulo con base 5 y altura 3 es: {area}")


def convierte_temperatura() -> None:
    """Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y
    luego imprime la temperatura equivalente en Fahrenheit."""
    print("Ingrese la temperatura en Celsius:")
    temperatura_celsius = input()
    if temperatura_celsius.isdigit():
        temperatura_celsius = int(temperatura_celsius)
        temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
        print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit}")
    else:
        print("Ha ingresado un caracter inválido")


def concat_string() -> None:
    """Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato
    de esa variable."""
    nombre = "Facundo"
    edad = "23"
    nombre_y_edad = nombre + edad
    print(f"El tipo de dato de la variable nombre_y_edad es: {type(nombre_y_edad)}")


def calcular_area_circulo() -> None:
    """Calcula el área de un círculo con radio 4. Imprime el resultado."""
    radio_circulo = 4
    area_circulo = math.pi * radio_circulo ** 2
    print(f"El área de un círculo con radio 4 es: {area_circulo}")


def calculadora() -> None:
    """Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números."""
    numero1 = input("Ingrese un número:")
    numero2 = input("Ingrese otro número:")
    if numero1.isdigit() and numero2.isdigit():
        numero1 = int(numero1)
        numero2 = int(numero2)
        suma:int = numero1 + numero2
        print(f"suma: {suma}")
        resta:int = numero1 - numero2
        print(f"resta: {resta}")
        multiplicacion:int = numero1 * numero2
        print(f"multiplicación: {multiplicacion}")
        if numero2 != 0:
            division:float = numero1 / numero2
            print(f"División: {division:.2f}")
        else:
            print("No se puede dividir por 0.")
    else:
        print("Ha ingresado un caracter inválido")


def operacion_compleja() -> None:
    """Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado
    como el tipo de dato de esa variable."""
    resultado_operacion = 2 * 4 / 3 + 4
    print(f"El resultado de la operación (2 * 4 / 3 + 4) es: {resultado_operacion}"
          f",y de tipo: {type(resultado_operacion)}")


def aprobo_desaprobo() -> None:
    """Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado."""
    aprobado: bool = False
    print(f"Estado de la variable booleana aprobado: {aprobado}")


def calcular_perimetro_triangulo() -> None:
    """Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado."""
    longitud_lado = 6
    perimetro_triangulo = 3 * longitud_lado
    print(f"El perímetro del triángulo equilátero es: {perimetro_triangulo}")


def imprime_tipo_de_dato() -> None:
    """Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato."""
    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")
    ciudad = input("Ingrese ciudad de residencia: ")
    print(f"Tipo de dato nombre: {type(nombre)} \nTipo de dato edad: {type(edad)} \nTipo de dato ciudad: {type(ciudad)}")


def operacion_matematica() -> None:
    """Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato."""
    resultado = (14 * 34) / 12 * (2 - 3 + 6)
    print(f"El resultado es: {resultado} y su tipo de dato es: {type(resultado)}")


def main() -> None:
    print("\n\t#############################\n\t\tEjercicio 1:\n\t#############################\n\n")
    print(area_rectangulo.__doc__)
    area_rectangulo()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 2:\n\t#############################\n\n")
    print(convierte_temperatura.__doc__)
    convierte_temperatura()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 3:\n\t#############################\n\n")
    print(concat_string.__doc__)
    concat_string()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 4:\n\t#############################\n\n")
    print(calcular_area_circulo.__doc__)
    calcular_area_circulo()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 5:\n\t#############################\n\n")
    print(calculadora.__doc__)
    calculadora()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 6:\n\t#############################\n\n")
    print(operacion_compleja.__doc__)
    operacion_compleja()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 7:\n\t#############################\n\n")
    print(aprobo_desaprobo.__doc__)
    aprobo_desaprobo()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 8:\n\t#############################\n\n")
    print(calcular_perimetro_triangulo.__doc__)
    calcular_perimetro_triangulo()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 9:\n\t#############################\n\n")
    print(imprime_tipo_de_dato.__doc__)
    imprime_tipo_de_dato()
    input("Pulse una tecla para continuar")
    
    print("\n\t#############################\n\t\tEjercicio 10:\n\t#############################\n\n")
    print(operacion_matematica.__doc__)
    operacion_matematica()


if __name__ == "__main__":
    main()