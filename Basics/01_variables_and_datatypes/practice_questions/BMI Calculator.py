# Instructions
# Write a program that calculates the Body Mass Index (BMI) based on the user's weight and height. The formula for BMI is:
# BMI = weight (kg) / (height (m))^2
# The program should take the user's weight in kilograms and height in meters as input, calculate the BMI, and then display the BMI value along with a message indicating whether the user is underweight, normal weight, overweight, or obese based on the following BMI categories:
# - Underweight: BMI < 18.5
# - Normal weight: 18.5 <= BMI < 24.9   
# - Overweight: 25 <= BMI < 29.9
# - Obese: BMI >= 30   



# Taking user inputs for weight and height.
weight = float(input("please enter yout weight in kilograms: "))
height = float(input("please enter your height in feet: "))

#converting height from feet to meters.
height = height * 0.3048


# Calculating BMI.
bmi = weight / (height ** 2)

# Determining BMI category.
if bmi < 18.5:
    category = "Underweight"    
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight" 
else:
    category = "Obese"

# Displaying the results.
print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")
