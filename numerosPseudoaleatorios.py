# Leonardo Dufrey Mejía Mejía 
# Carnet: 23648
# Fecha de creación: 2024-08-16
# Fecha de actualización: 2024-08-16
# Versión: 1.1
# Descripción: Programa que genera una serie de números pseudoaleatorios
# Función que utiliza el método de congruencia y los agrega al array. 

def metodo_congruencia(m, a, c, s, cantidad):
    x = s
    random = []
    
    # La secuencia de los números
    for _ in range(cantidad):
        # Fórmula en la tarea
        x = (a * x + c) % m
        # Agregar al array
        random.append(x)
    
    return random

def main():
    # Solicitar valores al usuario con validaciones
    while True:
        try:
            m = int(input("Ingrese el valor de m (módulo, m > 0): "))
            if m <= 0:
                raise ValueError("El módulo debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")
    
    while True:
        try:
            a = int(input("Ingrese el valor de a (multiplicador, a > 0): "))
            if a <= 0:
                raise ValueError("El multiplicador debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")
    
    while True:
        try:
            c = int(input("Ingrese el valor de c (incremento, c >= 0): "))
            if c < 0:
                raise ValueError("El incremento debe ser un número no negativo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")
    
    while True:
        try:
            s = int(input("Ingrese el valor de s (semilla, s >= 0): "))
            if s < 0:
                raise ValueError("La semilla debe ser un número no negativo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")
    
    while True:
        try:
            cantidad = int(input("Ingrese el número de valores a generar (cantidad > 0): "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente nuevamente.")

    # Generar los números pseudoaleatorios
    random = metodo_congruencia(m, a, c, s, cantidad)
    
    # Mostrar los resultados
    print("Números pseudoaleatorios generados:", random)

if __name__ == "__main__":
    main()
