print "Matrix Addition Exercise"
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional
# list is represented as a list of lists:

matrix_1 = [
            [1, 3],
            [2, 4],
            [3, 6]
                ]

matrix_2 = [
            [5, 2],
            [1, 0],
            [8, 5]
                ]

num_list_3 = matrix_1

# Calculate the result of adding the 2 matrices.

if (len(matrix_1) == len(matrix_2)):
    for num1 in range(0, len(matrix_1)):
        for num2 in range(0, len(matrix_1[0])):
            sum = matrix_1[num1][num2] + matrix_2[num1][num2]
            num_list_3[num1][num2] = sum

    print num_list_3
