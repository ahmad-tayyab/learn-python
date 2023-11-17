from typing import Union

per: Union[int, float] = 7
# per: int |float = 7  alternative of above code
grade: Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per < 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear Student your percentage is {
      per} now your calculated grade is:\t {grade}")


# grade: str = None   # we can't assign str type to a None type


per1: Union[int, float] = int(input("Enter your percentage:\t"))
grade1: Union[str, None] = None

if (per1 >= 0) and (per1 < 33):
    grade1 = "Fail"
elif (per1 >= 33) and (per1 < 50):
    grade1 = "E"
elif (per1 >= 50) and (per1 < 60):
    grade1 = "c"
elif (per1 >= 60) and (per1 < 70):
    grade1 = "B"
elif (per1 >= 70) and (per1 < 80):
    grade1 = "A"
elif (per1 < 80) and (per1 <= 100):
    grade1 = "A+"
else:
    grade1 = "Fail"

print(f"Dear Student your percentage is {
      per1} now your calculated grade is:\t {grade1}")
