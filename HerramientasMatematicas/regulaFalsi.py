from sympy import *
from mpmath import *
x = Symbol('x')
n = input("sum : ")
a = sympify(n)
mp.dps = 6
while(1):
    print("enter x value to substitue in equation")
    j = input()
    j = sympify(j)
    jm = a.evalf(subs={x:j})
    jm = N(jm,8)
    print(jm)
    print("1.exit. Any other number continue...")
    bn = int(input())
    if(bn==1):
        break
#k = input()
#k = sympify(k)
#l = a
#l.evalf(subs = {x:k})
print("Enter value of x1")
x1 = input()
x1 = sympify(x1)
print("Enter value of x2")
x2 = input()
x2 = sympify(x2)
x0 = 0
def formu():
    global a
    h = a
    global x1
    global x2
    k = h.evalf(subs={x:x1})
    l = h.evalf(subs={x:x2})
    m = k*(x2-x1)/(l-k)
    n = x1-m
    n = N(n,8)
    return n

while(1):
    x0 = formu()
    x0 = N(x0,8)
    print("x0 = "+str(x0))
    print("x1 = "+str(x1))
    print("x2 = "+str(x2))
    g = a.evalf(subs={x:x0})
    k = a.evalf(subs={x:x1})
    l = a.evalf(subs={x:x2})
    g = N(g,8)
    k = N(k,8)
    l = N(l,8)
    print("f(x0) = "+str(g))
    print("f(x1) = "+str(k))
    print("f(x2) = "+str(l))
    jk = g*k
    lk = g*l
    print("f(x0)*f(x1) = "+str(jk))
    print("f(x0)*f(x2) = "+str(lk))
    if(jk<0):
        x2 = x0
        print("x2 = x0")
    elif(lk<0):
        x1 = x0
        print("x1 = x0")
    print("2.exit. Any other number to continue...")
    bm = int(input())
    if(bm==2):
        break