# Take 10 integer values from the user
numbers = []
for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Set count values for positive, negative, odd, and even numbers
positive_count = 0
negative_count = 0
odd_count = 0
even_count = 0

# Set count to store the frequency
frequency = {}

# Iterate through the list of numbers
for number in numbers:
    # Check if the number is positive or negative
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

    # Check if the number is odd or even
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Update the frequency
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# Print the results
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
print("Frequency of each number:")
for number, freq in frequency.items():
    print(number, "occurs", freq, "time(s)")
