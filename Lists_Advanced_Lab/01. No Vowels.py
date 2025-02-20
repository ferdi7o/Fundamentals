def vowels_romever(input_text):
    forbidden_letters = ['a', 'o', 'u', 'e', 'i']
    new_list_of_text = [char for char in input_text if char.lower() not in forbidden_letters]
    return "".join(new_list_of_text)

text = input()
edited_text = vowels_romever(text)
print(edited_text)



# edited_tex = []
#
# for char in text:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         edited_tex.append(char)
#
# print("".join(edited_tex))