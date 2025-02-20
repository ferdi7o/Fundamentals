def get_chars_in_range(start, end):
    result = ""
    for char in range(ord(start) + 1, ord(end)):
        result += f"{chr(char)} "
    return result


start_char = input()
end_char = input()
print(get_chars_in_range(start_char, end_char))