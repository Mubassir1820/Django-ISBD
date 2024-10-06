# Write a Python function categorize_temperature(temp) that takes the temperature in Celsius as input and returns "Cold" if the temperature is below 10, "Warm" if it is between 10 and 25, and "Hot" if it is above 25.

def categorize_temperature(temp):
    
    # Condition-1
    if temp < 10:
        print("Cold")
    # Condition-2
    elif temp >= 10 and temp <= 25:
        print("Warm")
    # # Condition-3
    else:
        print("Hot")

temp = int(input("Enter the temperature: "))
categorize_temperature(temp)