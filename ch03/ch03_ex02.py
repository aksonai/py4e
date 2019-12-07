# Exercise 2: Rewrite your pay program using try and except so that your pro-
# gram handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input!")
    quit()

if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40 * rate
else:
    pay = hours * rate

print("Pay: ", pay)