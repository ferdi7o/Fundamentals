text = input().split("\\")
name, extension = text[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")