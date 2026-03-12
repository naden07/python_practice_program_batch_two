numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
total_difference = numbers[0]
for num in numbers[1:]:
    total_difference -= num
print(total_difference)