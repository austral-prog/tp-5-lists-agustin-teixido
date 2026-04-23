# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor mínimo de la lista o None si está vacía
    """
    pass  # Reemplazar con tu implementación

    if len(lista) > 0 :
        max_val = lista[0]

        for num in lista:
            if num < max_val:
                max_val = num

        return max_val
    elif len(lista) == 0 :
        return None
    else :
        return None