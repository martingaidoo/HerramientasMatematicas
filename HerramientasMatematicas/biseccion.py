#Dealbera, Juan Pablo
#Para que este codigo funcione debes ingresarle una funcion aqui debajo
#Ademas agregar los valores del intervalo, y el error permitido

#Funcion que recibe un valor y lo evalua en la funcion dada
#Funcion ejercicio 1: -0.874*(x**2)+1.75*x+2.627
#Funcion ejercicio 2: -2.1+6.21*x-3.9*(x**2)+0.667*(x**3)
def funcion (x):
    return (-2.1+6.21*x-3.9*(x**2)+0.667*(x**3))

#Funcion que recibe un intervalo y evalua si existe una raiz en el
def VerificarRaizExiste (a,b):
    return (funcion(a)>0 and funcion(b)<0) or (funcion(b)>0 and funcion(a)<0)

#Funcion que recibe 3 valores y verifica que lado debo elegir, verificando si existe una raiz en ese intervalo
def VerificarLado (Xa,Xr,Xb):#Xa, Xr, Xc
    if (VerificarRaizExiste(Xa,Xr)):
        return ([Xa,Xr])
    else:
        return ([Xr,Xb])

#Metodo de biseccion, recibe el intervalo y el error permitido
def Biseccion (a,b,e):
    resultado = []#Matriz que contendra las iteraciones con estos valores
    # Iteracion | Xa | Xr | Xb | f(Xa) | f(Xr) | f(Xb) | err
    iteraciones = 0 #Las iteraciones comienzan en 0
    while True:#Se ejecuta un while hasta que el error conseguido de Xr sea menor o igual al permitido
        if (iteraciones == 0):#Verifico si es la primera iteracion
            Xa = a#Si lo es asigno a Xa y Xb los valores del intervalo pasado
            Xb = b
        else:#Si no, verifico para que lado del intervalo me designo y asigno dichos extremos como los valores de Xa y Xb
            Xa,Xb = VerificarLado(resultado[iteraciones-1][1],resultado[iteraciones-1][2],resultado[iteraciones-1][3])
            #Xa = aux[0]#Una vez que verifico el lado asigno los valores
            #Xb = aux[1]
        Xr = (Xa+Xb)/2#Calculo el nuevo Xr
        fXa = funcion(Xa)#Calculo la funcion en cada valor
        fXb = funcion(Xb)
        fXr = funcion(Xr)
        if (iteraciones > 0):#Verifico si no es la primera iteracion
            err = abs(((Xr - resultado[iteraciones-1][2])/Xr)*100)#En ese caso calculo el error
        else:#Si no, asigno el valor 100
            err = 100
        resultado.append([iteraciones+1,round(Xa,5),round(Xr,5),round(Xb,5),round(fXa,5),round(fXr,5),round(fXb,5),round(err,5)])#Agrego a la matriz todos los resultados obtenidos

        if (err > e):#Verifico el error para saber si entra dentro de los valores permitidos, si no lo cumple itero una vez mas
            iteraciones += 1
        else:#Si no, termino el ciclo
            break
    return (resultado)#Retorno la matriz

#Intervalo
a = 0.3
b = 0.6
#Error permitido
e = 1
print ("Iteracion | Xa | Xr | Xb | f(Xa) | f(Xr) | f(Xb) | err")
for i in Biseccion (a,b,e):
    print (i)

#-----------------------------------------------
#Parte de interfaz grafica generada con gpt
import tkinter as tk
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            label = tk.Label(root, text=matriz[i][j], padx=20, pady=10)
            label.grid(row=i, column=j)
# Crear una ventana
root = tk.Tk()
root.title("Matriz")
# Llamar a la función para mostrar la matriz en la ventana
m = ["Iteracion","Xa","Xr","Xb","f(Xa)","f(Xr)" ,"f(Xb)","err"]#Agrego las etiqueras de la columna
mat = Biseccion (a,b,e)
mat.insert (0,m)
mostrar_matriz(mat)
# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()