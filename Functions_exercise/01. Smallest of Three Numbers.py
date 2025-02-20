# def smallest_number():
#     my_list = []
#     my_list.append(first_number)
#     my_list.append(twirst_number)
#     my_list.append(third_number)
#     small_number = min(my_list)
#     return small_number
#
#
# first_number = int(input())
# twirst_number = int(input())
# third_number = int(input())
# print(smallest_number())

def find_smaller_number(numbers: list) -> int:
    return min(numbers)

number_one = (input()) # input 25, 21, 4 ERROR
number_two = (input())
number_three = (input())

smaller_number = find_smaller_number([number_one, number_two, number_three])
print(smaller_number)