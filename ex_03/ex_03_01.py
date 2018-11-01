hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    overtime_hours = hours - 40.0
    extra_pay = overtime_hours * (rate * 0.5)
    total_pay = (hours * rate) + extra_pay
    print(total_pay)
else:
    print(hours * rate)
