#Lewis Travers
#14/11/2014
#Calculating pay

hours = int(input("Please enter the amount of hours worked: "))

payrate = int(input("Please enter the pay rate per hour: "))

pay = hours * payrate

overtime = int(input("How many hours did you work overtime?: "))

overtime_pay = overtime * payrate

total_pay = overtime_pay + pay

print("Your total pay is £{0}.".format(total_pay))
