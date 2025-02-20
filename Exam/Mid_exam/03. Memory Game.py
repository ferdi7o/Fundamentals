def memory_game():
    elements = input().split()
    moves = 0
    command = input()

    while command != "end":

        moves += 1
        index1, index2 = map(int, command.split())

        if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements):
            middle_index = len(elements) // 2
            elements.insert(middle_index, f"-{moves}a")
            elements.insert(middle_index + 1, f"-{moves}a")
            print("Invalid input! Adding additional elements to the board")
        elif elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            first, second = sorted([index1, index2], reverse=True)
            elements.pop(first)
            elements.pop(second)
        else:
            print("Try again!")

        if not elements:
            print(f"You have won in {moves} turns!")
            return

        command = input()


    print("Sorry you lose :(")
    print(" ".join(elements))


memory_game()
