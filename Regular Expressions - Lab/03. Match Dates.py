import re

pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
text = input()

dates = re.finditer(pattern, text)
for date in dates:
    date_data = date.groupdict()
    print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")