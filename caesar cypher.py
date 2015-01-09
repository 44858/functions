#Lewis Travers
#05/01/2015
#Caesar Cypher

alphabet = ['a','b','c','d','e','f','g',
            'h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u',
  'v','w','x','y','z']

def details():
    shift_value = int(input("Please enter a shift value: "))
    message = input("Please enter the message that you would like encrypted: ")
    return shift_value, message

def encryption(shift_value, message):
    for letter in message:
        if letter in alphabet:
           old_index = alphabet.index(letter)
           new_index = (old_index + shift_value) % len(alphabet)
           new_message = alphabet[new_index]
    else:
        new_message = message
    return new_message


shift_value, message = details()
message = encryption(shift_value, message)
print(message)
