text = input()
edited_text = ""

for index in range(len(text)):
    if edited_text == "":
        edited_text += text[index]
    elif edited_text[-1] == text[index]:
        continue
    else:
        edited_text += text[index]

print(edited_text)