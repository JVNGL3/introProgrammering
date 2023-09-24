#!/usr/bin/python3

class counter():
    # This class is used purely for having a counter within the recrusive function
    def __init__(self):
        counter.count = 0

    def incrementBy(self,x):
        counter.count += x


def tvarsumman(n):
    c = counter()
    if n == 0:
        #when the input is zero we have reaced the end of our recursion and the code on row 21 and onward is being executed
        return 0
    elif n%10 != 0:
        #if the input is not divisible by 10 it takes the rightmost digit and subtracts it from the input thus making it divisible by 10
        m = n - (n%10)  
        tvarsumman(m)
        c.incrementBy(n%10)               # this increments the counter with the rightmost nonzero digit in the number
        return c.count        
    else:
        tvarsumman(n/10)
        return

# print(tvarsumman(0))
    