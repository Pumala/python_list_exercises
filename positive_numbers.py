print "Positive Numbers II"
# Given a list of numbers, create a new list of positive numbers from the
# first list that are greater than zero

num_list_1 = [-10, 24, 7, -14, -35, 30, -19]
num_list_2 = []

for num in num_list_1:
    if (num / 1) > 0:
        num_list_2.append(num)

print num_list_2
