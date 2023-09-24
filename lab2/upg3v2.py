#!/usr/bin/python3


def tvarsumman(n):
    
    if n == 0:
        #when the input is zero we have reaced the end of our recursion and the code on row 21 and onward is being executed
        return 0
    elif n%10 != 0:
        #if the input is not divisible by 10 it takes the rightmost digit and subtracts it from the input thus making it divisible by 10
        m = n - (n%10)  
        c = tvarsumman(m)
        c += n%10               
        return c        
    else:
        return tvarsumman(n/10)

print(tvarsumman(123))
    