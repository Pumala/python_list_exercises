# print "De-dup Exercise"
# Given a list of numbers or strings, create a new list containing the
# same elements as the first list, except with any duplicate values removed.
# Print the list.

num_list = [1, 4, 5, 4, 3, 1, 1, 7, 8, 5, 9, 5]
num_list_new = [1, 4, 5, 4, 3, 1, 1, 7, 8, 5, 9, 5]
num_list2 = []

for num1 in num_list_new:
    counter = 0
    num_list2.append(num1)
    for num2 in num_list2:
        if num1 == num_list2[counter]:
            # del num_list[counter]
            del num_list2[num1]
            counter -= 1
            # deleted += 1
        counter += 1
    if counter == len(num_list):
        counter = 0

print num_list2


# num_list = [1, 4, 5, 4, 3, 1, 1, 7, 8, 5, 9, 5]
# num_list_new = [1, 4, 5, 4, 3, 1, 1, 7, 8, 5, 9, 5]
# num_list2 = []
#
# for num1 in num_list_new:
#     counter = 0
#     num_list2.append(num1)
#     for num2 in num_list:
#         if num1 == num_list[counter]:
#             del num_list[counter]
#             counter -= 1
#             # deleted += 1
#         counter += 1
#     if counter == len(num_list):
#         counter = 0
#
# print num_list2


# for num1 in num_list:
#     counter = 0
#     deleted = 0
#     index = num_list.index[num1]
#     num_list2.append(num_list[(index - deleted)])
#     for num2 in num_list:
#         if num1 == num_list[counter]:
#             del num_list[counter]
#             counter -= 1
#             deleted += 1
#         counter += 1
#     if counter == len(num_list):
#         counter = 0
#
# print num_list2


# for num1 in num_list:
#     counter = 0
#     num_list2.append(num1)
#     # match = False
#     for num2 in num_list:
#         # compare_me = num1
#         # num_list2.append(num1)
#         # counter = 1
#         # if num1 == num_list[counter + 1]:
#         if num1 == num_list[counter]:
#         # if num1 == num2 and match == True:
#             # del num_list[counter + 1]
#             del num_list[counter + 1]
#             # del num_list2[counter]
#         match = True
#     counter += 1
#     if counter == len(num_list):
#         counter = 0
#
# print num_list2
