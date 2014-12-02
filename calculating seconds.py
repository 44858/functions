#Lewis Travers
#02/12/2014
#Calculating seconds from given hours, minutes and seconds

def details():
    hours = int(input("Please enter a number of hours: "))
    minutes = int(input("Please enter a number of minutes: "))
    seconds = int(input("Please enter a number of seconds: "))
    return hours, minutes, seconds

def convert_to_seconds(hours, minutes, seconds):
    hours = convert_hours(hours)
    minutes = convert_minutes(minutes)
    total_seconds = hours + minutes + seconds
    return total_seconds

def convert_hours(hours):
    hours = hours * 3600
    return hours

def convert_minutes(minutes):
   minutes = minutes * 60
   return minutes

def display_seconds(total_seconds):
    print("The totsl number of seconds is {0}.".format(total_seconds))


#main program

hours, minutes, seconds = details()
hours = convert_hours(hours)
minutes = convert_minutes(minutes)
total_seconds = convert_to_seconds
