number_one = int(input())
number_two = int(input())

def factorial(factorial_number):
    if factorial_number == 0 or factorial_number == 1:
        return 1
    result = 1
    for num in range(2, factorial_number + 1):
        result *= num
    return result

num_one = factorial(number_one)
num_two = factorial(number_two)

calculation = num_one / num_two
print(f"{calculation:.2f}")