import re

pattern = r"\d+"
text = input()

while text:
    digits = re.findall(pattern, text)
    if digits:
        print(' '.join(digits), end = " ")

    text = input()