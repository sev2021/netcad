my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        print(my_list[i])               # debug only
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
