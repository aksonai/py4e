# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score
# >= 0.9
# >= 0.8
# >= 0.7
# >= 0.6
# < 0.6
# ~~~
# Grade
# A
# B
# C
# D
# F
# Enter score: 0.95 A ~ ~
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.
try:
    grade = float(input("Enter score: "))
except:
    print("Bad score")
    quit()

if grade < 0 or grade > 1.0:
    print("Score is out of range!")
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")