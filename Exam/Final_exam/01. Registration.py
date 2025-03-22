def letters(words,low_or_up):
    if low_or_up == "Lower":
        text = words.lower()
        print(text)
    else:
        print(words.upper())

def substring(words, substring):
    if substring in words:
        print(words.replace(substring, ""))
    else:
        print(f"The username {words} doesn't contain {substring}.")

def replace(words, replace_char):
    if replace_char in words:
        print(words.replace(replace_char, "-"))

def is_valid(words, chars):
    if chars in words:
        print("Valid username.")
    else:
        print(f"{chars} must be contained in your username.")

def reverse_(words, index_1, index_2):
    if 0 <= index_1 <= len(words) >= index_2:
        new_word = words[index_1: index_2 + 1][::-1]
        print(new_word.replace())


def my_program(text):
    commands = input()
    while commands != "Registration":
        parts = commands.split()
        mod = parts[0]
        index = parts[1]
        if mod == "Letters":
            letters(text, index)
        elif mod == "Substring":
            substring(text, index)
        elif mod == "Replace":
            replace(text, index)
        elif mod == "IsValid":
            is_valid(text, index)
        elif mod == "Reverse":
            index_1 = int(parts[1])
            index_2 = int(parts[2])
            reverse_(text, index_1, index_2)

        commands = input()

text = input()
my_program(text)