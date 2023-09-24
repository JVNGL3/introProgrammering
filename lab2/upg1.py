#!/usr/bin/python3

def bounce(n):
    print(n)
    if (n) == 0:
        return  
    else:
        n -= 1
        bounce(n)
    print(n+1)
    
#bounce(int(input("siffra:")))
