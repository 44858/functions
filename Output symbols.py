#Lewis Travers
#25/11/2014
#Output symbols

def input_symbols():
    integer = int(input("Please enter a number: "))
    character = input("Please enter a character: ")
    return integer, character

def output_symbols(integer, character):
    for count in range(integer):
        print(character)

#main program

integer, character = input_symbols()
message = output_symbols(integer, character)
print(message)
