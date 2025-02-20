numbers = input().split()

new_list = [float(element) for element in numbers]
new_list = [round(el) for el in new_list]
print(new_list)