print "Smallest Exercise"
# Print the smallest number in the list

num_list = [10, 24, 4, 14, 35, 31, 18]
small_num = num_list[0]

for num in num_list:
    if num < small_num:
        small_num = num

print small_num
