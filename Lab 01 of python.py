#LAB1

#1
"""
print("Hello JKLU!")
print("I am learning Python.")
"""
#2
"""
name=input("Enter your name: ")
branch=input("Enter your branch: ")
print("Welcome", name)
print("Your branch is", branch)
"""
#3
"""
length = float(input("Enter length in metres: "))
width = float(input("Enter width in metres: "))

area = length * width

print("Area =", area, "square metres")
"""
#4
"""
length = float(input("Enter length in feet: "))
width = float(input("Enter width in feet: "))

area = length * width
area = area * 0.092903

print("Area =", area, "square metres")
"""

#5
"""
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x <= 0 or y <= 0:
    print("Invalid Input")
elif y % x == 0:
    print("y is divisible by x")
else:
    print("y is not divisible by x")
"""
#6
"""
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
#7
"""
radius = float(input("Enter radius: "))

if radius < 1 or radius > 100:
    print("Invalid Input")
else:
    area = 3.14 * radius * radius
    print("Area =", area)
"""
#8
"""
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit =", fahrenheit)
print("Kelvin =", kelvin)
"""
#9
"""
seconds = int(input("Enter seconds: "))

if seconds < 1 or seconds > 86400:
    print("Invalid Input")
else:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print(hours, ":", minutes, ":", seconds)
"""
#10
"""
total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

attendance = (attended_classes / total_classes) * 100

print("Attendance =", attendance, "%")

if attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")
"""

#LAB2

#1
"""
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Hi")
else:
    print("Bye")
"""

#2
"""
x = float(input("Enter first parallel side: "))
y = float(input("Enter second parallel side: "))
h = float(input("Enter height: "))

area = ((x + y) * h) / 2

print("Area of trapezoid =", area)
"""
#3
"""
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Slightly overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")
"""
#4
"""
letter = input("Enter an alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")
"""
#5
"""
initial = 2.19e14
final = 4.68e14

growth = ((final - initial) / initial) * 100

print("Percentage of bacterial growth =", round(growth))
"""
#6
"""
months = int(input("Enter number of months: "))

years = months // 12
remaining_months = months % 12

print("Years =", years)
print("Months =", remaining_months)
"""
#7
"""
color = input("Enter color: ")
mode = input("Enter mode: ")

if color == "Blue":
    if mode == "Steady":
        print("Clear view")
    else:
        print("Clouds due")
else:
    if mode == "Steady":
        print("Rain ahead")
    else:
        print("Snow instead")
"""
#8
"""
cost = float(input("Enter cost: "))
revenue = float(input("Enter revenue: "))

if cost == revenue:
    print("Break even")
elif revenue > cost:
    print("Profit")
else:
    print("Loss")
"""
#9
"""
widgets = int(input("Enter number of widgets: "))

if widgets < 100:
    cost = widgets * 0.25
else:
    cost = widgets * 0.20

print("Total cost =", cost)
"""
#10
"""
pounds = float(input("Enter number of pounds: "))
cash = float(input("Enter cash: "))

cost = pounds * 2.50

if cash >= cost:
    change = cash - cost
    print("Change =", change)
else:
    owe = cost - cash
    print("You owe $", owe, "more.")
"""
#11
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest =", a)
    else:
        print("Largest =", c)
else:
    if b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)
"""
#12
"""
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 20 / 100
ta = basic_salary * 5 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + ta + da

print("HRA =", hra)
print("TA =", ta)
print("DA =", da)
print("Gross Salary =", gross_salary)
"""
#13
"""
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 20 / 100
ta = basic_salary * 5 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + ta + da
if gross_salary < 300000:
    print("Income Tax = 0%")
elif gross_salary <= 1000000:
    print("Income Tax = 10%")
elif gross_salary <= 2500000:
    print("Income Tax = 20%")
else:
    print("Income Tax = 30%")
"""
#14
"""
income = float(input("Enter taxable income: "))

if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("Tax =", tax)
"""

#LAB3

#1
"""
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
r = float(input("Enter radius: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
radius = r * r

if distance < radius:
    print("Point is inside the circle")
elif distance == radius:
    print("Point is on the boundary of the circle")
else:
    print("Point is outside the circle")
"""
#2
"""
s = float(input("Enter the side of the pentagon: "))
area = (5 * s * s) / (4 * 0.726)
print("Area of pentagon =", area)
"""
#3
"""
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b + c != 180:
    print("Invalid triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right-angled triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse-angled triangle")
else:
    print("Acute-angled triangle")
"""
#4
"""
number = int(input("Enter a 4 digit number: "))

first = number // 1000
second = (number // 100) % 10
third = (number // 10) % 10
fourth = number % 10

first_sum = first + second
last_sum = third + fourth

print("Sum of first two digits =", first_sum)
print("Sum of last two digits =", last_sum)

if first_sum == last_sum:
    print("The two sums are equal")
else:
    print("The two sums are not equal")
"""
#5
"""
number = int(input("Enter a 5 digit number: "))

d1 = number // 10000
d2 = (number // 1000) % 10
d3 = (number // 100) % 10
d4 = (number // 10) % 10
d5 = number % 10

largest = d1
position = 1

if d2 > largest:
    largest = d2
    position = 2

if d3 > largest:
    largest = d3
    position = 3

if d4 > largest:
    largest = d4
    position = 4

if d5 > largest:
    largest = d5
    position = 5

print("Largest digit =", largest)
print("Position =", position)
"""
#6
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

a = a + b + c
b = a - b - c
c = a - b - c
a = a - b - c

print("a =", a)
print("b =", b)
print("c =", c)
"""
#7
"""
number = int(input("Enter a 3 digit number: "))

if number < 100 or number > 999:
    print("Invalid input")
else:
    first = number // 100
    second = (number // 10) % 10
    third = number % 10

    sum_digits = first + second + third

    if number % sum_digits == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")
"""
#8
"""
water = float(input("Enter initial quantity of water: "))
days = int(input("Enter number of days: "))

if water < 0 or days < 0:
    print("Invalid input")
else:
    water = water * (0.95 ** days)
    added_water = 10 * (1 - (0.95 ** days)) / 0.05
    water = water + added_water

    print("Amount of water after", days, "days =", water)
"""
#9
"""
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if a1 == 0 and b1 == 0:
    print("Invalid first line")
elif a2 == 0 and b2 == 0:
    print("Invalid second line")
elif D != 0:
    x = Dx / D
    y = Dy / D

    print("x =", x)
    print("y =", y)

elif Dx == 0 and Dy == 0:
    print("The lines are coincident")
else:
    print("The lines are parallel")
"""




