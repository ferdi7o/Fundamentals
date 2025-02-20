# numbers = input().split(", ")
#
# for polindrome in numbers:
#     if polindrome[0] == polindrome[-1]:
#         print(True)
#     else:
#         print(False)

numbers = input()

def check_polindrome(number):
     return str(number) == str(number)[::-1]


def int_maker(numbers):
    number_as_int = map(int, numbers.split(", "))
    check = [check_polindrome(num) for num in number_as_int]
    for item in check:
        print(item)

int_maker(numbers)