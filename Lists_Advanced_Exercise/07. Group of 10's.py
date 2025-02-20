numbers = list(map(int, input().split(", ")))
group = 10

while len(numbers) != 0:

    list_of_numbers = [number for number in numbers if number <= group]
    remover = [numbers.remove(number) for number in list_of_numbers]
    print(f"Group of {group}'s: {list_of_numbers}")
    group += 10