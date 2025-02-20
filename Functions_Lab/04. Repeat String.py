string = input()
n_times = int(input())

repeat_string = lambda a, b: a * b

write = repeat_string(string, n_times)
print(write)