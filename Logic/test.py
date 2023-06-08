def encontrar_elementos_optimos(elementos, calorias_minimas, peso_maximo):
    mejor_conjunto = None
    mejor_peso_total = float('inf')
    mejor_calorias_total = 0

    # Generar todas las combinaciones posibles de elementos
    for i in range(1, 2**len(elementos)):
        conjunto_actual = []
        peso_total = 0
        calorias_total = 0

        # Verificar cada elemento en la combinación actual
        for j in range(len(elementos)):
            if (i >> j) & 1:
                elemento = elementos[j]
                conjunto_actual.append(elemento)
                peso_total += elemento['peso']
                calorias_total += elemento['calorias']

        # Verificar si el conjunto actual cumple con los requisitos
        if calorias_total >= calorias_minimas and peso_total <= peso_maximo:
            # Verificar si el conjunto actual es mejor que el anterior mejor conjunto
            if peso_total < mejor_peso_total or (peso_total == mejor_peso_total and calorias_total > mejor_calorias_total):
                mejor_conjunto = conjunto_actual
                mejor_peso_total = peso_total
                mejor_calorias_total = calorias_total

    return mejor_conjunto

# Ejemplo de uso
elementos = [
    {'nombre': 'E1', 'peso': 5, 'calorias': 3},
    {'nombre': 'E2', 'peso': 3, 'calorias': 5},
    {'nombre': 'E3', 'peso': 5, 'calorias': 2},
    {'nombre': 'E4', 'peso': 1, 'calorias': 8},
    {'nombre': 'E5', 'peso': 2, 'calorias': 3}
]

calorias_minimas = 16
peso_maximo = 9

conjunto_optimo = encontrar_elementos_optimos(elementos, calorias_minimas, peso_maximo)

if conjunto_optimo:
    print("Elementos viables:")
    for elemento in conjunto_optimo:
        print(f"{elemento['nombre']} Peso {elemento['peso']} Calorías: {elemento['calorias']}")
else:
    print("No se encontró ningún conjunto de elementos viables.")