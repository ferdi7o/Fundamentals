first_list = input().split(", ")
twirst_list = input().split(", ")

result_list = [word for word in first_list if any(word in second_word for second_word in twirst_list)]

# for item in first_list:
#     for second_word in twirst_list:
#         if item in second_word:
#             result_list.append(item)
#             break

print(result_list)