import re

pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
text = input()
matches = re.findall(pattern, text)

all_matches = {match[1]: match[2] for match in matches}
mirrored_maches = {}

for key, value in all_matches.items():
    reverse_value = value[::-1]
    if key == reverse_value:
        mirrored_maches[key] = value

if not all_matches:
    print("No word pairs found!")
else:
    print(f"{len(all_matches)} word pairs found!")
if not mirrored_maches:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(f"{key} <=> {value}" for key, value in mirrored_maches.items()))