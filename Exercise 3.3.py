score = input("Enter Score: ")
s = float(score)
if s >= 0.0 and s <= 1.0:
    if s >= 0.9:
        grade = "A"
    elif s >= 0.8:
        grade = "B"
    elif s >= 0.7:
        grade = "C"
    elif s >= 0.6:
        grade = "D"
    else:
        grade = "F"
else:
    grade = "error"
print(grade)
