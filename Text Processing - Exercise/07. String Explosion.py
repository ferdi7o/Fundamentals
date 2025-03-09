text = input()
explosion_count = 0
edited_text = ""

for index in range(len(text)):
    if text[index] != ">":
        if explosion_count > 0:
            explosion_count -= 1
            continue
        else:
            edited_text += text[index]
    elif text[index] == ">":
        explosion_count += int(text[index + 1])
        edited_text += text[index]

print(edited_text)