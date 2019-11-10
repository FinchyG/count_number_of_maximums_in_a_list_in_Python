# Problem: Count how many days temperature was the maximum temperature for the week

# Input: temperatures, a list of 7 numbers

# temperatures = [7, 7, 7, 7, 7, 7, 7]
# temperatures = [6, 6, 6, 6, 6, 6, 7]
# temperatures = [7, 7, 7, 7, 7, 7, 6]
temperatures = [1, 2, 3, 4, 5, 6, 7]

# Output: highest temperature for the week, a number

highest_temperature = temperatures[0]

# for loop to identify highest temperature of the week

for temperature in range(temperatures[1],len(temperatures) + 1):
    if temperature > highest_temperature:
        highest_temperature = temperature

# Output: count of the number of occurrences of highest_temperature, an integer

highest_temperature_occurrences = 0

# for loop to count the number of times highest_temperature occurs in a week

for temperature in temperatures:
    if temperature == highest_temperature:
        highest_temperature_occurrences = highest_temperature_occurrences + 1

print('The number of times the highest temperature occurred is ', highest_temperature_occurrences)
