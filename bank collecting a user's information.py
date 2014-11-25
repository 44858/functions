#Lewis Travers
#21/11/2014
#bank collecting a user's information

def user_details():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    gender = input("Please enter your gender: ")
    house_number = int(input("Please enter your house number: "))
    street_name = input("Please enter your street name: ")
    town = input("Please enter the name of your town: ")
    post_code = input("Please enter your postal code: ")
    if gender == "female":
        title = "Ms."
    else:
        title = "Mr."
    return first_name, last_name, title

def display_message(first_name, last_name, title):
    print("Welcome {0} {1} {2}.".format(title, first_name, last_name))


#main program

first_name, last_name, title = user_details()
message = display_message(first_name, last_name, title)
print(message)
