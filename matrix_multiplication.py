print "Matrix Multiplication Exercise"
# Given 2 two-dimensional lists of numbers, calculate the results of multiplying
# the two matrices and print the result in a Matrix

matrix_1 = [
            [2, 0],
            [1, 2]
                ]

matrix_2 = [
            [1, 2],
            [3, 4]
                ]

num_list_3 = [[],[]]

matrix_length = len(matrix_1)

for num1 in range(0, matrix_length): # 0, 1
    for num2 in range(0, matrix_length): # 0, 1
        product = matrix_1[num1][0] * matrix_2[0][num2]
        product += matrix_1[num1][1] * matrix_2[1][num2]
        num_list_3[num1].insert(num2, product)

print num_list_3


# product = matrix_1 = (0)(0) * matrix_2 (0)(0) # 2 * -1
# product = matrix_1 = (0)(1) * matrix_2 (1)(0) # -2 * 7

# product = matrix_1 = (0)(0) * matrix_2 (0)(1) # 2 * 4
# product = matrix_1 = (0)(1) * matrix_2 (1)(1) # -2 * -6

# product = matrix_1 = (1)(0) * matrix_2 (0)(0) # 5 * -1
# product = matrix_1 = (1)(1) * matrix_2 (1)(0) # 3 * 7

# product = matrix_1 = (1)(0) * matrix_2 (0)(1) # 5 * 4
# product = matrix_1 = (1)(1) * matrix_2 (1)(1) # 3 * -6
