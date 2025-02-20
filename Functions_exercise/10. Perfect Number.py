perfect_number = int(input())

def perfect_num(asd):
    sum_as_half = 0
    for num in range(1, perfect_number):
        if perfect_number % num == 0:
            sum_as_half += num
    if sum_as_half == perfect_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_num(perfect_number))