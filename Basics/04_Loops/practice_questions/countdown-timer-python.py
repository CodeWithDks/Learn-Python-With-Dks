# countdown-timer-python
# This program will create a countdown timer that counts down from 10 to 0, with a delay of 1 second between each number.


# Smart Countdown Timer

start_number = int(input("Enter countdown number: "))


# Validation
if start_number <= 0:
    print("Invalid input!")

else:

    # Countdown Loop
    for number in range(start_number, 0, -1):

        print(number)

        # Special Events
        if number == 10:
            print("Starting final sequence...")

        elif number == 5:
            print("Warning: Launch imminent!")

        elif number == 1:
            print("Too close... Ignition started!")

    
    # Final Message
    print("🚀 Blast Off! 🚀")
