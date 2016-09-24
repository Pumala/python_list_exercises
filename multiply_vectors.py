print "Multiply Vectors Exercise"
# Given two list of numbers (both lists of same length), create a new list
# by multiplying the pairs of numbers in corresponding positions:
# Ex: [2, 3, 5] x [3, 4, 2] = [6, 12, 10]

num_list_1 = [4, 5, 2, 8]
num_list_2 = [3, 6, 9, 6]
num_list_3 = []
index = 0

for num in num_list_2:
    curr_product = num_list_1[index]
    num_list_3.append(curr_product * num)
    index += 1

print num_list_3
