#Lewis Travers
#18/11/2014
#calculating pay

def calculate_basic_pay (hours,pay):
    total = hours * pay
    return total

def calculate_overtime_pay (hours,pay):
    overtime_pay = (hours - 40) * (pay * 1.5)
    basic_pay = 40 * pay
    total = overtime_pay + basic_pay
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("Please enter the amount of hours worked this week: "))
    pay = float(input("Please enter your hourly pay rate in £: "))
    return hours,pay

def display_total_pay(total):
    total_pay = round(total_pay,2)
    print("Your total pay for this week is £{0}.".format(total))


def calculate_pay():
    hours, pay = work_details
    
    
    
#main program

    
