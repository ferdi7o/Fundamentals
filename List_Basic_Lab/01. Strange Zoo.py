tail = input()
body = input()
head = input()

meerkat_list = [tail, body, head]

meerkat_list[0] , meerkat_list[-1] = meerkat_list[-1], meerkat_list[0]

print(meerkat_list)
