def length_name_filter(name) -> bool:
    if 3 < len(name) <= 16:
        return True
    return False

def only_letters(name) -> bool:
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True

def selbols_finder(name) -> bool:
    if " " in name:
        return False
    return True

def user_name_checker(name: str) -> bool:
    if length_name_filter(name) and only_letters(name) and selbols_finder(name):
        return True
    return False

username = input().split(", ")
for name in username:
    if user_name_checker(name):
        print(name)