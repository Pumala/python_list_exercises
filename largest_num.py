print "Largest Number Exercise"
# Print the largest number in the list

num_list = [10, 24, 4, 14, 35, 31, 18]
big_num = num_list[0]

for num in num_list:
    if num > big_num:
        big_num = num

print big_num
