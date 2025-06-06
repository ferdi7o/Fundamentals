import re

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"
text = input()
travel_points = 0

matches = re.findall(pattern, text)

destinations = [match[1] for match in matches]
travel_points += sum(len(dest) for dest in destinations)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
