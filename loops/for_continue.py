numbers = range(1, 21)

for num in numbers:
    if num % 2 != 0:
        continue  # Skip odd numbers
    
    print("Even number:", num)