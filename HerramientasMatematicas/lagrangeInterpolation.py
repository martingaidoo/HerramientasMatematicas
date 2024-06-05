def lagrange_interpolation(x, y, xi):
    """
    Calcula el polinomio de interpolación de Lagrange para un conjunto de datos
    y devuelve el valor interpolado en xi.

    Parámetros:
    x  : lista, puntos x de los datos.
    y  : lista, valores y correspondientes a los puntos x.
    xi : valor en el que se desea interpolar.

    Devuelve:
    yint : valor interpolado en xi.
    """
    n = len(x) - 1
    sum = 0.0
    for i in range(n + 1):
        product = y[i]
        for j in range(n + 1):
            if i != j:
                product *= (xi - x[j]) / (x[i] - x[j])
        sum += product
    return sum

# Ejemplo de uso
x = [0, 4, 6, 5, 3, 1.5, 2.5, 3.5]
y = [1, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630]
xi = 2
yint = lagrange_interpolation(x, y, xi)
print(f"El valor interpolado en x = {xi} es y = {yint}")