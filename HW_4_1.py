from math import *
def d(x1,x2,y1,y2):
    dis = sqrt((x2-x1)**2+(y2-y1)**2)
    print(dis)

x1 = int(input("please enter x1: "))
x2 = int(input("please enter x2: "))
y1 = int(input("please enter y1: "))
y2 = int(input("please enter y2: "))
d(x1,x2,y1,y2)