numbers = [4, 8, 15, 16, 23, 42]
target = 16

i = 0

while i < len(numbers):
    if numbers[i] == target:
        print("Number found at index:", i)
        break  # Exit loop 
    i += 1
