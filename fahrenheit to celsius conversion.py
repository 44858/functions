#Lewis Travers
#02/12/2014
#Fahrenheit to celsius conversion

def temp_input():
    fahrenheit = int(input("Please enter a temperature in degrees Fahrenheit: "))
    return fahrenheit

def conversion(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

def display_celsius(celsius):
    print("The temperature in degrees Celsius is {0}".format(celsius))

#main program

print("Fahrenheit to Celsius converter")
print("")
fahrenheit = temp_input()
celsius = conversion(fahrenheit)
celsius = display_celsius(celsius)
print(celsius)
