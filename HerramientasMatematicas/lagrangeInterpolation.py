def lagrange_interpolation(x, y, xi):
    """
    Calcula el polinomio de interpolación de Lagrange para un conjunto de datos
    y devuelve el valor interpolado en xi.

    Parámetros:
    x  : lista, puntos x de los datos.
    y  : lista, valores y correspondientes a los puntos x.
    xi : valor en el que se desea interpolar.

    Devuelve:
    yint    : valor interpolado en xi.
    formula : cadena de texto con la fórmula del polinomio de interpolación.
    """
    n = len(x) - 1
    sum = 0.0
    terms = []
    for i in range(n + 1):
        product = y[i]
        term = f"{y[i]}"
        for j in range(n + 1):
            if i != j:
                product *= (xi - x[j]) / (x[i] - x[j])
                term += f" * (x - {x[j]}) / ({x[i]} - {x[j]})"
        sum += product
        terms.append(term)
    formula = " + ".join(terms)
    return sum, formula

# Ejemplo de uso
x = [2,4,5]
y = [4.2,5.1,5.8]
xi = 3
yint, formula = lagrange_interpolation(x, y, xi)
print(f"El valor interpolado en x = {xi} es y = {yint}")
print("")
print(f"La fórmula del polinomio de interpolación es: f(x) = {formula}")
