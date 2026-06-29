# Problem 1 🟢

# Ask the user to enter a number. Print whether it is positive, negative, or zero.
try:
    num = int(input('Enter the number: '))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input. Please enter a whole number.")

# Problem 2 🟡

"""Ask the user to enter their score (0–100). Print their grade:

90–100 → A
70–89 → B
50–69 → C
Below 50 → F

Also print "Invalid score" if they enter something outside 0–100."""

try:
    score = int(input("Enter your score: "))
    
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Grade A")
    elif score >= 70:
        print("Grade B")
    elif score >= 50:
        print("Grade C")
    else:
        print("Grade F")
        
except ValueError:
    print("Invalid score. Please enter a whole number.")