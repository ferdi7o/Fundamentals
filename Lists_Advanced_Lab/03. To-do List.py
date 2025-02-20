work_list = [0] * 10
command = input()

while command != "End":
    index, text = command.split("-")
    index = int(index) - 1
    work_list[index] = text

    command = input()


def text_filter(list):
    edited_list = [item for item in list if item != 0]
    return edited_list

print(text_filter(work_list))