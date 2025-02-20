special_number = int(input())

for number in range(1, special_number + 1):
    sum_of_digits = 0
    digits = number

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        special_or_not = True
    else:
        special_or_not = False

    print(f"{number} -> {special_or_not}")