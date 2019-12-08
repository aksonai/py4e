# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    if hours > 40:
        pay = (hours - 40)*rate*1.5 + 40 * rate
    else:
        pay = hours * rate
    return pay

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = computepay(hours, rate)
print("Pay: ", pay)