import re

pattern = r"([|#])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
text = input()
matches = re.findall(pattern, text)


calories = sum([int(match[3]) for match in matches])
days = calories // 2000

print(f"You have food to last you for: {days} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")