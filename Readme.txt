How code gets executed:
 //line by line from the top
Variables:
temporarily store data
can be integers,double,boolean and strings

Typecasting:
Convert one type to another
    str_val = "hello"
    list_val = list(str_val)
    tuple_val = tuple(str_val)
    set_val = set(str_val)
    print(list_val)  # Output: ['h', 'e', 'l', 'l', 'o']
    print(tuple_val)  # Output: ('h', 'e', 'l', 'l', 'o')
    print(set_val)  # Output: {'h', 'e', 'l', 'o'}
String Indexing 
str a="helllo"
a[0]=h
a[-1]=o
String Methods:
len->to calculate length of string
upper&lower
course.find('p')->to find the index of p.This func is case sensitive
course.replace("Hell","Hy")
print('u' in NAME)->return bool

Operator Precedence:
Paranthesis
Exponention
Multiplication or Division
Addition or Subtraction

2+10*4**2=162

abs and round,ceil and floor methods


For Loops:
for num in range(1, 5):
    print(num)

student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, score in student_scores.items():
    print(f"{name}: {score}")


Lists:
Lists are ordered, mutable, and can contain elements of different data types, including numbers, strings, other lists, and more

Lists functions:
->Append
->Insert(value,pos)
->Remove
->RemoveAt
->Pop
->Index

list.sort()
list.reverse()


Tuples
same as list but are immutable
x,y,z=(1,2,3)

Dictionary->for storing key values pair 

Functions:
Keywords Arguments vs Positional Arguments
These are the keyword arguments:
def subtract(a, b):
    return a - b

result = subtract(b=5, a=3)
print(result)  # Output: -2


Keywords arguments must always be used after positional arguments

Functions
Classes
Inheritance 
Modules
Packages

Random
random.random()
random.randint()
random.choice(list)

Lambda Function:

A lambda function in Python is a small, anonymous function that can have any number of arguments but can only have one expression. It is also known as an inline function or a function without a name.

lambda x:x*x

Filter:
filter(func,iteratable)

map:(apply a function to all the members of the list)
map(func,iteratable)

reduce:
reduce(func,iteratable)

It applies the function to the first two elements of the iterable.
The result of the first operation is combined with the next element in the iterable using the same function.
This process is repeated until all elements in the iterable are processed, and a single value is obtained as the result.

Decorator FUnciton is the function that takes another function as an input and extend the behavior of that  function without changing its code 

def Decorator(func1):
    def Wrapper():
       Print("Do Something Before It)
       func1
       Print("Do Something After It)
    return Wrapper

@Decorator
def func1():
   print("Original Function")

func1()

Partial Functions:
Partial functions in Python are created using the functools.partial() function, which allows you to fix certain arguments of a function and generate a new function with the remaining arguments. This is particularly useful when you want to create specialized versions of a function with some arguments pre-set, reducing the need for repetitive code.

from functools import partial

# Original function
def power(base, exponent):
    return base ** exponent

# Create a partial function with the base fixed to 2
square = partial(power, 2)

# Use the partial function
result = square(3)  # Equivalent to power(2, 3)
print(result)  # Output: 8


Wraps Function:
The wraps decorator from the functools module is used to create a decorator that properly updates the metadata (such as the function name, docstring, and module name) of the decorated function to retain the original function's attributes. It is especially useful when creating decorators that modify or extend the behavior of functions, as it preserves the essential information about the original function.

When you create a decorator without using wraps, the metadata of the decorated function gets replaced by the metadata of the decorator function. This can lead to confusion and issues when debugging or using introspection on the decorated function. The wraps decorator helps to avoid these problems by maintaining the original function's information.