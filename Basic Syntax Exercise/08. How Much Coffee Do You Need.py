comand = input()
cafee_counter = 0

while comand != "END":
    if comand.lower() == "coding" or comand.lower() == "dog" or \
            comand.lower() == "cat" or comand.lower() == "movie":
        if comand.islower():
            cafee_counter += 1
        else:
            cafee_counter += 2
    comand = input()

if cafee_counter > 5:
    print("You need extra sleep")
else:
    print(cafee_counter)