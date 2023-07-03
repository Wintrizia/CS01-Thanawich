a = float(input("คะแนนเก็บ: "))
b = float(input("คะแนนสอบกลางภาค: "))
c = float(input("คะแนนสอบปลายภาค: "))

score = int(a+b+c)
grade = int

if score > 100:
    grade = "dum"
elif score >= 80:
    grade = "A"
elif score >= 75:
    grade = "B+"
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = "C+"
elif score >= 60:
    grade = "C"
elif score >= 55:
    grade = "D+"
elif score >= 50:
    grade = "D"
elif score < 50:
    grade = "F"

print("เกรดของคุณคือ: ", grade)