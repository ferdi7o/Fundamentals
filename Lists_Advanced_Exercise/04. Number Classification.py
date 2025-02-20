numbers = [int(num) for num in input().split(", ")]

negative = [number for number in numbers if number < 0]
positive = [number for number in numbers if number >= 0]
odd = [number for number in numbers if number % 2 != 0]
even = [number for number in numbers if number % 2 == 0]

print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')