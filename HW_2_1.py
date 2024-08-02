from math import *
a = int(input("a="))
b = int(input("b="))
c = int(input("C="))
delta = b**2 - (4*a*a) ;
if delta > 0:
    r1 = (-b+sqrt(delta))/(2*a) ;
    r2 = (-b-sqrt(delta))/(2*a) ;
    print("r1=",r1,"r2=",r2) ;
elif delta == 0:
    r = -b/(2*a) ;
    print ("r=",r)
else:
    print("no real roots.") ;

