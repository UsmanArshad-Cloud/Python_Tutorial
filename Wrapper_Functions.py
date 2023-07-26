from functools import wraps
def decorator(func1):
    @wraps(func1)
    def wrapper():
        print("Doing Something Before")
        func1()
        print("Doing Something After")
    return wrapper
@decorator
def func1():
    print("Original Function")
func1()
print(func1.__name__)  # Output: wrapper =>If @Wraps is not used
print(func1.__doc__)   # Output: This is the wrapper function.