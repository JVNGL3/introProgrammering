#!/usr/bin/python3 
import math

#5a
def derivate(f,x,h):
    return ((f(x+h) - f(x-h))/(2*h))

#5b
def solve(f, x0, h):
    # f för funktionen, x0 för sökningens startvärde, h för den önskade noggrannheten
    #x1 = x0 - (f(x0) / (derivate(f,x0,h)))
    x_n = x0
    if derivate(f,x_n,h) == 0:
        print("Error, division by 0")
        return
    x_n1 = x_n - (f(x_n)/derivate(f,x_n,h))

    while (abs(x_n1 - x_n) > h):
        if derivate(f,x_n,h) == 0:
            print("Error, division by 0")
            return
        x_n = x_n1
        x_n1 = x_n - (f(x_n)/derivate(f,x_n,h))
        #print("x_n:",x_n,"xn_1:",x_n1)
    #print(x_n1)
    return x_n1


# def f(x):
#    return (x- (math.e**(-1 * x)))

#print(solve(f, 1, 0.001))