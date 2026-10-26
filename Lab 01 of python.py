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

 

