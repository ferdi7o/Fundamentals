numbers_as_string = input().split(", ")

numbers_as_int = [int(num) for num in numbers_as_string]
even_list = [index for index in range(len(numbers_as_int)) if numbers_as_int[index]%2==0]

print(even_list)