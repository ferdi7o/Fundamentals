import re

text = input()
pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z0-9\-]+(\.[a-z0-9]+)+))\b"

search_email = re.findall(pattern, text)

for email in search_email:
    print(email[0])