def computepay(hours, rate):

    if hours > 40:
        overtime_hours = hours - 40.0
        extra_pay = overtime_hours * (rate * 0.5)
        total_pay = (hours * rate) + extra_pay
    else:
        total_pay = hours * rate

    return total_pay

if __name__ == "__main__":
    try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        pay = computepay(hours, rate)
        print("Pay:", pay)
    except:
        print("Error, please enter numeric input")
        quit()