import re

phone_nums = input()
pattern = r"(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b"

match_nums = re.findall(pattern, phone_nums)
print(", ".join(match_nums))