# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
a=(3.14, 2.718, 1.618, 0.577)
b=sum(a)/len(a)
print(b)


# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
f=98.6
b=((f-32)*5/9)
print(b)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
p=1000
r=5.5
t=36
C=p*((1+r/t)**(r*t))
print(C)

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
a=3.5
b=4.2
hyp=math.sqrt((a*a)+(b*b))
print(hyp)

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
a=float(7.8)
b=math.pi*(4/3)*(r*r*r)
print(b)

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
a=round(3.14159,3)
print(a)

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
a=(45/67)*100
print(a)

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
a=23.456
b=math.sqrt(a)
print(b)

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
p=2500
r=6.5
t=29
S=p*(1+r/t)
print(S)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
a=45.7
b=a*math.pi/180 
print(b)