import termcolor2
import math

print(termcolor2.colored("1_First Degree Equation", color="blue"))
print(termcolor2.colored("2_Second Degree Equation", color="blue"))
print(termcolor2.colored("3_Third Degree Equation", color="blue"))


def equation():
    user = input("Enter Your Selection: ")
    if user == "1":
        # a * x + b = 0
        # 2 * x + 8 = 0 => -4
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        x = -b / a
        return x

    if user == "2":
        # a * x**2 + b * x + c = 0
        # 4 * x**2 + 2 * x + 6 = 0
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        c = int(input("Enter Third Number: "))
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return x1, x2
        elif delta == 0:
            x = -b / a
            return x
        else:
            return termcolor2.colored("No Answer", color="red")

    if user == "3":
        # x**3 + a * x**2 + b * x + c = 0
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        c = int(input("Enter Third Number: "))

        p = (b - (a ** 2 / 3))
        q = (2 * (a ** 3 / 27)) - ((a * b) / 3 + c)
        delat = ((q ** 2) / 4) + ((p ** 3) / 27)
        if delat > 0:
            x = (-q / 2 + math.sqrt(delat)) ** 1 / 3 + (-q / 2 - math.sqrt(delat)) ** 1 / 3 / (a / 3)
            return x
        elif delat == 0:
            x1 = -2 * (q / 2) ** 1 / 3 - (a / 3)
            x2 = (q / 2) ** 1 / 3 - (a / 3)
            return x1, x2
        else:
            return termcolor2.colored("No Answer", color="red")
print(equation())
