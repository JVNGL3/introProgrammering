#!/usr/bin/python3

def bounce2(n):
    ref = n
    while ref > 0:
        print(ref)
        ref -= 1

    for _ in range(n+1):
        print(_)
    
    
#bounce2(int(input("siffra:")))
