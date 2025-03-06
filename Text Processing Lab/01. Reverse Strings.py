text = input()

while text != "end":
    reversed_text = ""
    for char in text[::-1]:
        reversed_text += char
    print(f"{text} = {reversed_text}")

    text = input()