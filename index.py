
Functions, Scoping, Data Collections 1 & List Comprehensions
Tasks Today:
Additions (or, and ... if statements)

String Manipulation
     a) strip()
     b) title()
Working With Lists
     a) min()
     b) max()
     c) sum()
     d) sort()
     e) Copying a List
     f) 'in' keyword
     g) 'not in' keyword
     i) Checking an Empty List
     j) Removing Instances with a Loop
List Comprehensions
Tuples
     a) sorted()
Functions
     a) User-Defined vs. Built-In Functions
     b) Accepting Parameters
     c) Default Parameters
     d) Making an Argument Optional
     e) Keyword Arguments
     f) Returning Values
     g) *args
     h) Docstring
     i) Using a User Function in a Loop
Scope
String Manipulation
.lstrip()
# string.lstrip()
name = "       hJohn Smith"
stripped_name = name.lstrip(" " "h")
print(stripped_name)
John Smith
.rstrip()
# string.rstrip()
name = "Bill Ross        th"
print(name.rstrip(" " "th"))
Bill Ross
.strip()
# string.strip()
name = "       John Smith         "
print(name.strip())
John Smith
.title()
# string.title()
president = "barack obama"
print(president.upper())
BARACK OBAMA
String Exercise
Strip all white space and capitalize every name in the list given

names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration

for name in names:
    justnames = name.strip()
    fixednames = justnames.upper()
    print(fixednames)
CONNOR
MAX
EVAN
JORDAN
Working With Lists
min()
# min(list)
numbers = [4, 5, 97, 54, 16]

print(min(numbers))
4
max()
# max(list)
numbers = [4, 5, 97, 54, 16]

print(max(numbers))
97
sum()
# sum(list)

print(sum(numbers))
176
sorted()
# sorted(list)
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
[4, 5, 97, 54, 16]
[4, 5, 16, 54, 97]
[4, 5, 97, 54, 16]
.sort()
Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list

# list.sort()
print(f"Before sort: {numbers}")
print(numbers.sort())
print(numbers)

# use sorted when you don't want to alter original list, use .sort() when you want to alter original list
Before sort: [4, 5, 97, 54, 16]
None
[4, 5, 16, 54, 97]
Copying a List
# [:] copies a list, doesn't alter original
list_1 = numbers[:]
print(list_1)
'in' keyword
l_teachers = ["Joel", "Derek", "Conner", "Brian", "Joe"]

#if "Pam" in l_teachers:
#   print("Coding Temple Instructor")
#else:
#   Print("Not an instructor")

for name in l_teachers:
    if "C" in name:
        print("Found")
    else:
        print("Not Found")
Not Found
Not Found
Found
Not Found
Not Found
'not in' keyword
if "Zack" not in l_teachers:
    print("Not a CT Instructor")
    
Not a CT Instructor
Checking an Empty List
# if l_1: or if l_1 = []
list_2 = []

if list_2 == []:
    print("Is Mayonnaise an instrument")
Is Mayonnaise an instrument
Removing Instances with a Loop
# while, remove
names = ["Conner", "Joel", "Max", "Evan", "Evan", "Rob"]

# while "Evan" in names:
#    names.remove("Evan")
# print(names)

for name in names:
    if name == "Evan":
        names.remove("Evan")

print(names)
['Conner', 'Joel', 'Max', 'Rob']
List Exercise
Remove all duplicates
Extra: Create a program that will remove any duplicates from a given list

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier

names = list(dict.fromkeys(names))
print(names)
['connor', 'bob', 'evan', 'max', 2, 3, 4, 'kevin']
List Comprehensions
Creating a quickly generated list to work with
*result* = [*transform* *iteration* *filter* ]

In a list comprehension we have a few pieces:
The first is the counter/ variable - IN this the variable is x
then we have a transform for the variable
The finale part of a list comp is called the condition
[variable, transform, condition]
# number comprehension

# With a regular for loop

nums = []

for i in range(100):
    if i % 2 == 0:
        nums.append(i**2)
print(nums)

print("\n")
nums_comp = [i**2 for i in range(100) if i % 2 == 0]
print(nums_comp)
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]


[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]
There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.

Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.

Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# square number comprehension

print([x**2 for x in range(10)])

print("\n")

squares_reg = []
for x in range(10):
    squares_reg.append(x**2)
print(squares_reg)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# string comprehension
names = ["Conner", "Max", "Evan", "Rob"]

first_char_comp = [name[0] for name in names]
print(first_char_comp)

first_char = []

for name in names:
    first_char.append(name[0])
print(first_char)
['C', 'M', 'E', 'R']
['C', 'M', 'E', 'R']
c_names = [first_name for first_name in names if first_name[0] == "C"]
print(c_names)

c_names_reg = []

for first_name in names:
    if first_name[0] == "C":
        c_names_reg.append(first_name)

print(c_names_reg)
['Conner']
['Conner']
 
Tuples
Defined as an immutable list


Seperated by commas using parenthesis
tup_1 = 1, 2, 3
tup_2 = (1,2,3)

print(tup_1[0])

print(len(tup_1))

for number in tup_1:
    print(number)

# for number in range(len(tup_1)):
#     popped_num = tup_1.pop()
#     print(tup_1[number])
1
3
1
2
3
sorted()
tup_3 = (20, 5, 1, 3, 9, 45)

sorted_tup = sorted(tup_3)
print(sorted_tup)

random_list = [3, 4, 66, 77, 33]
combine_list = sorted(sorted_tup + random_list)

new_tup = tuple(combine_list)

print(new_tup)
print(type(sorted_tup))
print(tup_3)
[1, 3, 5, 9, 20, 45]
(1, 3, 3, 4, 5, 9, 20, 33, 45, 66, 77)
<class 'list'>
(20, 5, 1, 3, 9, 45)
Adding values to a Tuple
print(tup_1)

tup_1 = tup_1 + (5,)
print(tup_1)
(1, 2, 3)
(1, 2, 3, 5)
Functions
User-Defined vs. Built-In Functions
def sayHello():
    return "Hello World"

print(sayHello())
Hello World
Accepting Parameters
def printFullName(first_name, last_name):
    return f"Hello, {first_name} {last_name}"

a_name = input("what is your first name? ")

print(printFullName("Joel", "Carter"))
print(printFullName(a_name, "Apol"))
print(printFullName("a", "Carter"))
print(printFullName("b", "Carter"))
print(printFullName("c", "Carter"))
print(printFullName("d", "Carter"))
Hello, Joel Carter
Hello, Brandon Apol
Hello, a Carter
Hello, b Carter
Hello, c Carter
Hello, d Carter
Default Parameters
def printAgentName(first_name, last_name = "Bond"):
    return f"The name is {last_name}... {first_name} {last_name}!"

print(printAgentName("James"))

# def printAgentAgain(last_name = "ever", first_name):
#     return f"Last name {last_name}, first name {first_name}!"

# print(printAgentName(first_name = "Greatest"))
The name is Bond... James Bond!
Making an Argument Optional
def printHorseName(first, middle = "", last = "Ed"):
    return f"Hello {first} {middle} {last}"

printHorseName("Mr")
'Hello Mr  Ed'
Keyword Arguments
def printSuperHero(name, power = "flying"):
    return f"The Hero's name is {name} and the superpower is {power}"

printSuperHero(power = "Spidey Sense", name = "Spider Man")
"The Hero's name is Spider Man and the superpower is Spidey Sense"
Creating a start, stop, step function
def my_range(stop, start=0, step=1):
    for i in range(start, stop, step):
        print(i)

my_range(20,5,2)
5
7
9
11
13
15
17
19
Returning Values
def addNums(num1, num2):
    return num1 + num2

addNums(5,2)
7
*args
def printArgs(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)

    for arg in args:
        print(arg)

    for kwarg in kwargs:
        print(kwarg)

printArgs(36, "DragonZord", "vanilla", 2, 3, testing="joel")
36
('DragonZord', 'vanilla', 2, 3)
{'testing': 'joel'}
DragonZord
vanilla
2
3
testing
Docstring
def printNames(list_1):
    for name in list_1:
        print(name)

printNames(["George", "Ramon", "Peter"])
help(printNames)
George
Ramon
Peter
Help on function printNames in module __main__:

printNames(list_1)

Using a User Function in a Loop
def printInput(answer):
    print(answer)

response = input("Are you ready to quit?? ")
while True:
    ask = input("What do you want to do? ")
    printInput(ask)

    response = input("Ready yet? ")
    if response.lower() == "quit":
        break
no
no
no
Function Exercise
Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
full_name = []
for i in range(len(first_name)):
    add = (first_name[i] + " " + last_name[i])
    full_name.append(add)

print(full_name)
['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
Scope
Scope refers to the ability to access variables, different types of scope include:
a) Global
b) Function (local)
c) Class (local)

number = 3

def myFunc():
    number = 6
    number += 4
    return number

print(number + 4)
print(myFunc())
7
10
Exercises
Exercise 1
Given a list as a parameter,write a function that returns a list of numbers that are less than ten


For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

newl_1 = []

for l in l_1:
    if l <= 10:
        newl_1.append(l)
    else:
        continue

print(newl_1)
[1, 5, 8, 9]
Exercise 2
Write a function that takes in two lists and returns the two lists merged together and sorted
Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_3 = sorted(l_1 + l_2)

print(l_3)
