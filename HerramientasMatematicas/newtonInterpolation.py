def newton_interpolation(x, y, xi):
    """
    Calcula el polinomio de interpolación de Newton para un conjunto de datos,
    y devuelve el valor interpolado en xi, la fórmula del polinomio y los coeficientes.

    Parámetros:
    x  : lista, puntos x de los datos.
    y  : lista, valores y correspondientes a los puntos x.
    xi : valor en el que se desea interpolar.

    Devuelve:
    yint       : valor interpolado en xi.
    formula    : cadena de texto con la fórmula del polinomio de interpolación.
    coeficientes : lista de coeficientes del polinomio de interpolación.
    """
    n = len(x) - 1
    # Inicialización de la tabla de diferencias divididas
    fdd = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        fdd[i][0] = y[i]

    # Construcción de la tabla de diferencias divididas
    for j in range(1, n+1):
        for i in range(n+1-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])

    # Obtención de los coeficientes
    coeficientes = [fdd[0][j] for j in range(n+1)]

    # Cálculo de la interpolación en xi y construcción de la fórmula del polinomio
    yint = fdd[0][0]
    xterm = 1.0
    formula = f"{fdd[0][0]}"
    for order in range(1, n+1):
        xterm *= (xi - x[order-1])
        yint += fdd[0][order] * xterm

        # Construcción de la fórmula
        term_formula = f"{fdd[0][order]}"
        for k in range(order):
            term_formula += f" * (x - {x[k]})"
        formula += f" + {term_formula}"

    return yint, formula, coeficientes

# Ejemplo de uso
x = [300,375,425,475]
y = [8.7,10,11.3,12.7]
xi = 400

yint, formula, coeficientes = newton_interpolation(x, y, xi)
print(f"El valor interpolado en x = {xi} es y = {yint}")
print("")
print(f"La fórmula del polinomio de interpolación es: f(x) = {formula}")
print("")
print(f"Los coeficientes b del polinomio de interpolación son: {coeficientes}")