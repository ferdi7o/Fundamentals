import re

pattern = r"(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
text = input()

while text:
    match = re.search(pattern, text)

    if match:
        url = match.group(1)
        print(url)

    text = input()


