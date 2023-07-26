def Decorator(func1):
    def Wrapper():
        print("Do Something Before It")
        func1()
        print("Do Something After It")
    return Wrapper

@Decorator
def func1():
   print("Original Function")

func1()