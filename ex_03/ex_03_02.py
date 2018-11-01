try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    overtime_hours = hours - 40.0
    extra_pay = overtime_hours * (rate * 0.5)
    total_pay = (hours * rate) + extra_pay
    print("Pay: " % total_pay)
else:
    print("Pay: " % hours * rate)
