import math
x1 = float(input("please enter the x-coordinate of the first point:"))
y1 = float(input("please enter the y-coordinate of the first point:"))
x2 = float(input("please enter the x-coordinate of the second point:"))
y2 = float(input("please enter the y-coordinate of the second point:"))
d = math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
print("Euclidean Distance:",d)