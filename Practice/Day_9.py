"""Problem 1 🟢

Create a list of 8 random numbers (you can hardcode them). 
Sort it in ascending order, then descending. Print both. 
Then print only the middle 4 elements using slicing."""

# Create a list with 8 random numbers
import random

numbers = []
for i in range(1,9):
    numbers.append(random.randint(0,100))

print(numbers)

# sort it in ascending order
sorted_ascending_order = sorted(numbers)

# sort it in descending order
sorted_descending_order = sorted(numbers, reverse=True)

# print both 
print(f'This is ascending oder of the numbers: {sorted_ascending_order}')
print(f'This is descending order of numbers: {sorted_descending_order}')

# Print mildel 4 numbers
print(f'This is middle 4 numbers: {numbers[2:6:1]}')


"""
Problem 2 🟡

Ask the user to enter 6 numbers.
Store them in a list. 
Remove the largest and smallest numbers, 
then print the remaining list and its new average."""

# step 1 : Ask the user to enter 6 numbers store them in a list
# let's create a list for store the numbers
nums = []
# now let's ask the user to enter 6 numbers
for i in range(1,7):

    while True:
        try:
            num = int(input(f'Enter the {i} number: '))
            nums.append(num)
            break    
        except ValueError:
            print("Invalid input. Please enter digits only.")
   
print("Your list of numbers:", nums)

# Let's find the largest number
largest_number = max(nums)
print(f'The largest number in nums is: {largest_number}')
# remove the larget number
nums.remove(largest_number)

# Let's find the smallest number
smallest_number = min(nums)
print(f'The smallest number in nums is: {smallest_number}')
nums.remove(smallest_number)

# Print the list after removing largest and smallest
print("After remove largest & smallest list of numbers:", nums)

# Now lets Find the average of remaining numbers in nums
total_sum = sum(nums)
total_len = len(nums)

average = total_sum/total_len

print(f'This the average: {average}')


