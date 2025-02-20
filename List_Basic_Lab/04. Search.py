n_number = int(input())
key_word = input()
mein_list = []

for _ in range(n_number):
    new_element = input()
    mein_list.append(new_element)

print(mein_list)

for element in range(len(mein_list) -1, -1, -1):
    if key_word not in mein_list[element]:
        mein_list.remove(mein_list[element])

print(mein_list)
