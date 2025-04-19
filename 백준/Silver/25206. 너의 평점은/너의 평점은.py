rating = 0
rating_sum = 0.0
for i in range(20):
    name, credit, grade = input().split()
    credit = float(credit)
    if grade == 'P':
        continue
    elif grade == 'A+':
        rating += credit
        rating_sum += (credit * 4.5)
    elif grade == 'A0':
        rating += credit
        rating_sum += (credit * 4.0)
    elif grade == 'B+':
        rating += credit
        rating_sum += (credit * 3.5)
    elif grade == 'B0':
        rating += credit
        rating_sum += (credit * 3.0)
    elif grade == 'C+':
        rating += credit
        rating_sum += (credit * 2.5)
    elif grade == 'C0':
        rating += credit
        rating_sum += (credit * 2.0)
    elif grade == 'D+':
        rating += credit
        rating_sum += (credit * 1.5)
    elif grade == 'D0':
        rating += credit
        rating_sum += (credit * 1.0)
    elif grade == 'F':
        rating += credit
        rating_sum += (credit * 0.0)
print(f"{rating_sum / rating:.6f}")