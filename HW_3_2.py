def multi_2n7 (n):
    r1 = n%2
    r2 = n%7
    if r1 == 0 and r2 == 0: 
       print ("yes.")
    else:
        print("no.")


n = int(input("please enter the number: "))
multi_2n7(n)
