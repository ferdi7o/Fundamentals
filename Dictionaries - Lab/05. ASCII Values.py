data = input().split(", ")
dic = {el: ord(el) for el in data} # comprehesion dictionary

# for el in data:
#     key = el
#     value = ord(el)
#     dic[key] = value

print(dic)