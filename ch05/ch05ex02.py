# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.


count = 0

while True:
    str_val = input("Enter a number:")
    if str_val == 'done':
        break
    try:
        val = float(str_val)
    except:
        print("Invalid input")
        continue

    if count == 0:
        min_val = val
        max_val = val
    elif val < min_val:
        min_val = val
    elif val > max_val:
        max_val = val

    count = count + 1


print(min_val, max_val)
