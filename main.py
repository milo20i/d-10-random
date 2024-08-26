import random

# Create a list of numbers from 1 to 90
numbers = list(range(1, 91))

# Randomly select 6 unique numbers from the list
random_numbers = random.sample(numbers, 6)

# Print the selected numbers
print(random_numbers)
