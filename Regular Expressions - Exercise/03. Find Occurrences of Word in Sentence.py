import re

text = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"

search = re.findall(pattern, text, re.IGNORECASE)

print(len(search))
