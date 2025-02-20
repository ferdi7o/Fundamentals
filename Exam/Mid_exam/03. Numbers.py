numbers_list = list(map(int, input().split()))
avarage_number = sum(numbers_list) / len(numbers_list)

if len(numbers_list) <= 1:
    print("No")
else:
    filtered_number = [num for num in numbers_list if num > avarage_number]
    avarage_higher_numbers = sorted(filtered_number, reverse=True)[:5]
    print(*avarage_higher_numbers if avarage_number else "No")
