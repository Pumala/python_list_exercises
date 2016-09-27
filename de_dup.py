print "De-dup Exercise"
# Given a list of numbers or strings, create a new list containing the
# same elements as the first list, except with any duplicate values removed.
# Print the list.

mixed_list = [1, "cat", 4, "dog", 8, "cat", 5, 8, "fish", 4, "monkey", 5, "tuna", "dog", "fish", "dog", 5]
no_dups_list = []

for element in mixed_list:
    if element not in no_dups_list:
        no_dups_list.append(element)

print no_dups_list
