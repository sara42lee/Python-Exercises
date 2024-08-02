avg = float(input("average score ="))
if avg >= 0 and avg < 10:
    print("Fail.")
elif avg >= 10 and avg < 15:
    print("Good.")
elif avg >= 15 and avg < 18:
    print("Very Good.")
elif avg >= 18 and avg <= 20:
    print("Excellent.")
else:
    print("Invalid grade.")