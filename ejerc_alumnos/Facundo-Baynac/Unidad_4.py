# UNIDAD 4


def intervalo() -> None:
    """
    1. Crear una variable con valor 20 va a ser como referencia el minimo.
    Otra con valor de 500, va a ser como referencia el maximo.
    Luego pregunta al usuario por un valor, almacenarlo en otra variable, forzar a que ponga un numero, sino preguntar repetidamente.
    Ese numero transformarlo en integer
    
    Ahora imprimir en pantalla.
    - Si el numero que puso el usuario es menor que el valor minimo definido mostrar el texto VALOR BAJO
    - Si el numero que puso el usuario es mayor que el valor maximo definido mostrar el texto VALOR ALTO
    - Si el numero que puso el usuario esta entre el valor minimo y el valor maximo mostrar el texto VALOR MEDIO
    """
    valor_min = 20
    valor_max = 500

    numero = input("Ingrese un numero para continuar o una letra para salir: ")
    while numero.isdigit():
        numero = int(numero)
        if numero > valor_max:
            print("VALOR ALTO")
        elif numero < valor_min:
            print("VALOR BAJO")
        else:
            print("VALOR MEDIO")
        numero = input("Ingrese un numero para continuar o una letra para salir: ")


def es_anio_bisiesto() -> None:
    """
    2. Escriba un programa que pida un año y que escriba si es bisiesto o no.
    Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
    """
    anio = input("Ingrese un año: ")
    if anio.isdigit():
        anio = int(anio)
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    else:
        print("Debe ingresar un año válido")


def contador_bucles() -> None:
    """
    3.
    - Pedir al usuario que ingrese un número de inicio del bucle
    - Pedir al usuario que ingrese un número de fin del bucle
    Validar que el número de inicio sea menor al número de fin, si no es así volver a pedir los dos números, hasta que ésto sea correcto
    Luego de que el usuario ingrese los dos números, mostrar en pantalla todos los números que hay entre el número de inicio y el número de fin
    
    De la siguiente manera:
    
    Este es el bucle número 1
    Este es el bucle número 2
    Este es el bucle número 3
    ---
    Fin del programa.
    """
    num1 = input("Ingrese un número de inicio del bucle: ")
    num2 = input("Ingrese un número de fin del bucle: ")
    if num1.isdigit() and num2.isdigit() and int(num1) < int(num2):
        for contador in range(int(num1), int(num2)+1):
            print(f"Este es el bucle número {contador}")
    else:
        print("No ha ingresado un número o el número de fin de bucle es inferior al del inicio")


def promedio_examen() -> None:
    """
    4.Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
    Dentro del cuatrimestre son 4 examenes y luego un examen final.
    La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
    Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
    Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.
    
    Entonces el programa debe preguntar por la nota de cada examen.
    En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
    En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
    En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
    Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
    En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.
    """
    exam1 = input("Ingrese la nota del 1er examen: ")
    exam2 = input("Ingrese la nota del 2do examen: ")
    exam3 = input("Ingrese la nota del 3er examen: ")
    exam4 = input("Ingrese la nota del 4to examen: ")
    if exam1.isdigit() and exam2.isdigit() and exam3.isdigit() and exam4.isdigit():
        exam1 = float(exam1)
        exam2 = float(exam2)
        exam3 = float(exam3)
        exam4 = float(exam4)
        if exam1 > 0 and exam1 <= 10 and exam2 > 0 and exam2 <= 10 and exam2 > 0 and exam2 <= 10 and exam2 > 0 and exam2 <= 10:
            promedio:float = (exam1 + exam2 + exam3 + exam4) / 4
            print(f"El promedio de las notas es: {promedio}")
            if promedio >= 6:
                print("Tienes aprobada la cursada")
                final = input("Ingrese la nota del examen final: ")
                if final.isdigit() and float(final) >= 6:
                    print("Aprobaste la materia")
                else:
                    print("No aprobaste el final, debes rendir recuperatorio")
            else:
                print("No aprobaste la cursada")
        else:
            print("A ingresado una nota no válida (debe ser entre 1 y 10)")
    else:
        print("No ha ingresado un valor numérico")
    


def coeficientes_primer_grado() -> None:
    """
    5. Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
    Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a
    Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones):

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 0
    Escriba el valor del coeficiente b: 3
    La ecuación no tiene solución.

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 4.2
    Escriba el valor del coeficiente b: 21
    La ecuación tiene una solución: -5.0

    ECUACIÓN A X + B = 0
    Escriba el valor del coeficiente a: 0
    Escriba el valor del coeficiente b: 0
    Todos los números son solución.
    """


def coeficientes_segundo_grado() -> None:
    """
    6. Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.
    Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)
    Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).

    a	b	c	Solución
    1	-2	2	Sin solución real
    2	-7	3	Dos soluciones: 0.5 y 3.0
    1	2	1	Una solución: -1.0
    0	0	5	Sin solución
    0	0	0	Todos los números son solución
    0	3	2	Una solución: -0.666...
    """


def area_triangulo() -> None:
    """
    7. Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
    Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
    Nota: Utilice como valor de pi el valor 3.141592.
    """


def aproximacion() -> None:
    """9. Escriba un programa que pida tres números y diga si el tercero está más cerca del primero o del segundo."""


def main() -> None:
    print("\n\t#############################\n\t\tEjercicio 1:\n\t#############################\n\n")
    help(intervalo)
    intervalo()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 2:\n\t#############################\n\n")
    help(es_anio_bisiesto)
    es_anio_bisiesto()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 3:\n\t#############################\n\n")
    help(contador_bucles)
    contador_bucles()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 4:\n\t#############################\n\n")
    help(promedio_examen)
    promedio_examen()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 5:\n\t#############################\n\n")
    help(coeficientes_primer_grado)
    coeficientes_primer_grado()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 6:\n\t#############################\n\n")
    help(coeficientes_primer_grado)
    coeficientes_segundo_grado()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 7:\n\t#############################\n\n")
    help(area_triangulo)
    area_triangulo()
    input("Pulse una tecla para continuar")
    print("\n\t#############################\n\t\tEjercicio 9:\n\t#############################\n\n")
    help(aproximacion)
    aproximacion()
    input("Pulse una tecla para continuar")


if __name__ == "__main__":
    main()