from math import *
def sqrn(n):
    s = 0 
    for i in range(1,n+1):
        s = i**2 + s
    ss = sqrt(s)
    print("s = ", s)
    print("ss = ", ss)
n = int(input("please enter the number: "))
sqrn(n) 