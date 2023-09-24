#!/usr/bin/python3

def kostnad(P,r,a):
    k = P + (a+1)*P*r/2
    return k

print("Den total kostnaden blir:", kostnad(50000, 0.03, 10), "kr")