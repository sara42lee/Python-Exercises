s = int(input("Please enter the number of seconds:"))
r_s = s%60
h = int(s/3600)
m = int((s-r_s-(3600*h))/60)
print("hours:",h,"minutes:",m,"seconds:",r_s)