def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n: El número entero no negativo del que se desea calcular el factorial.

    Returns:
        El factorial de n.
    """
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: calcular factorial de n multiplicando n por el factorial de n-1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    """
    Calcula la productoria de una lista de números.

    Args:
        lista: La lista de números de la que se desea calcular la productoria.

    Returns:
        La productoria de la lista.
    """
    # Caso base: si la lista está vacía, la productoria es 1
    if not lista:
        return 1
    # Caso recursivo: multiplicar el primer elemento de la lista por la productoria del resto de la lista
    else:
        return lista[0] * productoria(lista[1:])

def calcular(fact_1=None, prod_1=None, fact_2=None):
    """
    Realiza los cálculos de factorial y productoria según los argumentos proporcionados.

    Args:
        fact_1: El número entero no negativo del que se desea calcular el factorial (opcional).
        prod_1: La lista de números de la que se desea calcular la productoria (opcional).
        fact_2: El número entero no negativo del que se desea calcular el factorial (opcional).

    Returns:
        Ningún valor, solo imprime los resultados en pantalla.
    """
    # Calcular y mostrar el factorial de fact_1 si está presente
    if fact_1 is not None:
        resultado = factorial(fact_1)
        print(f"El factorial de {fact_1} es {resultado}")
    
    # Calcular y mostrar la productoria de prod_1 si está presente
    if prod_1 is not None:
        resultado = productoria(prod_1)
        print(f"La productoria de {prod_1} es {resultado}")
    
    # Calcular y mostrar el factorial de fact_2 si está presente
    if fact_2 is not None:
        resultado = factorial(fact_2)
        print(f"El factorial de {fact_2} es {resultado}")

# Ejemplo de uso
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
