# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.

def computegrade(grade):
    if grade < 0 or grade > 1.0:
        return "Score is out of range!"
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    else:
        return "F"


try:
    grade = float(input("Enter score: "))
except:
    print("Bad score")
    quit()

print(computegrade(grade))