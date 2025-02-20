def is_all_num_and_digits(password):
    return password.isallet() and password.isalnum() \
           or print("Password must consist only of letters and digits")


def is_have_two_num():
    pass



def password_validator(password):
    if 6 > len(password) or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
        return



password = input()
