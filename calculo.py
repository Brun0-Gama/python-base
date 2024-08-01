import os

# Assuming desired_capacity is already defined
desired_capacity = 42 # Example value, replace it with your desired value
MEMORY_DOWN = 80
# Calculate the percentage
percentage = round((1 - (int(MEMORY_DOWN) / (desired_capacity * 7 * 0.95))) * 100)
# cpu = round((1 - (int(MEMORY_DOWN) / (desired_capacity * 7 * 0.95))) * 100)
print(percentage)
# print(cpu)