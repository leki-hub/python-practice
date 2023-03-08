# List of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all elements in the list are greater than 0
result = all(x > 0 for x in numbers)
print(result)  # True
# List of numbers and strings
mixed_list = [1, 2, 3, "4", 5]

# Check if all elements in the list are integers
result = all(isinstance(x, int) for x in mixed_list)
print(result)  # False
