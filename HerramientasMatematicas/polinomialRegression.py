def polinomial_regression(x, y, degree):
    n = len(x)
    m = degree
    
    # Verificar si la regresión es posible
    if n < m + 1:
        print("Error: No hay suficientes puntos de datos para realizar la regresión polinomial.")
        return None
    
    # Inicializar la matriz aumentada A
    A = [[0.0] * (m + 2) for _ in range(m + 1)]
    
    # Calcular los elementos de la matriz aumentada
    for i in range(m + 1):
        for j in range(m + 1):
            A[i][j] = sum(x[k]**(i + j) for k in range(n))
    
    # Calcular el vector de términos independientes
    for i in range(m + 1):
        A[i][m + 1] = sum(y[k] * x[k]**i for k in range(n))
    
    # Resolución del sistema de ecuaciones mediante eliminación gaussiana
    for i in range(m + 1):
        # Hacer el pivote A[i][i] igual a 1
        pivot = A[i][i]
        for j in range(m + 2):
            A[i][j] /= pivot
        
        # Hacer los elementos de la columna i iguales a 0 (excepto en la fila i)
        for k in range(m + 1):
            if k != i:
                factor = A[k][i]
                for j in range(m + 2):
                    A[k][j] -= factor * A[i][j]
    
    # Los coeficientes están en la última columna de la matriz aumentada
    coefficients = [A[i][m + 1] for i in range(m + 1)]
    
    return coefficients

def print_polynomial(coefficients):
    terms = []
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            if i == 0:
                terms.append(f"{coeff:.4f}")
            elif i == 1:
                terms.append(f"{coeff:.4f} * x")
            else:
                terms.append(f"{coeff:.4f} * x^{i}")
    polynomial = " + ".join(terms)
    print("La función polinómica es:")
    print("f(x) =", polynomial)

# Datos de ejemplo
x = [1, 2, 3, 4, 5, 6, 7]
y = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]  # Ejemplo para un polinomio de grado 2

# Grado del polinomio
degree = 2

# Calcular los coeficientes del polinomio
coefficients = polinomial_regression(x, y, degree)

if coefficients is not None:
    print("Coeficientes del polinomio:", coefficients)
    print_polynomial(coefficients)
