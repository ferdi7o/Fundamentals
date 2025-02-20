# oneinout = input()
#
# listmaker = oneinout.split(" ")
# oppsite_numbers = []
#
# for new_number in listmaker:
#     intejurmaker = -int(new_number)
#     oppsite_numbers.append(intejurmaker)
#
# print(oppsite_numbers)

allnumbers = input().split()

opposite_list = [-int(number) for number in allnumbers]

print(opposite_list)