# Exercise 1: Write a simple program to simulate the operation of the grep com-
# mand on Unix. Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$
import re

filename = input("Enter the filename: ")
regex = input("Enter a regular expression: ")

counter = 0
fhand = open(filename, 'r')
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        counter += 1

print(counter)