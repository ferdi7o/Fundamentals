key_value = {}
data = input().split()
search = input().split()

for el in range(0, len(data), 2):
    key = data[el]
    value = int(data[el + 1])
    key_value[key] = value

for searh in search:
    if searh in key_value.keys():
        print(f"We have {key_value[searh]} of {searh} left")
    else:
        print(f"Sorry, we don't have {searh}")