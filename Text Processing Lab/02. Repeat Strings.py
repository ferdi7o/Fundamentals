repeat = input()

if " " not in repeat:
    print(repeat * (len(repeat)))
else:
    text_list = repeat.split()
    for text in text_list:
        print(text * len(text), end="")