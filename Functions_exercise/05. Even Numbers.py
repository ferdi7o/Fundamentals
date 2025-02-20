numbers = input().split()
number_as_int = [int(num) for num in numbers]

def even_number_founder(num):
    return num % 2 == 0


even_numbers = list(filter(even_number_founder,number_as_int))
print(even_numbers)