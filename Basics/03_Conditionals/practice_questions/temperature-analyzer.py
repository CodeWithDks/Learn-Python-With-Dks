# Temperature Analyzer
# Write a program that takes a temperature in Celsius as input and categorizes it as follows:

'''Temperature Analyzer

Take temperature input.

Conditions:

above 40 → “Very Hot”
above 30 → “Hot”
above 20 → “Normal”
otherwise → “Cold”
Important

Order matters.'''

temperature = int(input("Enter temperature: ")) # 45

if temperature > 40:
    print("Very Hot")
elif temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Normal")
else:
    print("Cold")