numbers=[1,2,3,4,5,6,7,8,9,10]
#Method1
for number in numbers:
    print(number*number)
#Method2
def square(x):
    return x*x
square=list(map(square,numbers))
print(square)
square=list(map(lambda x:x*x,numbers))
print(square)
#Method3


#Convert Celsius to Farenhite and Farenhite to Celsius

CelsiusTemperatures=[0, 10, 20, 30, 40]
#Fahrenheit Temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]
def Convert_to_Farenhite(C):
    F=(9/5)*C+32
    return F


farenhite=list(map(Convert_to_Farenhite,CelsiusTemperatures))
print(farenhite)
farenhite=list(map(lambda x:9/5*x+32,CelsiusTemperatures))
print(farenhite)

