import re

pattern = r"\b(?P<day>\d{2})([\./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
text = input()

