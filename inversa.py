"""
Este módulo calcula la inversa de un número ingresado por el usuario.
Si el número es cero o no es válido, se maneja la excepción correspondiente.
"""


class Exceptionnumerocero(Exception):
    """Excepción personalizada para indicar que el número ingresado es cero."""


try:
    x = float(input("Numero: "))
    if x == 0:
        raise Exceptionnumerocero
    inversa = 1 / x
    print(f"numero= {x} su inversa es {inversa}")

except ValueError:
    print("Ingrese un numero para calcular la inversa")

except ZeroDivisionError:
    print("Ingrese un numero diferente de CERO para obtener un valor diferente a infinito")

except Exceptionnumerocero:
    print("Ingrese un numero diferente de CERO para obtener un valor diferente a infinito")

else:
    print("Se presento un error")

finally:
    print("Fin de la aplicacion")
