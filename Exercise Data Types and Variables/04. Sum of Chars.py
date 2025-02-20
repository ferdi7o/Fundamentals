number_of_charakters = int(input())
total_sum = 0

if number_of_charakters > 20:
    pass

else:
    for i in range(number_of_charakters):
        asci = input()
        total_sum += ord(asci)

    print(f"The sum equals: {total_sum}")
