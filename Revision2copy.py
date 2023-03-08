# Initialize the sum to zero
sum = 0

# Get the number from the user
num = int(input("Enter a number: "))

# Initialize the counter variable
i = 1

# Use a while loop to iterate through all numbers from 1 to num
while i <= num:
    # Check if the current number is even
    if i % 2 == 0:
        # If it is, add it to the sum
        sum += i
    # Update the counter variable
    i += 1

# Print the final sum
print("The sum of all even numbers from 1 to", num, "is", sum)
