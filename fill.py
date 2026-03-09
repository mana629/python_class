"""
question 1: Write a Python program to check if the number is positive, negative or zero.
i = int(input("Please enter your number: "))
 

if i> 0 :
    print("The number is positive")
elif i==0:
    print("The number is zero")
else:
    print("The number is negative")
    """
"""question 2: Write a Python program to check if the number is even or odd.   
i = int(input("Please enter your number: "))

if i % 2 == 0:
    print("The number is even")
else:   
     print("The number is odd")
"""
"""question 3: 3. Take age and print:
    - "Child" if age < 13
    - "Teen" if age 13–19
    - "Adult" otherwise 
i = int(input("Please enter your age: "))
if i < 13:
    print("child")
elif i >13 and i < 19:
    print("teen")
else:
    print("adult")"""
"""question 4: Write a Python program to check if the marks are distinction, first class, pass or fail.
m = int(input("Please enter your marks: "))

if m >= 80:
    print("distiction")
elif m >= 60 and m < 80:
    print("first class")
elif m >=35 and m < 60:
    print("pass")
else:
    print("fail")
    question 5: Write a Python program to check if the number is a multiple of 3 or 5.
i = int(input("Please enter your number: "))
if i % 3 == 0 or i % 5 == 0:
    print("true")
else:
    print("false")

Take two numbers and print which one is greater or if equal.
i = int(input("Please enter your number: "))
m = int(input("Please enter your number: "))
if i > m:
    print("i")
elif i == m :
    print("equal")
else:    print("m")

""" """1. Take a number and print:
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both
    - otherwise print number"""

i = int(input("Please enter your number: "))
if i % 3 == 0 :
    print("FizzBuzz")   
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
else:
    print(i)