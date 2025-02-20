def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum_numbers, num3):
    return sum_numbers - num3


def add_and_subtract():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    sum_result = sum_numbers(num1, num2)
    final_result = subtract(sum_result, num3)
    print(final_result)


add_and_subtract()
