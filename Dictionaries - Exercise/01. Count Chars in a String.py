text = input()
dics = {}

for character in text:
    if character == " ":
        continue
    if character in dics:
        dics[character] += 1
    else:
        dics[character] = 1

for item, key in dics.items():
    print(f"{item} -> {key}")