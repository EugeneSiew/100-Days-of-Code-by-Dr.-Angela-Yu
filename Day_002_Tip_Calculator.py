# Greetings and Prompt user to enter total bill and tip percentage 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Convert tip to percentage
percentage_of_tip = tip/100 + 1

# Prompt user to enter number of people splitting the bill
num_of_people = int(input("How many people to split this bill? "))

# Calculate the price per person has to pay (2 decimal places)
price_per_person = "{:.2f}".format((bill*percentage_of_tip) / num_of_people)

# Print the price each person has to pay
print(f"Each person should pay: ${price_per_person}")

