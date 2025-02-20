number = int(input())
positive_list = []
negative_list = []

for _ in range(number):
    number_p_or_n = int(input())
    if number_p_or_n < 0:
        negative_list.append(number_p_or_n)
    else:
        positive_list.append(number_p_or_n)


print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)} \nSum of negatives: {sum(negative_list)}")