import math
# def printMessage():
#     print("Welcome to ICD2O!")

# def subtract(num1, num2):
#     answer = num1 - num2
#     return answer

# printMessage()
# result = subtract(5,6)
# print(subtract(4,2))

# print(result)

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# print(subtract(x,y))

def greet(name):
    return f"Hello, {name}"

print(greet("James"))

def cube(num):
    return num**3

print(cube(5))

def area_rectangle(length,width):
    return length*width

print(area_rectangle(5,2))

def format_pi(decimals):
    return f"{math.pi:.{decimals}f}"

print("Pi is", format_pi(3))

def seconds(hours):
    return hours*60

print(seconds(5))

def total_with_tax(price,tax_rate):
    return f"Total: ${price*tax_rate + price}"

print(total_with_tax(5,0.13))

def bmi(weight,height):
    return f"BMI = {weight/height**2:.2f}"

print(bmi(140,6))

def greeting_with_age(name,age):
    return f"Hi {name}, you are {age} years old"

print(greeting_with_age("James",14))

def pay(hours,rate):
    return f"Pay: ${hours*rate:.2f}"

print(pay(8,17.50))

def format_score(score,decimals):
    return f"Score: {score:.{decimals}f}%"

print(format_score(87.465656757656, 3))

    

