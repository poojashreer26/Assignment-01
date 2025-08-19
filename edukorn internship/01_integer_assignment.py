# INTEGER DATATYPE ASSIGNMENT
# ===========================
import math
# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
A= range(0,10)
B=math.prod(A)
print(B)


# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
remainder=(156%7)
print(remainder)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
a=(25**2)
print(a)
# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
a=(125**1/3)
print(a)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
a=range(1,6)
b=sum(a)
print(b)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
if 97%2==1:
   print(True)
else:
   print(False)   

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
n=range(1,9)
m=math.prod(n)
print(m)


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
a=(15,23,31,42,56)
print(sum(a)/len(a))


# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
a=math.gcd(48,36)
print(a)
# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
a=int (range(1,40))
if a%2!=0:
   b= Sum(a)
print(b)
