"""
Este módulo define una clase para calcular el Máximo Común Divisor (MCD)
entre dos números utilizando el algoritmo de Euclides.
"""


class MaximoComunDivisor:
    """Clase para calcular el Máximo Común Divisor de dos números."""

    def __init__(self, a, b):
        """
        Inicializa la clase con dos números.

        Args:
            a (int): Primer número.
            b (int): Segundo número.
        """
        self._a = a
        self._b = b

    @property
    def a(self):
        """Getter para el primer número."""
        return self._a

    @a.setter
    def a(self, value):
        """Setter para el primer número."""
        self._a = value

    @property
    def b(self):
        """Getter para el segundo número."""
        return self._b

    @b.setter
    def b(self, value):
        """Setter para el segundo número."""
        self._b = value

    def calcular_mcd(self):
        """
        Calcula el Máximo Común Divisor utilizando el algoritmo de Euclides.

        Returns:
            int: El MCD de los dos números.
        """
        a = abs(self._a)
        b = abs(self._b)
        while b != 0:
            a, b = b, a % b
        return a


def main():
    """
    Función principal que solicita dos números enteros, crea una instancia de la clase
    MaximoComunDivisor, y muestra el MCD calculado. Además, ejemplifica el uso de getters y setters.
    """
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        return

    mcd_obj = MaximoComunDivisor(a, b)
    print(f"El MCD de {mcd_obj.a} y {mcd_obj.b} es: {mcd_obj.calcular_mcd()}")

    # Ejemplo de uso de getters y setters
    try:
        nuevo_a = int(input("Ingrese un nuevo valor para el primer número: "))
        nuevo_b = int(input("Ingrese un nuevo valor para el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        return

    mcd_obj.a = nuevo_a
    mcd_obj.b = nuevo_b
    print(f"El MCD de {mcd_obj.a} y {mcd_obj.b} es: {mcd_obj.calcular_mcd()}")


if __name__ == "__main__":
    main()
