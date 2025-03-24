quantity_of_pieces = int(input())
pieces_list = {}

for _ in range(quantity_of_pieces):
    piece, composer, key = input().split("|")
    pieces_list[piece]=[composer, key]

while True:
    command = input()
    if command == "Stop":
        break
    parts = command.split("|")
    process = parts[0]
    piece_name = parts[1]

    if process == "Add":
        if piece_name in pieces_list:
            print(f"{piece_name} is already in the collection!")
        else:
            composer = parts[2]
            key = parts[3]
            pieces_list[piece_name] = [composer, key]
            print(f"{piece_name} by {composer} in {key} added to the collection!")
    elif process == "Remove":
        if piece_name not in pieces_list:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
        else:
            del pieces_list[piece_name]
            print(f"Successfully removed {piece_name}!")
    elif process == "ChangeKey":
        if piece_name not in pieces_list:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
        else:
            new_key = parts[2]
            pieces_list[piece_name][1] = new_key
            print(f"Changed the key of {piece_name} to {new_key}!")

for piece in pieces_list:
    composer, key = pieces_list[piece]
    print(f"{piece} -> Composer: {composer}, Key: {key}")