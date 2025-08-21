# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
a="Python Programming"
b=a[::-1]
print(b)

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
a="racecar"
if a==b:
   print("is palindrome")
else:
   print("not palindrome")

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
a="Python is a great programming language"
b=len(a)
print(b)

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
a='hello world'
b= a.title()
print(b)

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
a='Data Science'
b=len(a)
print(b)

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
a='Machine Learning'
b=a.replace(" ","_")
print(b)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
a= 'Python Programming Language'
b='python'
if a in b:
   print(True)
else:
   print(False)

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
a="Artificial Intelligence"
b=a[0:6]
print(b)

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
a="UPPERCASE"
b=a.lower()
print(b)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
a='Computer Science'
b=('a','e','i','o','u')
for i in a:
   if i not in b:
      print(i,end='')


# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
a="mississippi"
b=max(a)
print(b)

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
a="listen"
b="silent"
if sorted(a) not in sorted(b):
   print("True")
else:
   print("False")
   
  

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
a="python programming language"
b=a.title()
print(b)

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
a='Hello World'
b=('a','e','i','o','u')
count=0
for i in a :
   if i not in b and i.isalpha():
      count+=1
print(count)

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
a='Python is a programming language'
b=a.split()
for i in b:
   print(max(i),end='-')
   

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
a='Hello, World! How are you?'
b=a.replace(',',''),a.replace('World!','are you?')
print(b)



# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
a="Python"
print(a.startswith(a))

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
a= "Hello World"
b=a.index("o")
print(b)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
a="apple,banana,orange"
b=a.split(',')
print(b)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
a=['Python', 'is', 'awesome']
for i in a:
   if i != " ":
      print(i,end=" ")



# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
a='12345'
b=a.isdigit()
print(b)
# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
a="HelloWorld"
b=a.isalpha()
print(b)

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
a="hello world"
b=" "
for i in range(len(a)):
   if i%2==0:
      a+=a[i].upper()
   else:
      a+=a[i].lower()
print(a)
      


# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
a="banana"
b=[]
for i in range (0,len(a)):
  if a[i]=='a':
     b.append(i)
print(b)





# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
a="  Hello World  "
b= a.strip()
print(b)

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
a="programming"
b= a.endswith('ing')
print(b)

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
a="Hello World"
b=a.replace("o","0")
print(b)

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
a="Python is a programming language"
b=a.split()
print(min(b))

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
a='Python programming is powerful'
count=0
for i in a and a.lower():
   if i=='p':
      count+=1
print(count)

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
a='Hello World Python'
b=a[::-1]
print(b)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
a="user@example.com"
if '@' in a and '.' in a and  a.index('@') < a.index('.'):
   print('valid')
else:
   print('invalid')


# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
a="https://www.example.com/path"
b=a.split('/')[-1].split('//')[0]
print(b)

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
a='''the rain falls soft,
Agentle, whispered beat,
washing the world clean,
A melody so sweet'''
b=a.split(",")
print(len(b))




# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
a="hello"
b="world"
c=[]
for i in a:
   for j in b:
      if i==j:
         c.append(i)
print(c)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
a="+1-555-123-4567"
b=a.replace("-","")
if b.startswith('+1') and len(b)==12:
    print('vaild')
else:
    print('invalid')


# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
a="abc123def456ghi789"
b=a.isnumeric()
print(b)

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
a="snake_case"
b=a.replace('_','')
print(b)

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
a="A man a plan a canal Panama".lower()
b=a.replace(" ","")
c=a[::-1]
if a==b:
   print('is palandrome')
else:
   print('not palandrome')



# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
a="the quick brown fox jumps over the lazy dog"
b=a.split()
c=0
d=' '
for i in a:



# Question 40: Generate acronym from "National Aeronautics and Space Administration"
 print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
a="National Aeronautics and Space Administration"
b=a.split()
for i in b:
    if len(i)>3:
       print(i[0:1],end="")

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
a= "((()))"
if len(a)%2 == 0:
    print("is equal")
else:
    print("not equal")


# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
a=dict({'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/'})
b = "hello world"
c=[]
for i in a:
        c.append(a[i])
print(c)

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
a="programming"
b="grammar"
c=""
for i in range(len(a)):
   for j in range(i,len(a)+1):
      d=a[i:j]
      if a in b and len(d)>len(c):
         c.append(d)
print(c)


# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
a='https://www.google.com'
if a.startswith('http://')and a.endswith('.com' ):
    print('valid')
else:
    print('not valid')

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
a="Python programming is amazing and powerful"
b=a.split()
for i in b:
    if len(i)>5:
        print(i,end=",")

# Question 46: Convert "hello world" to Pig Latin


# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
a="192.168.1.1"
b=a.split('.')
for i in b:
    if int(i) in range(0,255):
        print('vaild')
    else:
        print('invalid')


# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
a='abc'
for i in range(len(a)):
   for j in range (i,len(a)+1):
      print(a[i:j],end=" ")

# Question 49: Convert "hello world" to ROT13 encoding


# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
a="4532015112830366"
if len(a)==16:
    print(True)
else:
    print(False)