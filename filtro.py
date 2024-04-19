import sys

def filtrar_productos(precios, umbral, operacion="mayor"):
    """
    Filtra los productos según el umbral y la operación especificados.

    Args:
        precios (dict): Diccionario con los nombres de los productos como claves y sus precios como valores.
        umbral (int): Umbral para filtrar los precios.
        operacion (str): Especifica si se deben mostrar los productos mayores ("mayor") o menores ("menor") que el umbral.

    Returns:
        list: Lista de nombres de productos que cumplen la condición especificada.
    """
    productos_filtrados = []

    # Verificar la operación a realizar
    if operacion == "mayor":
        for producto, precio in precios.items():
            if precio > umbral:
                productos_filtrados.append(producto)
    elif operacion == "menor":
        for producto, precio in precios.items():
            if precio < umbral:
                productos_filtrados.append(producto)
    else:
        return "Lo sentimos, no es una operación válida"

    return productos_filtrados

if __name__ == "__main__":
    # Precios de los productos de ejemplo
    precios = {'Notebook': 700000,
               'Teclado': 25000,
               'Mouse': 12000,
               'Monitor': 250000,
               'Escritorio': 135000,
               'Tarjeta de Video': 1500000}

    # Verificar los argumentos proporcionados en la línea de comandos
    if len(sys.argv) == 2:
        # Si se proporciona un argumento, se toma como umbral y se muestran los productos mayores al umbral
        umbral = int(sys.argv[1])
        productos = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ", ".join(productos))
    elif len(sys.argv) == 3:
        # Si se proporcionan dos argumentos, el primero es el umbral y el segundo especifica si se muestran productos mayores o menores al umbral
        umbral = int(sys.argv[1])
        operacion = sys.argv[2].lower()
        productos = filtrar_productos(precios, umbral, operacion)
        if isinstance(productos, str):
            print(productos)  # Si la operación especificada no es válida, se imprime un mensaje de error
        else:
            if operacion == "mayor":
                print("Los productos mayores al umbral son:", ", ".join(productos))
            elif operacion == "menor":
                print("Los productos menores al umbral son:", ", ".join(productos))
    else:
        print("Número de argumentos incorrecto.")

# Por ejemplo: "python filtro.py 30000 "mostrará los productos cuyos precios son mayores que 30000, mientras que "python filtro.py 30000 menor" mostrará los productos cuyos precios son menores que 30000.

