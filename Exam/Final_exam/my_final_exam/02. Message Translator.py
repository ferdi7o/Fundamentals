import re

messages = int(input())
pattern = r"!([A-Z]{1}[a-z]{2,})!:\[([A-Za-z]{8,})]"


for _ in range(messages):
    message = input()
    valid = re.findall(pattern, message)
    if valid:
        message_codes = ""
        valid_message = valid[0][1]
        for char in valid_message:
            message_codes += str(ord(char)) + " "
        print(f"{valid[0][0]}: {message_codes}")
    else:
        print("The message is invalid")

