# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
x= 5 + 3j
print(x)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
a=7-2j
b=a.real
print(b)

# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
a=4+6j
b=a.imag
print(b)

# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
a=(3 + 2j)
b=(1 + 4j)
c=a+b
print(c)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
a=(2 + 3j)
b=(1 + 2j)
c=a*b
print(c)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
a=6+8j
print(abs(a))

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
a=5 - 7j
print(complex(a))

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
a=(10 + 5j) - (3 + 2j)
print(a)
# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
a=(8 + 6j) / (2 + 1j)
print(a)

# Question 10: Find the phase angle of complex number 1 + 1jg
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
import cmath
a=1 + 1j
b=cmath.phase(a)
print(b)