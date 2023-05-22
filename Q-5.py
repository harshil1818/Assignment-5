def print_alphabet_triangle(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0

    for i in range(1, rows + 1):
        for j in range(i):
            print(alphabet[count % 26], end="")
            count += 1
        print()

# Test the function
num_rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(num_rows)
