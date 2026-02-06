grades = [85, 78, 92, 55, 88]

for grade in grades:
    if grade < 60:
        print("Failing grade found:", grade)
        break
    print("Passed grade:", grade)