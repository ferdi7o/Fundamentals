deck_file = input().split(" ")
splitling = int(input())

for i in range(splitling):
    left_deck = []
    right_deck = []

    half_deck = len(deck_file) // 2
    left_deck = deck_file[:half_deck]
    right_deck = deck_file[half_deck:]

    deck_file = []

    for item in range(half_deck):
        deck_file.append(left_deck[item])
        deck_file.append(right_deck[item])

print(deck_file)