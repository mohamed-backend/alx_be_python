# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter variable for the while loop
row = 0

# Use a while loop to iterate through the rows of the pattern
while row < size:
    # Use a for loop to print the asterisks for each row
    for _ in range(size):
        print("*", end="")  # Print asterisks side by side without newline
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
