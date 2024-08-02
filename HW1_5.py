w = int(input("number of wheels:"))
b = int(input("number of bodies:"))
d = int(input("number of dummies:"))
c = min(w//4,b,d//2)
r_w = w-(c*4)
r_b = b-c
r_d = d-(c*2)
print("wheels:",r_w,"bodies:",r_b,"dummies:",r_d)