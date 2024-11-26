print("* Calculate the sum between start and stop number *")

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

total_sum = 0
for num in range(start, end + 1):
    total_sum += num

print(f"The sum from {start} to {end} is: {total_sum}")