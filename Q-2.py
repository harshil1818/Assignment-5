start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
divisor = int(input("Enter the number to check divisibility: "))

print("Numbers divisible by", divisor, "in the range", start, "to", end, "are:")
for num in range(start, end+1):
    if num % divisor == 0:
        print(num)