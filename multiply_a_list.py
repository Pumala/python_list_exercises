print "Multiply a List Exercise"
# Given a list of numbers, and a single number to represent the factor,
# create a new list consisting of each of the number in the first list
# multiplied by the factor

factor = int(raw_input("Choose a number to represent the factor: "))

num_list_1 = [4, 5, 3, 2, 7]
num_list_2 = []

for num in num_list_1:
    num_list_2.append(num * factor)

print num_list_2
