# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40 * rate
else:
    pay = hours * rate

print("Pay: ", pay)