def calcular_promedio(velocidades):
    """
    Calcula el promedio de una lista de velocidades.

    Args:
        velocidades (list): Lista de velocidades de las correas transportadoras.

    Returns:
        float: Promedio de las velocidades.
    """
    # Suma de todas las velocidades en la lista
    total_velocidades = sum(velocidades)
    # Calcula el promedio dividiendo la suma total de velocidades entre el número total de elementos
    promedio = total_velocidades / len(velocidades)
    return promedio

def listar_correas_sobre_promedio(velocidades):
    """
    Lista las posiciones de las correas transportadoras que están por encima del promedio.

    Args:
        velocidades (list): Lista de velocidades de las correas transportadoras.

    Returns:
        list: Lista de posiciones de las correas transportadoras que están por encima del promedio.
    """
    # Calcula el promedio de las velocidades utilizando la función calcular_promedio
    promedio = calcular_promedio(velocidades)
    # Crea una lista de posiciones de las correas que tienen velocidades por encima del promedio
    correas_sobre_promedio = [i for i, velocidad in enumerate(velocidades) if velocidad > promedio]
    return correas_sobre_promedio

if __name__ == "__main__":
    # Lista de velocidades de las correas transportadoras
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
                 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
                 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
                 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
                 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
                 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    
    # Obtiene las posiciones de las correas cuyas velocidades están por encima del promedio
    correas_sobre_promedio = listar_correas_sobre_promedio(velocidad)
    print(correas_sobre_promedio)
