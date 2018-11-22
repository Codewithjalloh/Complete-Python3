
print("(----- PYTHON TUTORIALS -----)")
# PYTHON SYNTAX
# Execute Python Syntax
print("hello World!")
print("Hello Python!")
print("Hello King!!")
print("Hello Something.......")

#Python Indentation
if 5 > 2:
    print("Five is greater than 2")

if 11 > 10:
    print("Eleven is greater than 10")

if 3 < 10:
    print("Three is not greather than 10")

# Comments
# This is a comment
print('Hello, World!')
print("This is a comment just used the # sign")

#Making a comment for you guys to read developers
print("Hello developers")

# Docstrings
'''
This is a multiline docstrings.
'''

"""
This is where you write as many comment
or notes you want and the compile will not
read this group of text
"""

'''
Say something, say something, say something
Say something, say something, say something
Say something, say something, say something
Say something, say something, say something
Say something, say something, say something
'''


# VARIABLES

x = 5
y = "John"
print(x)
print(y)

myName = "King"
my_name = "King 2"
myName3 = "King3"

firstName = "Malik"
secondName = "Shabara"
lastName = "King"

occupation = "Data Analytics"
jobTitle = "Manager"
role = "Customer Service Asssitance"

myAge = 31
myCurrentAge = 102
my_new_age = 12

salary = 34000
current_salary = 102000

luckyNumber: float = 1.2




xx = 4
xxx = ""

# Output Variables
myX = "awesome"
print("Python is " + myX)

someX = "Python is "
someY = "awesome"
both_x_and_y = someX + someY
print(both_x_and_y)


# NUMBERS
'''
There are three numeric types in Python:
int
float
complex
'''

int_x = 1
float_x = 2.8
complex_x = 1j
print(int_x)
print(float_x)
print(complex_x)

# int
int_1 = 1
int_2 = 38948439438349
int_3 = -324843
print(int_1)
print(int_2)
print(int_3)

# float
float_1 = 1.10
float_2 = 1.0
float_3 = -35.59
float_4 = 35e3
float_5 = 12E4
float_6 = 87.7e100
print(float_1)
print(float_2)
print(float_3)
print(float_4)
print(float_5)
print(float_6)

# Complex
complex_1 = 3+5j
complex_2 = 5j
complex_3 = -5j
print(complex_1)
print(complex_2)
print(complex_3)

# SPECIFY A VARIABLE TYPE
specificInt_1 = int(1)
specificInt_2 = int(2.8)
specificInt_3 = int("3")

print(specificInt_1)
print(specificInt_2)
print(specificInt_3)

specificFloat_1 = float(1)
specificFloat_2 = float(2.8)
specificFloat_3 = float("3")
specificFloat_4 = float("4.2")

print(specificFloat_1)
print(specificFloat_2)
print(specificFloat_3)
print(specificFloat_4)

specificString_1 = str("s1")
specificString_2 = str(2)
specificString_3 = str(3.0)

print(specificString_1)
print(specificString_2)
print(specificString_3)


# STRINGS

# get the character at position 1 (remember that the first character has the position 0)
string_a = "Hello, World!"
print(string_a[1])

# Substring. get the character from position 2 to position 5 (not included):
string_b = "Hello, World!"
print(string_b[2:5])

# the string() method removes any whitespace from the beginning or the end;
string_c = " Hello, World! "
print(string_c.strip())

# the len() method returns the length of a string:
string_d = "Hello, World!"
print(len(string_d))

# the lower() method returns the string in lower case
string_e = "Hello, World!"
print(string_e.lower())

# the upper() method returns the string in upper case:
string_f = "Hello, World!"
print(string_f.upper())

# the replace() method replaces a string with another string:
string_g = "Hello World!"
print(string_g.replace("H", "J"))

# the split() method splits the string into substrings if it finds instances of the separator
string_h = "Hello, World!"
print(string_h.split(","))




# OPERATORS

# Python Arithmetic Operators
'''
# Python Arithmetic Operators
Operator
+   Addition            x + y
-   Subtraction         x - y
*   Multiplication      x * y
/   Division            x / y
%   Modulus             x % y
**  Exponentiation      x ** y
//  Floor Division      x // y
'''
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1%2)
print(10**20)
print(9//2)

a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c = a - b
print("Line 2 - Value of c is ", c)

c = a * b
print("Line 3 - Value of c is", c)

c = a / b
print("Line 4 - Value of c is ", c)

c = a % b
print("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b
print("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b
print("Line 7 - Value of c is ", c)


# Python Assignment Operators
'''
Operator        Example         Same As
=               x = 5           x = 5
+=              x += 3          x = x + 3
-=              x -= 3          x = x - 3
*=              x *= 3          x = x * 3
/=              x /= 3          x = x / 3
%=              x %= 3          x = x % 3
//=             x // = 3        x = x // 3
**=             x ** = 3        x = x ** 3
&=              x &= 3          x = x & 3
|=              x |= 3          x = x | 3
^=              x ^= 3          x = x ^ 3
>>=             x >>= 3         x = x >> 3
<<=             x <<= 3         x = x << 3
'''



# Python Comparison Operators

'''
# Python Comparison Operators
== (a == b) is not true
!= (a! = b) is true
>  (a > b) is not true
<  (a < b) is true
>= (a >= b) is not true
<= (a <= b) is true
'''
a = 21
b = 10

if ( a == b):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if ( a != b ):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if ( a < b ):
    print("Line 3 - a is less than b ")
else:
    print("Line 3 - a is not less than b")

if ( a > b):
    print("Line 4 - a is greater than b")
else:
    print("Line 4 - a is not greater than b ")
a,b = b,a

if ( a <= b ):
    print("Line 5 - a is either less than or equal to b")
else:
    print("Line 5 - a is neither less than nor equal to b")

if ( b >= a ):
    print("Line 6 - b is either greater than or equal to b")
else:
    print("Line 6 - b is neither greater than nor equal to b")



# Python Logocal Operators
'''
and      returns True if both statements are true                   x < 5 and x < 10
or       returns True if one of the statement is true               x < 5 or x < 4
not      reverse the result, returns False if the result is true    not (x < 5 and x < 10)
'''

# Python Identify Operators
'''
is      returns true if both variables are the same object         x is y
is not  returns true if both variables are not the same object     x is not y
'''


# Python Membership Operators
'''
in      returns True if a sequence with the specified value is present in the object            x in y
not in  returns True if a sequence with the specified value is not present in the onbecjt       x not in y

'''

# Python Bitwise Operators
'''
&       AND                     Set each bit to 1 if both bits are 1
|       OR                      Sets each bit to 1 if one if two bits is 1
^       XOR                     Sets each bit to 1 if only one of two bits is 1
~       NOT                     Inverts all the bits
<<      Zero fill left shift    Shift left by pusshing zeros in from the right and let the leftmost bits fall off
>>      Signed right shift      Shit right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''

# PYTHON LISTS
'''
There are four collection data type in the Python programming language:
List: is a collection which is ordered and changeable. allows duplicate memebers
Tuple: is a collection which is ordered and uchangeable. allows duplicate memebers
Set: is a collection which is unordered and unindexed. No duplicate members
Dictionary: is a collection which unordered, changeable and indexed. No duplicate memebersself.
'''

# list
thisIsList = ["apple", "banana", "cherry"]
print(thisIsList)

# access items
thisIsList = ["apple", "bababa", "cherry"]
print(thisIsList[1])

# Change item value
thisIsList = ["apple", "banana", "cherry"]
thisIsList[1] = "Blackcurrant"
print(thisIsList)

# loop throught a list
thisIsList = ["apple", "banana", "cherry"]
for x in thisIsList:
    print(x)

# check if item exist
thisIsList = ["apple", "bababa", "cherry"]
if 'apple' in thisIsList:
    print("Yes", "apple is in the fruits list")

# List length
thisIsList = ["apple", "banana", "cherry"]
print(len(thisIsList))

# add items
thisIsList = ["apple", "banana", "cherry"]
thisIsList.append("orange")
print(thisIsList)

thisIsList = ["apple", "banana", "cherry"]
thisIsList.insert(1, "orange")
print(thisIsList)


# remove item
# remove() method removes specified item:
thisIsList = ["apple", "banana", "cherry"]
thisIsList.remove("banana")
print(thisIsList)

# pop() method removes the specified index (or the last item if index is not specified)
thisIsList = ["apple", "banana", "cherry"]
thisIsList.pop()
print(thisIsList)

# del keyword removes the specified index:
thisIsList = ["apple", "banana", "cherry"]
del thisIsList[0]
print(thisIsList)

# del keyword can also delete the list competely
thisIsList = ["apple", "banana", "cherry"]
del thisIsList
print(thisIsList) # this will cause an error becuase "thisIsList" no longer exist

# clear() method empties the list:
thisIsList = ["apple", "banana", "cherry"]
thisIsList.clear()
print(thisIsList)

# The list() Constructor
# using the list() constructor to make a list:

thisIsList = list(("apple", "banana", "cherry")) # note the double round-backets
print(thisIsList)

'''
method          Description
appen()         Adds an element at the end of the list
clear()         Removes all the element from the list
copy()          Returns a copy of the list
count()         Returns the number of elements with the specified value
extend()        Add the elements of a list (or any iterable), to the end of the current list
index()         Returns the index of the first element with the specified value
insert()        Adds an element at the specified pesition
pop()           Removes the element at the specified position
remove()        Removes the item with the specified value
reverse()       Reserses the order of the list
sort()          Sorts the list

'''

# TUPLES
# a tuple is a collection which is ordered and unchangeableself.

thisIsTuple = ("apple", "banana", "cherry")
print(thisIsTuple)


# access tuple items
thisIsTuple = ("apple", "banana", "cherry")
print(thisIsTuple[1])

# chenage tuple values
thisIsTuple = ("apple", "banana", "cherry")
thisIsTuple[1] = "Blackcurrant"
# the value will remain the same:
print(thisIsTuple)

# Loop Through a Tuple
thisIsTuple = ("apple", "banana", "cherry")
for x in thisIsTuple:
    print(x)

# check if item exist
thisIsTuple = ("apple", "banana", "cherry")
if "apple" in thisIsTuple:
    print("Yes", "apple is in the fruits tuple")

# tuple length
# to determine how many items a list have, use the len() method:

thisIsTuple = ("apple", "banana", "cherry")
print(len(thisIsTuple))

# Add items
# once a tuple created, you cannot add items to it. Tuples are unchangeable
thisIsTuple = ("apple", "banana", "cherry")
thisIsTuple[3] = "orange" # this will raise an error
print(thisIsTuple)

# Remove Items
# note: you cannot remove items in a tupleself.

# del keyword can delete the tup;e completely:
thisIsTuple = ("apple", "banana", "cherry")
del thisIsTuple
print(thisIsTuple) # this will raise an error because the tup;e no longer

# The tuple() constructor
thisIsTuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thisIsTuple)


# Tuple Methods
'''
Method          Description
count()         Returns the number of times a specified value occurs in a tuple
index()         Searches the tuple for a specified value and returns the position of where it was found

'''

# PYTHON SETS
# a set is a collection which is unordered and unindexed. In Python sets are written ith curly bracketsself.
thisIsSet = {"apple", "banana", "cherry"}
print(thisIsSet)

# Acess Items
# loop through the set, and print the values;

thisIsSet = {"apple", "banana", "cherry"}

for x in thisIsSet:
    print(x)

# check if "banana" is present in the set
thisIsSet = {"apple", "banana", "cherry"}
print("banana" in thisIsSet)

# Change Items
# one a set is created, you cannot change its items, but you can add new itemsself.


# Add Items
# add one item to a set use the add() method
# add more that one item item to a set use the update() method

thisIsSet = {"apple", "banana", "cherry"}
thisIsSet.add("orange")
print(thisIsSet)

# add multiple items to a set, using the update() method
thisIsSet = {"apple", "banana", "cherry"}
thisIsSet.update(["orange", "mango", "grapes"])
print(thisIsSet)

# Get the length of a Set
# to determine how many items a set have, use the len() method
thisIsSet = {"apple", "banana", "cherry"}
print(len(thisIsSet))

# Remove item
# remove an item in a set, use the remove(), or the discard() method

# remove "banana" by using the remove() method
thisIsSet = {"apple", "banana", "cherry"}
thisIsSet.remove("banana")
print(thisIsSet)

# remove "banana" by using the discard() method
thisIsSet = {"apple", "banana", "cherry"}
thisIsSet.discard("banana")
print(thisIsSet)

# pop() method to remove an item
thisIsSet = {"apple", "banana", "cherry"}
x = thisIsSet.pop()
print(x)
print(thisIsSet)

# the clear() method empties the set:
thisIsSet = {"apple", "banana", "cherry"}
thisIsSet.clear()
print(thisIsSet)

# del keyword with delete the set completely
thisIsSet = {"apple", "banana", "cherry"}
del thisIsSet
print(thisIsSet)

# The set() Constructor
# it is also possible to use the set() constructor to make a set
thisIsSet = set(("apple", "banana", "cherry"))
print(thisIsSet)

'''
Method                  Description
add()                   adds an element to the set
clear()                 removes all the elements from the set
copy()                  returns a copy of the set
difference()            returns a set containing the different between two or more sets
difference_update()     removes the items in this set that are also include in another, specified set
discard()               remove the specifield item
intersection()          returns a set, that is the intersection of two other sets
intersection_update()   removes the items in this set that are present in other, specifield sets(s)
isdijoint()             returns whether two sets have a intersection or not
issubset()              returns whether anoher set contains another set or not
issuperset()            returns whether this set contains another set or not
pop()                   removes the specified element
remove()                removes the specified element
symmetric_difference()  returns a set with the symmetric difference of two sets
symmetric_difference_update()   inserts the sysmmetric differences from this set and another
union()                 returns a set containing the union of sets
update()                update the set with the union of this set and others

'''

# DICTIONARY
thisIsDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisIsDict)

# accessing item
x = thisIsDict["model"]

# get() method will give you the accessing result
x = thisIsDict.get("model")

# Change Values
thisIsDict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964
}
thisIsDict["year"] = 2018

# loop through a dictionary
for x in thisIsDict:
    print(x)

for x in thisIsDict:
    print(thisIsDict[x])

# you can use the values() function to return values of a dictionary
for x in thisIsDict.values():
    print(x)

# loop through both keys and values, by using the item() function
for x, y in thisIsDict.items():
    print(x, y)


# check if Key Exists
thisIsDict = {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
}

if "model" in thisIsDict:
    print("Yes, 'model' is one of the keys in the thisIsDict dictionary ")

# dictionary length
# to determine how many items (key-value-pairs) a dictionary have, use the len() method
print(len(thisIsDict))

# adding items
thisIsDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

thisIsDict["color"] = "red"
print(thisIsDict)

# removing items
# using the pop mehod removes the item with specific key name
thisIsDict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}

thisIsDict.pop("model")
print(thisIsDict)

# popitem()
thisIsDict = {
"brand": "ford",
"model": "mustang",
"year": 1964
}
thisIsDict.popitem()
print(thisIsDict)

# del keyword remove the item with specific key name
thisIsDict = {
"brand": "ford",
"model": "mustang",
"year": 1964
}
del thisIsDict["model"]
print(thisIsDict)

# del also delete the whole dictinary

# clear() keyword empties the dictionary
thisIsDict = {
"brand": "ford",
"model": "mustang",
"year": 1964
}
thisIsDict.clear()
print(thisIsDict)


# the dict() constructor
thisDict = dict(brand="ford", model="mustang", year=1964)
# note that keyword are not string literal
# note the use of equals rather than colon for the assignment
print(thisDict)

'''
Method              Description
clear()             Removes all the elements from the dictionary
copy()              Returns a copy of the dictionary
fromkeys()          Returns a dictionary with specified keys and values
get()               Returns the value of specified key
items()             Returns a list containing the a tuple for each key valye pair
keys()              Returns a list containing the dictionary's keys
pop()               Removes the element with specifified key
popitem()           Removes the last inserted key-value pair
setdefault()        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()            Updates the dictionary with specified key-value pairs
values()            Returns a list of all the values in the dictionary
'''

# IF... ELSE
'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

An "if statement" is written by using the if keyword

'''
a = 33
b = 200
if b > a:
    print("b is greater than a")


# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")

# else
a = 200
b = 33
if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b ")


a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# short hand if
if a > b: print("a is greater than b")

# short hand if... else
print("A") if a > b else print("B")

# multiple else statements on the same line
print("A") if a > b else print("=") if a == b else print ("B")

# and
# and keyword is a logical operator
if a > b and c > a:
    print("Both conditions are True")

# or
# or keyword is a logical operator, and is used to combine condition statement
if a > b or a > c:
    print("At least one of the conditions are True")


# LOOPS
# python has two primitive loop commands: while loop and for loop

# the while loop
i = 1
while i < 6:
    print(i)
    i += 1

# the break statememt
# with the break statement we can stop the loop event if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# the continue statement
# with the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# For Loops
# for loop is used to iterating over
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through a string
# even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)

# the break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)


# the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# the range() function
# loop through a set of code a specified number of times, we can use the range() function

for x in range(6):
    print(x)

# range() function defualts to 0 as starting value range(2, 6) which mean values from 2 to 6
for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)


# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finsihed")

# nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# recursion
# also accepts function recursion, which means a defined function can call itselfself.
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# FUNCTIONS
# a function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function a function can return data as a resultself.

# creating a function
def my_function():
    print("Hello from a function")

# calling a function
def our_function():
    print("Hello from a function")

my_function()

# parameters
# information can be passed to functions as paramters
def my_function(fnmae):
    print(fname + " refsnes")

my_function("email")
my_function("Tobias")
my_function("Linus")

# Default parameter value
# the following example
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# return values
# to let a function return a value, use the return statement
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# LAMBDA
# a lambda function is a small anonymous functionself.
x = lambda a : a + 10
print(x(5))

# a lambda function that multiplies argument a with argument b and print result
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# why use lambda functions?
# power of lambda is better shown when you use them as an annoymous function
def myfunc(n):
    return lambda a : a * n

# use that function definition to make a function that always doubles the number you send in
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# use the same function definition to make both functions, in the same program
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# ARRAYS
# create an array containing car names
cars = ["Ford", "Volvo", "BMW"]

# an array is special variable, which hold more than one value at a time
car1 = "Ford"
car2 = "Volvo"
car3 = "BMB"

# Access the element of an Array
x = cars[0]
cars[0] = "Toyota"

# the length of an array
x = len(cars)

# looping array elements
for x in cars:
    print(x)

# adding array elements
# you can use the append() method to add an element to an array
cars.append("Honda")

# removing arrays elements
# you can use the pop() method to remove an element from the array
cars.pop(1)

# you can also use the remove() method
cars.remove("Volvo")

'''
Method          Description
append()        adds an element at the end of the list
clear()         removes all the elements from the list
copy()          returns a copy of the list
count()         returns the number of elements with the specifield value
extend()        add the elements of a list (or any iterable), to the end of the current list
index()         returns the index of the first element with specified value
insert()        adds an element at the specified position
remove()        removes the first item with the specified value
sort()          sorts the list
'''

# CLASSES AND OBJECTS
'''
Python is an object oriented programming languageself.
Almost everything in python is an object, with its properties and methods
A class is like an object constructor, or a "blueprint" for creating objects.
'''

# Create a class
# create a class named MyClass, with property named x:
class MyClass:
    x = 5

# Create Object
# we can use the class named myClass to create objects
p1 = MyClass()
print(p1.x)

# The __init__() Function
'''
The example above are classes and objects in their simplest form, and are not really useful in real life application

to understand the meaning of classes we have to understand the built-in __init__() functionself.

all the classes have a function called __init__(), which is always executed when the class is being initiatedself.

Use the __init__() function to assign values to object properties, or other operations that are neccessary to do when the object is being created:

'''

# create a class named Person, used the __init__() function to assign values for name and age:
# the __init__() function is called automatically every time the class is being used to create a new object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# The Self Parameter
# the self parameter is a reference to the class itself, and is used to access variable that belong to the class
# it does not have to be named self, you can call it whetever you like, but it has to be the first paramater of any function in the class

# use the words mysillyobject and abc instead or self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# modify object properties
p1.age = 40

# Delete object properties
del p1.age

# Delete Objects
del p1

# ITERATORS
# An iterator is an object that contains a countable number of valuesself.
'''
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

# Iterator VS Iterable
# lists, tuples, dictionaries, and sets are all iterable objects. they are iterable containers which you can get an itertor from
# all these objects have a iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# even string are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Looping Through an iterator
# we can also use a for loop to iterate through an iterable object:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# iterate the character of a string:
mystr = "banana"

for x in mystr:
    print(x)

# Create an Iterator
'''
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

'''

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1, 2, 3,4, 5, 5 etc.)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
# the example above would contine forever if you had enough next() statement
'''

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# MODULES
# what is a module?
# consider a module to be the same as code library
# a file containing a set of functions you want to include in your application

# Create a module
# create a module just save the code you want in a file with the file extension .py:

# save this code in a file named mymodule.py
def greeting(name):
    print("Hello, " + name)

# Use a module
import mydodule

mydodule.greeting("Jonathan")

# Variable in module
# the module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
# save this code in the file mymodule.py

person = {
    "name": "john",
    "age" : 36,
    "country": "Norway"
}

# import the module named mymodule, and access the person1 dictionary:
import mymodule

a = mymodule.person1["age"]
print(a)

# Naming a Module
# re-naming a module
# you can create an alias when you import a module, by using the as keyword:
# create an alias for mymodule called mx:

import mymodule as mx
a = mx.person1["age"]
print(a)


# Built-in Modules
# are several built-in modules in python, which you can import whenever you likeself.

# import and use the platform module:
import platform

x = platform.system()
print(x)


# Using the dir() Function
# there is a built-in function to list all the function names (or variable names ) in a moduleself. the dir() function

# list all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x)

# Import From Module
# you can choose to import only parts from a module, by using the from keywordself.

# the module named mymodule has one function and one dictionary:

def greeting(name):
    print("Hello", + name)

person = {
 "name" : "John",
 "age" : 36,
 "country" : "Norway"

}

# Import only the person1 dictionary from the module:

from mymodule import person1
print(person1["age"])

# DATETIME

# python dates
# a date in python is not a date type of its own, but we can import a module named datetime to work with dates as date objects

import datetime

x = datetime.datetime.now()
print(x)

# Date Output
'''
When we execute the code from the example above the result will be:

2018-10-20 17:19:53.042189
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

'''
# return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# to create a date, we can use the dateTime() class (constructor) of the datetime module
# the datetime() class requries three parameters to create a date: year, month, day

# create a date object
import datetime

x = datetime.datetime(2020,5,17)
print(x)

'''
The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
'''

# The strftime() method
'''
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
'''

# display the name of the month
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

'''
Directive	Description	Example	Try it
%a	Weekday, short version	Wed
%A	Weekday, full version	Wednesday
%w	Weekday as a number 0-6, 0 is Sunday	3
%d	Day of month 01-31	31
%b	Month name, short version	Dec
%B	Month name, full version	December
%m	Month as a number 01-12	12
%y	Year, short version, without century	18
%Y	Year, full version	2018
%H	Hour 00-23	17
%I	Hour 00-12	05
%p	AM/PM	PM
%M	Minute 00-59	41
%S	Second 00-59	08
%f	Microsecond 000000-999999	548513
%z	UTC offset	+0100
%Z	Timezone	CST
%j	Day number of year 001-366	365
%U	Week number of year, Sunday as the first day of week, 00-53	52
%W	Week number of year, Monday as the first day of week, 00-53	52
%c	Local version of date and time	Mon Dec 31 17:41:00 2018
%x	Local version of date	12/31/18
%X	Local version of time	17:41:00
%%	A % character	%

'''

# JSON
# JSON is a syntax for storing and exchanging data
# JSON is text, writtem with javaScript object notation

# JSON in Python
# python has a built-in package called json, which can be used to work with JSON Data

# import the json module
import json

# Parse JSON - Convert from JSON to Python
# if you have a JSON string, you can parse it by using the json.loads() method

# convert from JSON to python
import json

# some JSON:
x = '{"name":"json"m "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary:
print(y["age"])

# Convert from Python to JSON
# if you have a python object, you can convert it into a JSON string by using the json.dumps() method

# convert from python to json
import json

# a python object (dict):
x = {
    "name": "john",
    "age" : 30,
    "city" : "New York"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string:
print(y)

'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

'''

# convert python objects into JSON strings, and print the values
import json

print(json.dumps({"name": "john", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null

'''
# convert a python object containing all the legal data types
import json

x = {
    "name" : "john",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars" : [
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"ford edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))


# Formart the Result
# the example above print a json string, but it is not very easy to read, with no indentation and line break
# The json.dumps() method has parameters to make it easier to read the result:

# use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

# use the separators parameter change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))


# use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)

# PIP

# what is pip?
# Pip is a package manager for python packages, or modules if you like

# what is a package?
# a package contains all the files you need to a module
# modules are python code libraries you can include in your projectself.

# Check if PIP is installed
pip --version

# Install Pip
# pip install camelcase

# Using A Package
import camelcase

c = camelcase.CamelCase()

txt "Hello world"

print(c.hump(txt))

# Find Packages
https://pypi.org/.


# TRY EXCEPT
# the try block let you test a block of code of erros
# the except block lets you handle the error
# the finally block lets you execute code, regardless of the result of the try - and except blocks


# Exception Handling
# when an error occurs, or exception as we call it, Python will normal stop and generate an error message
# These exceptions can be handle using the try statement:

# the try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")

# This statement will raise an error, because x is not defined:
print(x)

# Many Exceptions
# you can define as many exception blocks as you want e.g if you want to execute a special block of code for a special kind of error

# print one message if the block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
# you can use the else keyword to define a block of code to be executed if no erros were raised:
# In this example, the try block does not generate any error:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
# the finally block, if specified, will be executed regardless if the try block raises an error or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


print("(----- FILE HANDLING -----)")
# FILE OPEN
# file handling is an important part of any web application
# python has several functions for creating, reading, updating, and deleting files


# File Handling
# the key function for working with files in python is the open() function
# the open() function takes two parameters: filename, and mode

'''
There are four different method (modes) for openning a file

"r" - Read - Default value. Open a file for reading, error if the file does not exist
"a" - Append - Open a file for appending, creates the file if it does not exits
"w" - Write - Open a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, return and error if the file exists

"t" - Text - default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''

# to open a file for reading it is enough to specify the ame of the file
f = open("demofile.txt")

# the code above is the same as:
f = open("demofile.txt", "rt")

# because "r" for read, and "t" for text are the default values, you do not need to specify them

# FILE OPEN
# asume we have the following file, located in the same folder as Python:

demofile.txt
Hello! Welcome to demofile.tx
This file is for testing purposes
Good Luck!!


# to open the file, use the built-in open() function
# the open() function return a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# Read Only Parts of the File
# by default the read() method returns the whole text, but you can also specify how many character ypu want to return:

# return the 5 first characters of the file
f = open("demofile.txt", "r")
print(f.read(5))

# Read lines
# you can return one line by using the readline() method;

# read one line of the file
f = open("demofile.txt", "r")
print(f.readline())

# by looping through the lines of the file, you can read teh whole file, line by line
# loop through the file by line
f = open("demofile.txt", "r")
for x in f:
    print(x)


# FILE WRITE
# Write to an Existing File

# to write to an exitsing file, you must add a paramater to the open() function
'''
"a" - Append - Will append to the end of the file
"w" - Write - Will overwrite any existing content
'''

# open the file "demofile.txt" and append content to file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line")

# open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Whoops! I have deleted the content!")

# the "w" method will overwrite the entire file


# Create a New File
'''
To create a new file in Python, use the open() method, with one if the following paramaters

"x" - Create - Will create a file, returns an error if the file exist
"a" - Append - Will create a file if the specified file does not exist
"w" - Write - Will create a file if the specified file does not exist

'''

# create a file called "myfile.txt"
f = open("myfile.txt", "x")
# result: a new empty file is created!

# create a new file if it does not exist
f = open("myfile.txt", "w")

# DELETE FILE
# to delete a file, you must import the OS module, and runs its os.remove() function:

# remove the file "demofile.txt"
import  os
os.remove("demofile.txt")

# Check if File Exist:
# to avoid getting an error, you might want to check if the file exist before you try to delete it:
# check if file exist, then delete it

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete Folder
# to delete an entire folder, use the os.rmdir() method

# remove the folder "myfolder":

import os
os.rmdir("myfolder")
# you can only remove empty folders

print("(----- PYTHON MYSQL -----)")

# MYSQL
# one of the most popular database in MySQL

# Install MySQL Drive
# python -m pip install mysql-connector

# Test MySQL Connector
import mysql.connector

# Create Connection
# start by creating a connection to the database
# Use the username and password from your MySQL database

# demo_mysql_connection.py

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    password="yourpassword"
)
print(mydb)

# Creating a Database
# to create a database in MYSQL, use the "CREATE DATABASE" statement:

# create a database named "mydatabase"

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
# if the above code was executed with no errors, you have successfully created a database

# Check if Database Exist
# you can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement
# return a list of your system's databases

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# or you can try to access the database when making the connection:
# try connecting to the database "mydatabase"

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)


# CREATE TABLE
# to create a table in MYSQL, use the "CREATE TABLE" Statement
# Make sure you define the name of the database when you create the connection

# Create a table named "customers":

import mysql.connector

mydb = mysql.connector.connect (

    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# check if Table Exists
# return a list of your system's databases
import mysql.connector

mydb = mysql.connector.connect (

    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatbase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# Primary Key
# create primary key when creating the table

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT
PRIMARY KEY, name, VARCAR(255), address(VARCHAR(255)))")

# if the table already exist, use the ALTER TABLE keyword:

# Create primary key on an existing table
import mysql.connector

mydb = mysql.connector.connector(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE Customers AND COLUMN id INT AUTO_INCREMENT PRIMARY Key")


# INSERT INTO TABLE
# To fill a table in MYSQL, use the "INSERT INTO" statement

# insert a record in the customer table

import mysql.connector

mydb = mysql.connector.connect (

    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatbase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")

# notice the statememt: mydb.commit() it is required to make the changes, otherwise no changes are made to the table

# Insert Multiple Rows
# To insert multiple rows into a table, use the executemary() method

# the second paramater of the executemary() method is a list of tuples, containing the data you want to insert:

import mysql.connecor

mydb = mysql.connector.connect(

    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hananh', 'Mountain 21'),
    ('Micheal', 'Valley 245'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One wat 98'),
    ("Vicky", 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted")

# Get Inserted ID:

# insert one row, and return the ID :
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    passwd = "yourpassword",
    database = "mydatabse"

)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

# SELECT FROM
# to select from a table in MySQL, use the "SELECT" Statement:

# select all records from the "customer" table, and display the result:

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fecthall()

for x in myresult:
    print(x)


# Using the fecthone() Method
# fetchone() method will return the first row of the result:

# fecth only one row
import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)



# SQL WHERE
# select records where the address is "Park Lane 38": result

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"

)

sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# Wildcard Characters
# use the % to represent wildcard character

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"

)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# Prevent SQL Injection
# escaoe query values by using the placeholder %s method:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"

)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ORDER BY
'''
Use the ORDER by statement to sort the result in ascending or descending order
The ORDER BY Keyword sorts the result ascending by default. to sort the result in descending order, use the DESC keyword

'''

# sort the result aplhabetically by name

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"

)

mycursor = mydb.cursor()

sql = "SELECT *  FROM Customers ORDER BY Name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Order by DESC
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"

)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY Name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# DELETE FROM BY
# you can delete records from an existing table by using the DELETE FROM statement

# delete any record where the address is "Mountain 21"

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"
)

mycursor = mydb.cursor()

sql = "DELETE FROM Customers WHERE address = 'Mountain 21' "
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

'''
Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!

'''
# prevent sql injection

'''
It is considered a good practice to escape the values of any query, also in delete statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:
'''

# escape values by using the placeholder %s method:
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"
)

mycursor = mydb.cursor()

sql = "DELETE FROM Customers WHERE address = %s"
adr = ("Yellow Garden 2")

mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# DROP TABLE
# you can delete an existing table by using the DROP TABLE statement
# delete the table customers

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)


# Drop only if exist
# delete the table "customers" if it exist
import mysql.connector

mydb = mysql.connector.connect (

    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

# UPDATE TABLE
# you can update existing records in a table by using the "UPDATE" statement

# overwrite the address column from "values 345" to "Canyoun 123"

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

'''
Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated. If you omit the WHERE clause, all records will be updated!

'''

# Prevent SQL Injection
'''
It is considered a good practice to escape the values of any query, also in update statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:
'''

import mysql.connector

mydb = mysql.connector.connect (
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) afftected")


# MYSQL LIMIT
# limit the result
# you can limit the number of records returned from the query, by using the "LIMIT" statement
# select the 5 first records in the "customers table"
import mysql.connector

mydb = mysql.connector.connect (
        host="localhost",
        user="yourusername",
        passwd="yourpassword",
        database="mydatabse"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# Start from Another Position
# start from position 3, and return 5 records

import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# MYSQL JOIN

# Join two or more tables
# you can combine rows from two or more tables, based on a related column between them, by using a JOIN Statement
# consider you have a "users" table and a "products" table:

# join users and products to see the name of the users favorite product:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabse"
)

mycursor = mydb.cursor()

sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.
'''

# Left Join
'''
In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.

If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
'''

# Select all users and their favorite product:
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    LEFT JOIN products ON users.fav = products.id"

# Right Join
'''
If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
'''
# select all products, and the user(s) who have them as their favorite
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id"

print("(----- PYTHON MONGODB -----)")












print("(----- PYTHON REFERNCE -----)")


# BUILD-IN FUNCTIONS
# python has a set of build-in functions:

# abs()         Returns the absolute value of a number
# return the absolute value of a number
x = abs(-7.25)

# return the absolute value of a complex number
x = abs(3+5j)

#all()          Returns True if any item in an iterable object are true
# check if all items in a list are True:
mylist = [True, True, True]
x = all(mylist)

# more examples
# check if all items in a list are True
mylist = [10, 1, 1]
x = all(mylist)

# check if all items in a tuple are True
mytuple = (0, True, False)
x = all(mytuple)

# check if all items in a set are True:
myset = {0, 1, 0}
x = all(myset)

# check if all items in a dictionary are True
mydict = {0:"Apple", 1:"Orange"}
x = all(mydict)

# any()         Returns True if any item in an iterable object is true
# check if any of the items in a list are true

mylist = [False, True, False]
x = any(mylist)

# more examples
mytuple = (0, 1, False)
x = any(mytuple)

myset = {0, 1, 0}
x = any(myset)

mydict = {0: "Apple", 1:"Orange"}
x = any(mydict)

# ascii()       Returns a readable version of an object. replaces non-ascii characters with escape character
x = ascii("My name is Ståle")
# å will be replaced with \xe5

# bin()         Returns the binary version of a number
x = bin(36)
# the result will aways start with the prefix 0b

# bool()        Returns the boolean value of the specified object
x = bool(1)


# bytearray()  Returns an array of bytes
 x = bytearray(4)

# syntax bytearray(x, encoding, error)
# param values

'''
parameter               Description
x                       a source to use whe creating the bytearray object
encoding                the encoding of the string
error                   specifies what to do if the encoding fails

'''

# bytes()      Return a bytes object
x = bytes(4)
# syntax bytearray(x, encoding, error)

# callable()        Returns True if the specified object is callable, otherwise false
def x():
    a = 5
print(callable(x))

# a normal variable is not callable
x = 5
print(callable(x))

# char()        Returns a character from the specified unicode code
x = chr(97)

# classmethod()     Converts a method into a class method

# compile()         Returns the specified source as an object, ready to be executed
mytext = "print(55)"
x = compile("mytext", "test", "eval1")
exec(x)

# syntax compile(source, filename, mode, flag, dont_inherit, optimze)
# compile more than one statement, and the execute it:

mytext = "print(55)\nprint(88)"
x = compile("mytext", "test", "exec")
exec(x)

# complex()     Returns a complex number
# convert the number 3 ad imagiary number 5 into a complex number:
x = complex(3, 5)

# syntax(real, imaginary)

# convert a string into a complex numbers
x = complex('3+5j')

# delattr()     Deletes the specified attribute (property or method) from the specified object
# delete the "age" property from the "person" object
class Person:
    name = "John"
    age = 36
    country = "Norway"

delattr(Person, 'age')

# syntax(object, attribute)

# dict()        Returns a dictionary(Array)
# create a dictionary containing personal information:

x = dict(name ="john", age = 36, country="Norway")

# dict(keyword arguments)

# dir()     Returns a list of the specified objects properties and methods
# display the content of an object
class Person:
    name = "John"
    age = 36
    country = "Norway"
print(dir(Person))

#divmod()       Returns the quotient and the remainder when argument1 is divide by argument2
# display the quotient and the remainder of 5 divided by 2:
x = divmond(5, 2)
# syntax(divident, divisor)


# enumerate()       Takes a collection (e.g a tuple) and returns it as an enumerate object
# convert a tuple into an enumerate object
x = ("apple", "banana", "cherry")
y = enumerate(x)

# syntax(iterable, start)

# exec()	Executes the specified code (or object)
# execute a block of code
x = 'name = "John"\nprint(name)'
exec(x)

# exec(object, globals, locals)

# filter()	Use a filter function to exclude items in an iterable object
# return the array with only values above 18:

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myfunc, ages)

for x in adults:
    print(x)

# syntax(function, iterable)

# float()	Returns a floating point number
x = float(3)

# more examples
x = float("3.500")


# format()	Formats a specified value
x = format(0.5, '%')
# syntax format(value, format)

'''
format	The format you want to format the value into.
Legal values:
'<' - Left aligns the result (within the available space)
'>' - Right aligns the result (within the available space)
'^' - Center aligns the result (within the available space)
'=' - Places the sign to the left most position
'+' - Use a sign to indicate if the result is positive or negative
'-' - Use a sign for negative values only
' ' - Use a leading space for positive numbers
',' - Use a comma as a thousand separator
'_' - Use a underscore as a thousand separator
'b' - Binary format
'c' - Converts the value into the corresponding unicode character
'd' - Decimal format
'e' - Scientific format, with a lower case e
'E' - Scientific format, with an upper case E
'f' - Fix point number format
'F' - Fix point number format, upper case
'g' - General format
'G' - General format (using a upper case E for scientific notations)
'o' - Octal format
'x' - Hex format, lower case
'X' - Hex format, upper case
'n' - Number format
'%' - Percentage format

'''

# formar 255 into a hexadecimal value
x = format(255, 'x')

# frozenset()	Returns a frozenset object
# freeze the list, and make it unchangeable
mylist = ["apple", "banana", "cherry"]
x = frozenset(mylist)

# more examples
# try to change the value of a frozenset item: this will cause an error
mylist = ["apple", "banana", "cherry"]
x = frozenset(mylist)
x[1] = "strawberry"

# getattr()	Returns the value of the specified attribute (property or method)
# get the value of the "age" property of the "Person" object
class Person:
    name = "John"
    age = 36
    country = "Norway"

x = getattr(Person, "age")

# syntax getattr(object, attribute, default)
'''
Parameter	Description
object	Required. An object.
attribute	The name of the attribute you want to get the value from
default	Optional. The value to return if the attribute does not exist
'''

# use the "default" parameter to write a message when the attribute does not exits

class Person:
    name = "John"
    age = 36
    country = "Norway"

x = getattr(Person, 'Page', 'my message')

# globals()	Returns the current global symbol table as a dictionary

# display the global symbol table:
x = globals()
print(x)

# get the filename of the current program
x = globals()
print(x["__file__"])

# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# check if the "person" object has the "age" property
class Person:
    name = "John"
    age = 36
    country = "Norway"

x = hasattr(Person, "age")

# syntax hasattr(object, attribute)

# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system

# hex()	Converts a number into a hexadecimal value
# convert 255 into hexadecimal value
x = hex(255)
# returned string always starts with the prefix 0x


# id()	Returns the id of an object
# return the unique id of a tuple object
x = ("apple", "banana", "cherry")
y = id(x)

# input()	Allowing user input
# ask for the user's name and print it:
print("Enter your name")
x = input()
print("Hello " + x)

# the input() function allows user input

# syntax input(prompt)

# eamples
x = input("Enter your name: ")
print("hello", + x)

# int()	Returns an integer number
x = int(3.5)

# isinstance()	Returns True if a specified object is an instance of a specified object
# check if the number 5 is an integer
x = ininstance(5, int)

# syntax isinstance(objectm type)

# examples
x = isinatance("Hello", (float, int, str, list, dict, tuple))

# check of y is an instance of myObj:
class myObj:
    name = "John"

y = myObj()

x = isinatance(y, myObj)

# issubclass()	Returns True if a specified class is a subclass of a specified object
class myAge:
    age = 36

class myObj(myAge):
    name = "John"
    age = myAge

x = issubclass(myObj, myAge)

# issubclass(object, subclass)

# iter()	Returns an iterator object
# create an iterator object, and print the items:
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# len()	Returns the length of an object
mylist = ["apple", "banana", "cherry"]
x = len(mylist)


# list()	Returns a list
x = list(("apple", "banana", "cherry"))

# locals()	Returns an updated dictionary of the current local symbol table
x = locats()
print(x)

# map()	Returns the specified iterator with the specified function applied to each item
def myfunc(n):
    return len(n)

x = map(myFunc, ("apple", "banana", "cherry"))

# syntax map(function, iterables)

# example
# make new fruits by sending two iterable objects into the function:
def myfunc(a, b):
    return a + b
x = map(myFunc, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple"))

# max()	Returns the largest item in an iterable
x = max(5, 10)

# syntax max(n1, n2, n3, ....)

# more examples
x = max("Mike", "John", "Vicky")

a = (1, 5, 3, 9)
x = max(a)

# memoryview()	Returns a memory view object
# create and prince a memoryview object
x = memoryView(b"Hello")
print(x)

# return the unicode of the first character
print(x[0])

# return the unicode of the second character
print(x[1])

# min()	Returns the smallest item in an iterable
x = min(5, 10)

# syntax min(n1, n2, n3)

# next()	Returns the next item in an iterable
# create an iterator, and print the items one by one
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

# example
# return a defult value when the iterable has reached to its end:
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)

# object()	Returns a new object
# create an empty object
x = object()

# oct()	Converts a number into an octal
x = oct(12)

# open()	Opens a file and returns a file object
f = open("demofile.txt", "r")
print(f.read())

'''
file	The path and name of the file
mode	A string, define which mode you want to open the file in:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''

# ord()	Convert an integer representing the Unicode of the specified character
x = ord("h")

# pow()	Returns the value of x to the power of y
x = pow(4, 3)

# example
# return the value of 4 to the power of 3, modulus 5 (game as (4 * 4 * 4) % 5):
x = pow(4, 3, 5)


# print()	Prints to the standard output device
print("Hello World")

# example
print("Hello", "How are you?")

x = ("apple", "banana", "cherry")
Print(x)

# print two messages, and specify the separator
print("Hello", "how are you?", sep=" ---")

# property()	Gets, sets, deletes a property

# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
x = range(6)
for n in x:
    print(x)
# syntax range(start, stop, step)
'''
Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Optional. An integer number specifying at which position to endt.
step	Optional. An integer number specifying the incrementation. Default is 1

'''

# example
x = range(3, 6)
for n in x:
    print(n)

x = range(3, 20, 2)
for n in x:
    print(n)

# repr()	Returns a readable version of an object

# reversed()	Returns a reversed iterator
alpha = ["a", "b", "c", "d"]
ralph = reversed(alpha)

for x in ralph:
    print(x)

# round()	Rounds a numbers
x = round(5.76543, 2)
print(x)


# set()	Returns a new set object
x = set(("apple", "banana", "cherry"))

# setattr()	Sets an attribute (property/method) of an object
# change the value of the "age" property of the "person" object

class Person:
    name = "John"
    age = 36
    country = "Norway"

setattr(Person, "age", 40)

# syntax setaatr(object, attribute, value)

'''

Parameter	Description
object	Required. An object.
attribute	Required. The name of the attribute you want to set
value	Required. The value you want to give the specified attribute
'''

# slice()	Returns a slice object
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

# syntax slice(start, end, step)

'''
Parameter	Description
start	Optional. An integer number specifying at which position to start the slicing. Default is 0
end	An integer number specifying at which position to end the slicing
step	Optional. An integer number specifying the step of the slicing. Default is 1
'''

# example
# create a tuple and a slice object. Start the slice object at position 3m and slice to position 5, and return the result:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

# create a tuple and a slice object. use the step parameter to return every thrid item:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

# sorted()	Returns a sorted list
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = sorted(a)
print(x)

# synatx sorted(iterable, key=key, reverse=reverse)
'''
iterable	Required. The sequence to sort, list, dictionary, tuple etc.
key	Optional. A Function to execute to decide the order. Default is None
reverse	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
'''

# example
# sort numeric
a = (1, 11, 2)
x = sorted(a)
print(x)

# sort ascending
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = sorted(a, reverse=True)
print(x)

# @staticmethod()	Converts a method into a static method

# str()	Returns a string object
x = str(3.5)

# syntax str(object, enconding=enconding, errors=erros)

# example
x = int("12")

# sum()	Sums the items of an iterator
a = (1, 2, 3, 4, 5)
x = sum(a)

# synatx sum(iteratble, start)

# example
a = (1, 2, 3, 4, 5)
x = sum(a, 7)

# tuple()	Returns a tuple
x = tuple(("apple", "banana", "cherry"))

# type()	Returns the type of an object
# return the type of these objects:

a = ("apple", "banana", "cherry")
b = "Hello world"
c = 33

x = type(a)
y = type(b)
z = type(c)

'''
Parameter	Description
object	Required. If only one parameter is specified, the type() function returns the type of this object
bases	Optional. Specifies the base classes
dict	Optional. Specifies the namespace with the definition for the class
'''

# vars()	Returns the __dict__ property of an object
class Person:
    name = "John"
    age = 36
    country = "norway"
x = vars(Person)

# zip()	Returns an iterator, from two or more iterators
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

# syntax zip(iterator1, iterqator2, iterator3 ...)

# example
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)



# STRING METHODS

# capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world!"
x = txt.capitalize()
print(x)


# casefold()	Converts string into lower case
txt = "hello, and welcome to my world!"
x = txt.casefold()
print(x)

# center()	Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)

# syntax string.center(length, character)
txt = "banana"
x = txt.center(20, "O")
print(x)

# count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# syntax string.count(value, start, end)

# examples
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# encode()	Returns an encoded version of the string
txt = "My name is ståle"
x = txt.encode()
print()

# syntax string.encode(enconding=encoding, errors=erros)

'''
Parameter	Description
encoding	Optional. A String specifying the encoding to use. Default is UTF-8
errors	Optional. A String specifying the error method. Legal values are:
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
'''

# examples
txt = "My name is ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace")
print(txt.encode(encoding="ascii",errors="ignore")
print(txt.encode(encoding="ascii",errors="namereplace")
print(txt.encode(encoding="ascii",errors="replace")
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace")
print(txt.encode(encoding="ascii",errors="strict")

# endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# syntax string.endswith(value, start, end)

# examples
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# check if position 5 to 11 ends with the phrase "my world."
txt = "Hello, welcome to my world."
x = txt.endswith("my world", 5,11)
print(x)

# expandtabs()	Sets the tab size of the string
txt = "H\te\t1\t1\to"
x = txt.expandtabs(2)
print(x)

# example
txt = "H\te\t1\t1\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# string.find(value, start, end)

# example
txt = "hello, welcome to my world"
x = txt.find("e")
print(x)

# where is the txt is the first occurence of the letter "e" when you only search between position 5 and 10?:
txt = "hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# if the value is not found, the find() method returns -1 but the index() method will raise an exception
txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

# format()	Formats specified values in a string
# format_map()	Formats specified values in a string

# index()	Searches the string for a specified value and returns the position of where it was found
# where in the text the word "welcome"
txt = "hello, welcome to my world."
x = txt.index("welcome")
print(x)

'''
Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string
'''

# examples
# where in the txt is the first occurrence of the letter "e"?
txt = "hello, welcome to my world."
x = txt.index("e")
print(x)

# where in the txt is the first occurrence of the letter "e" when you only search between possible 5 and 10?
txt = "hello, welcome to my world."
x = text.index("3", 5, 10)

# if the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

# isalnum()	Returns True if all characters in the string are alphanumeric
# check if all the character in the text are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

'''
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc.
'''

# example
txt = "Company 12"
x = txt.isalnum()
print(x)

# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

'''
The isalpha() method returns True if all the characters are alphabet letters (a-z).

Example of characters that are not alphabet letters: (space)!#%&? etc.
'''

# example
txt = "Company10"
x = txt.isalpha()
print(x)

# isdecimal()	Returns True if all characters in the string are decimals
txt = "\u0033" # unicode for 3
x = txt.isdecimal()
print(x)

# example
a = "\u0030" # unicode for 0
b = "\u0047" # inicode for G

print(a.isdecimal())
print(b.isdecimal())

# isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)

# isidentifier()	Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)

# islower()	Returns True if all characters in the string are lower case
# check if all the characters in the text are in lower case:
txt = "hello world!"
x = txt.islower()

# syntax string.islower()

# examples
a = "hello world!"
b = "hello 123"
c = "mynameisKing"

print(a.islower())
print(b.islower())
print(c.islower())

# isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())

# isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# isspace()	Returns True if all characters in the string are whitespaces
txt = "  "
x = txt.isspace()
print(x)

# example
txt = "    s   "
x = txt.isspace()
print(x)

# istitle()	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

# example
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello",
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

# isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!!"
x = txt.isupper()
print(x)

# example
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS KING"

print(a.isupper())
print(b.isupper())
print(c.isupper())


# join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
X = "#".join(myTuple)
print(x)

# syntax string.join(iterable)

# example
myDict = {"name":"john", "country":"Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# ljust()	Returns a left justified version of the string
txt = "banana"
x = txt.Ijust(20)
print(x, "is my favorite fruit")

# string.Ijust(length, character)

# example
txt = "banana"
x = txt.Ijust(20, "O")
print(x)

# lower()	Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# syntax string.lower()

# lstrip()	Returns a left trim version of the string
txt = "      banana          "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# syntax = string.lstrip(characters)
#more example
txt = ",,,,,,ssaaw.....banana"
x = txt.lstrip(",.asw")
print(x)

# maketrans()	Returns a translation table to be used in translations

# partition()	Returns a tuple where the string is parted into three parts
# search for the word "banana" and return a tuple with three elements: 1. everything before the match, 2. the match 3, everything after the "match"

txt = "I could eat banana all day"
x = txt.partition("banana")
print(x)

# syntax string.partition(value)

# example
txt = "I could eat banana all day"
x = txt.partition("apples")
print(x)


# replace()	Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# syntax string.replace(oldvalue, newvalue, count)

# examples
txt = "one one as a race horse, two two was one too"
x = txt.replace("one", "three")
print(x)

txt = "one one as a race horse, two two was one too"
x = txt.replace("one", "three", 2)
print(x)

# rfind()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

# syntax string.rfind(value, start, end)

# examples
# where in the text is the last occurence of the letter "e"
txt = "Hello, welcome to my world"
x = txt.rfind("e")
print(x)

# where in the text is the last occurence of the letter "e" when you only search between position 5 and 10?
txt = "Hello, welcome to my world"
x = txt.rfind("e", 5, 10)
print(x)

# if the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception
txt = "hello, welcome to my world"
print(txt.rfind("q"))
print(txt.rindex("q"))


# rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa. "
x = txt.rindex("casa")
print(x)

# rpartition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, bananas, cherry"
x = txt.rsplit(", ")
print(x)

# syntax string.rsplit(separator, max)

# examples
txt = "apple, bananas, cherry"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)



# rstrip()	Returns a right trim version of the string
txt = "      bananas       "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)

# synatx string.split(separator, max)

# examples
# split the string, using comma, followed by a space, as a separtor
txt = "hello, my name is KING, I am 31 years old"
x = txt.split(", ")
print(x)


# split the string, using comma, followed by a space, as a separator
txt = "hello, my name is King, I am 31 year old"
x = txt.split(", ")
print(x)

# use a hash tag as a separator
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# split the string into a list with max 2 items
txt = "apple#banana#cherry#orange"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

# splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# example
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

# startswith()	Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# syntax string.startswith(value, start, end)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name is King"
x = txt.swapcase()
print(x)

# title()	Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)

# translate()	Returns a translated string

# upper()	Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)

# zfill()	Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)
print(x)

# syntax string.zfill(len)

# fill the strings with zeros until they are 10 characters long
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))


# PYTHON LIST/ARRAY METHODS

# append()	Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# synatax list.append(elmnt)

# examples
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)


# clear()	Removes all the elements from the list
fruits = ["apple", "banana", "cherry", "orange"]
fruits.clear()

# copy()	Returns a copy of the list
fruits = ["apple", "banana", "cherry", "orange"]
x = fruits.copy()

# count()	Returns the number of elements with the specified value
fruits = ["apple", "banana", "cherry", "orange"]
x = fruits.count("cherry")

# syntax list.count(values)

# examples
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

# extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]

fruits.extend(cars)

# syntax list.extend(iterable)

# examples
fruits = ["apple", "banana", "cherry"]
points = (1, 4, 5, 9)
fruits.extend(points)

# index()	Returns the index of the first element with the specified value
fruits = ["apple", "banana", "cherry"]
x = fruits.index("cherry")

# syntax list.index(elmnt)

# examples
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)

# note the index() method only return the first occurence of the value

# insert()	Adds an element at the specified position
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")

# syntax list.insert(pos, element)

# pop()	Removes the element at the specified position
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)

# syntax list.pop(pos)

# examples
fruits = ["apple", "banana", "cherry"]
x = fruits.pop(1)
# note: The pop() method returns removed value

# remove()	Removes the first item with the specified value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# reverse()	Reverses the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reversed()

# sort()	Sorts the list
# sort the list alphabetically:
cars = ["Ford", "BMW", "Volvo"]
cars.sort()

# syntax list.sort(reverse=True|False, key=myFunc)

# sort the list descending
cars = ["Ford", "BMW", "Volvo"]
cars.sort(reverse=True)

# sort the list bu the length of the values
# a function that returns the length of the values

def myFunc(e):
    return len(e)

cars = ["Ford", "Mitsubishi", "BMW", "VW"]

cars.sort(key=myFunc)

# sort the list by the length of the values and reversed:
# a function that returns the length of the values

def myFunc(e):
    return len(e)

cars = ["Ford", "Mitsubishi", "BMW", "VW"]

cars.sort(reverse=True, key=myFunc)



# PYTHON DICTIONARY METHODS
# clear()	Removes all the elements from the dictionary
# remove all elements from the car list:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()
print(car)

# syntax dictionary.clear()

# copy()	Returns a copy of the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.copy()
print(x)

# syntax dictionary.copy()

# fromkeys()	Returns a dictionary with the specified keys and values
x = ("key1", "key2", "key3")
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# syntax dict.fromkeys(keysm values)

# examples
x = ("key1", "key2", "key3")
thisdict = dict.fromkeys(x)
print(thisdict)


# get()	Returns the value of the specified key
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = cars.get("model")
print(x)

# syntax dictionary.get(keyname, values)

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.get("prince", 15000)
print(x)

# items()	Returns a list containing the a tuple for each key value pair
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)

# syntax dictionary.items()

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

car["year"] = 2018
print(x)

# keys()	Returns a list containing the dictionary's keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

# syntax dictionary.keys()

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
car["color"] = "white"
print(x)

# pop()	Removes the element with the specified key
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop("model")
print(car)

# syntax dictionary.pop(keyname, defaultvalue)

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.pop("model")
print(x)


# popitem()	Removes the last inserted key-value pair
# remove the last item from the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.popitem()
print(car)

# syntax dictionary.popitem(keyname, defaultvalue)

# the removed item is the return value of the pop method
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.popitem()
print(x)

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

# syntax dictionary.setdefault(keyname, value)

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("color", "white")
print(x)

# update()	Updates the dictionary with the specified key-value pairs
# insert an item to the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car,update({"color":"white"})
print(x)

# syntax  dictionary.update(iterable)
# return the values
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)

# syntax dictionary.values()

# examples
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
car["year"] = 2018
print(x)



# PYTHON TUPLE METHOD
# count()	Returns the number of times a specified value occurs in a tuple
thistuple = (1, 3, 7, 8, 7, 5,4, 6, 8, 5)
x = thistuple.count()
print(x)

# syntax tuple.count(values)

# index()	Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5,4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# syntax tuple.index(value)

# PYTHON SET METHODS
# add()	Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# syntax set.add(elmnt)

# examples
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

# clear()	Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# syntax set.clear()

# copy()	Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# difference()	Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(x)

# syntax set.difference(set)

# examples
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)
print(z)


# difference_update()	Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)

# discard()	Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# intersection()	Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)


# synatax set.intersection(set1, set2...etc.)
'''
Parameter	Description
set1	Required. The set to search for equal items in
set2	Optional. The other set to search for equal items in.
You can compare as many sets you like.
Separate the sets with a comma
'''

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
print(result)

# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# synatax set.intersection(set1, set2...etc.)
'''
Parameter	Description
set1	Required. The set to search for equal items in
set2	Optional. The other set to search for equal items in.
You can compare as many sets you like.
Separate the sets with a comma
'''

# examples
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)
print(x)

# isdisjoint()	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)
print(z)

# syntax set.isdisjoint(set)

# example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)
print(z)


# isdisjoint()	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# syntax set.isdisjoint(set)

# example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


# issubset()	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)

# syntax issubset(set)

# example
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

# issuperset()	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)

# set.issuperset(set)

# examples
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

# pop()	Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# syntax set.pop()

# examples
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# note: the pop() method returns removed value

# remove()	Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# syntax set.remove(item)

# symmetric_difference()	Returns a set with the symmetric differences of two sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.sysmmetric_difference(y)
print(z)

# syntax set.sysmmetric_difference(set)

# symmetric_difference_update()	inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
x.sysmmetric_difference_update(y)

# syntax set.sysmmetric_difference_update(set)

# union()	Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.union(y)
print(z)

# syntax set.union(set1,set2)

# example
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)

# update()	Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

x.update(y)
print(x)

# syntax set.update(set)


# PYTHON KEYWORDS METHODS
# and	A logical operator
x = (5 > 3 and 5 < 10)
print(x)

# examples
# using the and keyword in an if statement
if 5 > 3 and 5 < 10:
    print("Both statement are True")
else:
    print("At least one of the statements are False")

# as	To create an alias
import calender as c
print(c.month_name[1])

# assert	For debugging
x = "hello"

# if condition returns True, then nothing happens
assert x == "hello"

# if condition returns False, AssertionError is raised
assert x == "goodbye"

# more examples
x = "hello"
assert x == "goodbye", "x should be 'hello'"

# break	To break out of a loop
for i in range(9):
    if i > 3:
        break
        print(i)

# examples
i = 1
while i < 9:
    print(i)
    if i == 3:
        break
    i += 1


# class	To define a class
class Person:
    name = "King"
    age = 31

# examples
# create an object named p1, using the class from the example above
p1 = Person()
print(p1.name)

# continue	To continue to the next iteration of a loop
for i in range(9):
    if == 3:
        continue
    print(i)


# example
i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)

# def	To define a function
def my_function():
    print("Hello from a fuctions")
my_function()


# del	To delete an object
# delete an object
class MyClass:
    name = "King"

del myClass
print("myClass")

# delete a variable
x = "hello"
del x
print(x)

# delete the first item in a list
x = ["apple", "bananan", "cherry"]
del x[0]
print(x)

# elif	Used in conditional statements, same as else if
for i in range(-5, 5):
    if i > 0:
        print("YES")
    elif i == 0:
        print("WHATEVER")
    else:
        print("NO")

# else	Used in conditional statements
x = 2
if x > 3:
    print("YES")
else:
    print("NO")

# use the else keyword in a try...except block to define what to do if no error were raised
x = 5

try:
    x > 10
except:
    print("Something went wrong")
else:
    print("the 'try' code was executed without raising any errors!")

# except	Used with exceptions, what to do when an exception occurs
try:
    x > 3
except:
    print("Something went wrong")


# write one message if it is a NameError, and another if it is an TypeError
x = "Hello"

try:
    x > 3
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")

# Try to execute a statement that raises an error, but none of the defined error types(in this case a zeroDivisionError)
try:
    x = 1/0
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
        print("You are comparing values of different type")
except:
    print("Something else wnet wrong")

# write a message of no error were raised
x = 1
try:
    x > 10
except NameError:
        print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
else:
    print("The 'Try' code was executed without raising any erros!")

# False	Boolean value, result of comparison operations
print(5 > 6)

# more examples
print(5 > 6)
print(4 in [1,2,3])
print("Hello" is "goodbye")
print(5 == 6)
print(5 == 6 or 6 == 7)
print(5 == 6 and 6 == 7)
print("hello" is not "hello")
print(not(5 == 5))
print(3 not in [1,2,3])

# finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
try:
    x > 3
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The try...except block is finished")

# for	To create a for loop
for x in range(1, 9):
    print(x)

# examples
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# from	To import specific parts of a module
from datatime import time
x = time(hour=15)
print(x)

# global	To declare a global varriable
# declare a global variable inside a function, and use it outside the function
# create a function
def myfunction():
    global x
    x = "hello"

# execute the function:
myfunction()

# x should now be global, and accessible in the global scope.
print(x)

# if	To make a conditional statement
x = 5
if x > 3:
    print("YES")

# examples
x = 5
if x > 6:
    print("YES")
else:
    print("NO")


# import	To import a module
import datetime
x = datetime.datetime.now()
print(x)

# in	To check if a value is present in a list, tuple, etc.
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("yes")


# examples
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

# is	To test if two variables are equal
x = ["apple", "banana", "cherry"]
y = x
print(x is y)

# examples
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y )

# lambda	To create an anonymous function
# create a function that adds 10 to any number you send
x = lambda a : a + 10
print(x(5))

# a lambda fuction with three arguments:
x = lambda a, b, c : 1 + b + c
print(x(5, 6, 2))

# None	Represents a null value
x = None
print(x)

# example
x = None
if x:
    print("Do you think None is True")
else:
    print("None is not True...")

# nonlocal	To declare a non-local variable
# make a function inside a function, which uses the variable x as a non local variable:

def myfunc1():
    x = "King"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())

# some example as above, but without the nonlocal keyword
def myfunc1():
    x = "King"
    def myfunc2():
        x = "hello"
    myfunc2()
    return x

print(myfunc1())

# not	A logical operator
x = False
print(not x)

# or	A logical operator
x = (5 > 3 or 5 > 10)
print(x)

# using the or keyword in an if statement:
if 5 > 3 or 5 > 10:
    print("At least one of the statement are True")
else:
    print("None of the statement are True")

# pass	A null statement, a statement that will do nothing
# create a placeholder for future code
def myfunction:
    pass

# examples
class Person:
    pass

# raise	To raise an exception
x = -1

if x < 0:
raise Exception("Sorry, no numbers below zero")

# example
# raise a typeerror if x is not an integer
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# return	To exit a function and return a value
def myfunction():
    return 3+3
print(myfunction())

# example
def myfunction():
    return 3+3
    print("Hello, World!")

print(myfunction())

# True	Boolean value, result of comparison operations
print(7 > 6)

# more example
print(5 < 6)
print(2 in [1,2,3])
print(5 is 5)
print(5 == 5)
print(5 == 5 or 6 == 7)
print(5 == 5 and 7 == 7)
print("hello" is not "goodbye")
print(not(5 == 7))
print(4 not in [1,2,3])

# try	To make a try...except statement
try:
    x > 3
except:
    print("Something went wrong")

# example
try:
    x > 3
except:
    Exception("Something went wrong")

# while	To create a while loop
x = 0
while x < 9:
    print(x)
    x = x + 1
# with	Used to simplify exception handling
# yield	To end a function, returns a generator






# PYTHON HOW TO
# How to Remove Duplicates From a Python List
# remove any duplicate from a list
# A List with Duplicates
mylist = ["a", "b", "a", "c", "c"]
# Create a Dictionary
# Convert Into a List
mylist = list(dict.fromkeys(mylist))
# Print the List
print(mylist)


# Create a Function
# Create a function that takes a List as an argument.
def my_function(x):
    # Create a dictionary, using this List items as keys.
    # Return List
    return list(dict.fromkeys(x))
    # Convert Into a List
    # Call the Function
mylist = my_function(["a", "b", "a", "c", "c"])

# Print the Result
print(mylist)


# How to Reverse a String in Python
# The fastest (and easiest?) way is to use a slice that steps backwards, -1.

txt = "Hello World"[::-1]
print(txt)

'''
Create a slice that starts at the end of the string, and moves backwards.

The slice statement [::-1] is the same as [11:0:-1] which means start at position 11
(because "Hello "World" has 11 characters), end at position 0, move with the step -1,
negative one, which means one step backwards.

'''

# Create a Function
def my_function(x):
    # Slice the String
    # Return the String
    return x[::-1]
# Call the Function
mytxt = my_function("I wonder how this text looks like backwards")
# Print the Result
print(mytxt)
