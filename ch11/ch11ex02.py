# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259
import re

filename = input("Enter file: ")
fhand = open(filename, 'r')

nums = []

for line in fhand:
    match = re.search("New\sRevision:\s(\d+)", line)
    if match:
        nums.append(int(match.group(1)))

print(sum(nums)/len(nums))