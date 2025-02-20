numbers = input().split()
numbers_as_int_in_list = [int(num) for num in numbers]

min_number = min(numbers_as_int_in_list)
max_number = max(numbers_as_int_in_list)
sum_numbers = sum(numbers_as_int_in_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
