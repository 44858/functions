#Lewis Travers
#28/11/2014
#sort function

def get_numbers():
    x = int(input("Please enter a number for x: "))
    y = int(input("Please enter a number for y: "))
    return x, y

def sort_function(x, y):
    if x > y:
        return y, x
    else:
        return x, y

def print_numbers(x, y):
    if x > y:
        print("{0}, {1}.".format(y, x))
    else:
        print("{0}, {1}.".format(x, y))

# main program

x, y = get_numbers()
x, y = sort_function(x, y)
x, y = print_numbers(x, y)
print(x, y)
