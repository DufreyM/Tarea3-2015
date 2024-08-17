def funcion_dispersión(numero, num_celdas):
    """Calcula la posición en la memoria usando la función de dispersión."""
    if not isinstance(numero, int) or not isinstance(num_celdas, int):
        raise ValueError("Los parámetros deben ser enteros.")
    if num_celdas <= 0:
        raise ValueError("El número de celdas debe ser un entero positivo.")
    
    return numero % num_celdas

def almacenar_en_memoria(datos, num_celdas):
    """Almacena un array de datos en celdas de memoria indexadas."""
    if not isinstance(datos, list):
        raise ValueError("Los datos deben ser una lista.")
    if not all(isinstance(dato, int) for dato in datos):
        raise ValueError("Todos los elementos de la lista deben ser enteros.")
    if not isinstance(num_celdas, int) or num_celdas <= 0:
        raise ValueError("El número de celdas debe ser un entero positivo.")

    memoria = [None] * num_celdas  # Inicializa las celdas de memoria vacías

    for numero in datos:
        posicion = funcion_dispersión(numero, num_celdas)

        # Resolver colisión buscando la siguiente celda disponible
        intentos = 0
        while memoria[posicion] is not None:
            posicion = (posicion + 1) % num_celdas
            intentos += 1
            if intentos > num_celdas:
                raise RuntimeError("No se pudo almacenar el dato debido a una colisión que no se pudo resolver.")

        memoria[posicion] = numero

    return memoria

def recuperar_de_memoria(memoria, numero):
    """Busca un valor en las celdas de memoria."""
    if not isinstance(memoria, list):
        raise ValueError("La memoria debe ser una lista.")
    if not isinstance(numero, int):
        raise ValueError("El número a buscar debe ser un entero.")
    
    num_celdas = len(memoria)
    posicion = funcion_dispersión(numero, num_celdas)

    # Buscar el dato en la memoria
    intentos = 0
    while memoria[posicion] is not None:
        if memoria[posicion] == numero:
            return posicion
        posicion = (posicion + 1) % num_celdas
        intentos += 1
        if intentos > num_celdas or posicion == funcion_dispersión(numero, num_celdas):
            break

    return None  # No se encontró el valor

# Ejemplo de uso
datos = [15, 558, 32, 132, 102, 5, 257]
num_celdas = 11

memoria = almacenar_en_memoria(datos, num_celdas)
print("Celdas de memoria:", memoria)

# Buscar la posición de un valor
valor_a_buscar = 257
posicion = recuperar_de_memoria(memoria, valor_a_buscar)
if posicion is not None:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la memoria")
