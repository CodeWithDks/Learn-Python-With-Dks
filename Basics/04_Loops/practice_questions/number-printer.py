# Print numbers from 1 to 10 using a loop.

# Using a for loop
for i in range(1,11):
    print(i)

# Using a while loop
count = 1
while count <= 10:
    print(count)
    count += 1

# print even numbers from 1 to 20 using a loop.

# Using a for loop
for i in range(1,21):
    if i%2==0:
        print(i)

# Using a while loop
count = 1
while count <=20:
    if count%2==0:
        print(count)
    count += 1


# Print the multiplication table of using user input.

# Using a for loop
number = int(input("Enter a number to print its multiplication table:"))
print(f"Multiplication table of {number}:")
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")


# Using a while loop
number = int(input("Enter a number to print its multiplication table:"))
print(f"Multiplication table of {number}:")
count = 1
while count <=10:
    print(f"{number} x {count} = {number*count}")
    count += 1  



