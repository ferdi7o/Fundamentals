def even_and_odd_digits():
    numbers_as_string = input()
    list_as_int = [int(num) for num in numbers_as_string]
    even_sum = sum(num for num in list_as_int if num % 2 == 0)
    odd_sum = sum(num for num in list_as_int if num % 2 != 0)

    return even_sum, odd_sum


even_sum , odd_sum = even_and_odd_digits()
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")