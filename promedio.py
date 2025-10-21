# 1. Define la lista de números
numeros = [10, 20, 35, 40, 50]

# 2. Calcula la suma de los números usando la función 'sum()'
suma_total = sum(numeros)

# 3. Calcula la cantidad de números usando la función 'len()'
cantidad_de_elementos = len(numeros)

# 4. Calcula el promedio
if cantidad_de_elementos > 0:
    promedio = suma_total / cantidad_de_elementos
    print(f"La suma es: {suma_total}")
    print(f"La cantidad de elementos es: {cantidad_de_elementos}")
    print(f"El promedio es: {promedio}")
else:
    print("La lista está vacía, no se puede calcular el promedio.")