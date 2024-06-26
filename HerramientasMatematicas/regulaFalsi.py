import tkinter as tk

# Definición de la función matemática
def funcion(x):
    return (-1 - 3 * x + (x**3))

# Función para verificar si hay una raíz en el intervalo [a, b]
def VerificarRaizExiste(a, b):
    return (funcion(a) > 0 and funcion(b) < 0) or (funcion(b) > 0 and funcion(a) < 0)

# Función para determinar el lado del intervalo donde buscar la raíz
def VerificarLado(Xa, Xr, Xb):
    if VerificarRaizExiste(Xa, Xr):
        return (Xa, Xr)
    else:
        return (Xr, Xb)

def ModFalsePos(xl, xu, es, imax):
    iter = 0
    fl = funcion(xl)
    fu = funcion(xu)
    ea = es + 1  # Inicializa ea con un valor mayor que es para garantizar que entre en el bucle
    il = 0
    iu = 0
    resultado = []
    
    xr = 0  # Inicialización de xr fuera del bucle
    
    while ea > es and iter < imax:
        if iter == 0:
            Xa = xl
            Xb = xu
        else:
            Xa, Xb = VerificarLado(resultado[iter - 1][1], resultado[iter - 1][2], resultado[iter - 1][3])
        
        xrold = xr
        xr = Xb - fu * (Xa - Xb) / (fl - fu)
        fr = funcion(xr)
        iter += 1
        
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        
        test = fl * fr
        
        if test < 0:
            xu = xr
            fu = funcion(xu)
            iu = 0
            il += 1
            if il >= 2:
                fl = fl / 2
        elif test > 0:
            xl = xr
            fl = funcion(xl)
            il = 0
            iu += 1
            if iu >= 2:
                fu = fu / 2
        else:
            ea = 0
        
        resultado.append([iter, round(Xa, 5), round(xr, 5), round(Xb, 5), round(fl, 5), round(fr, 5), round(fu, 5), round(ea, 5)])
    
    return resultado


# Función para mostrar la matriz en una ventana Tkinter
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            label = tk.Label(root, text=matriz[i][j], padx=10, pady=5, borderwidth=1, relief="solid")
            label.grid(row=i, column=j, sticky="nsew")

# Definición de intervalo y error permitido
xl = -1
xu = 1
es = 0.5
imax = 10

# Creación de la ventana Tkinter
root = tk.Tk()
root.title("Método de Falsa Posición Modificada")

# Ejecución del método de falsa posición modificada
resultado_falsa_posicion = ModFalsePos(xl, xu, es, imax)

# Etiquetas de las columnas
etiquetas = ["Iteración", "Xa", "Xr", "Xb", "f(Xa)", "f(Xr)", "f(Xb)", "Error (%)"]

# Insertar etiquetas como primera fila en la matriz de resultados
resultado_falsa_posicion.insert(0, etiquetas)

# Mostrar la matriz en la ventana Tkinter
mostrar_matriz(resultado_falsa_posicion)

# Ajustar el tamaño de las columnas para que se expandan automáticamente
for j in range(len(etiquetas)):
    root.grid_columnconfigure(j, weight=1)

# Iniciar el bucle principal de Tkinter
root.mainloop()
