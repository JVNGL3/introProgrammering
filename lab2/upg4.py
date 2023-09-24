#!/usr/bin/python3


def tvarsumman2(n):
    count = 0
    while True:
        if n == 0:
            return count
        else:
            count += (n%10)
            n -= (n%10)
            n /= 10
    
#tvarsumman2(int(input("input:")))