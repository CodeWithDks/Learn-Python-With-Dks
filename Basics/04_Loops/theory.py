# Loops in python.
# Loops are used to execute a block of code repeatedly until a certain condition is met. In Python, there are two main types of loops: for loops and while loops.

# 1. For Loop: A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

# Example of For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) #This code will print each fruit in the list one by one.

# 2. While Loop: A while loop is used to execute a block of code as long as a specified condition is true.

# Example of While Loop
count = 0
while count < 5:
    print(count) #This code will print the value of count as long as it is less than 5.
    count += 1 #This line increments the value of count by 1 in each iteration, which eventually makes the condition (count < 5) false and stops the loop. 



# 3. Break and Continue: These are control statements that can be used inside loops to alter their behavior.

# Example of Break and Continue
for i in range(10):
    if i == 5:
        break #The break statement will exit the loop when i is equal to 5, so the loop will stop executing after printing numbers from 0 to 4.
    print(i)


for i in range(10):
    if i % 2 == 0:
        continue #The continue statement will skip the current iteration of the loop when i is an even number, so it will only print odd numbers from 1 to 9.
    print(i)

# Pass Statement: The pass statement is a placeholder that does nothing. It is used when you need to have a block of code but don't want to execute anything in it.

# Example of Pass Statement
for i in range(5):
    if i == 2:
        pass #The pass statement does nothing when i is equal to 2, so the loop will continue executing and print all numbers from 0 to 4 without any interruption.
    print(i)

# Nested Loops: You can also have loops inside other loops, which are called nested loops. This allows you to iterate over multiple sequences or perform more complex iterations.

# Example of Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}") #This code will print the values of i and j for each combination of i and j, resulting in a total of 6 iterations (i=0 with j=0 and j=1, i=1 with j=0 and j=1, i=2 with j=0 and j=1).

# Nested loops using while loop
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}") #This code will produce the same output as the previous example, but it uses while loops instead of for loops to achieve the same result.
        j += 1
    i += 1

