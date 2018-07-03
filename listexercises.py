# Sum the numbers

numbers = [1, 2, 3]
def sum_numbers(numbers):
    total = 0
        for num in numbers:
        total+= num
    print total
    return total
sum_numbers([1,2,3,4])

# Largest Number
def largest_number(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num
    print largest
    return largest
largest_number([1, 2, 3, 4, 5])

#Smallest Number
def smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print smallest
    return smallest
smallest_number([1, 1, 1, 1, 1])

# Positive Numbers

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            print num
    return num
print positive_numbers([-1, -2, 1, 2])

# Positive Numbers 2
def positive_numbers2(numbers):
    positive_num = []
    for num in numbers:
        if num > 0:
            positive_num.append(num)
    print positive_num
    return postiive_num
positive_numbers2([-1, -2, 1, 2])

#Multiply a list
def mult_lst(lst, factor):
    new_lst = []
    for num in lst:
        product = num * factor
        new_lst.append(product)
    print new_lst
    return new_lst
mult_lst([1,2,3,4], 2)

#Multiply vectors
def mult_vector(lst1, lst2):
    new_lst = []
    for i in range(0, len(lst1)):
        product = lst1[i] * lst2[i]
        new_lst.append(product)
    print new_lst
    return new_lst
mult_vector([1,2,3,4,], [1,2,3,4,])
    
    # Alternate
# def mult_vector(lst1, lst2):    
#     new_lst = []
#     for i in lst1:
#         product = i * lst2[]
#         new_lst.append(product)
#     print new_lst
# mult_vector([1,2,3,4,], [1,2,3,4,])

# Add Matrices
matrix1 = [ [1, 2,],
    [3,4] ]
matrix2 = [[5,6],
    [7,8] ]
def matrix_add(mat1, mat2):
    new_lst1 = []
    new_lst2 = []
    new_mat= [[new_lst1], [new_lst2]]
    for i in range(1):
        for j in range(2):
            total = mat1[i][j] + mat2[i][j]
            new_lst1.append(total)
    for k in range(1,2):
        for l in range(2):
            total = mat1[k][l] + mat2[k][l]
            new_lst2.append(total)
    print new_mat
    return new_mat
matrix_add(matrix1, matrix2)

    #Alternate
matrix1 = [ [1, 2, 3],
    [3,4, 5], [2, 122, 344]]
matrix2 = [[5, 6, 2],
    [7, 8, 3], [1, 2, 677] ]


def matrix_add(mat1, mat2):
    matrix_total = []
    height = len(mat1)
    width = len(mat1[0])

    for i in range(height):
        matrix_total.append([])
        for j in range(width):
            total = mat1[i][j] + mat2[i][j]
            matrix_total[i].append(total)
    print matrix_total
    return matrix_total

matrix_add(matrix1, matrix2)

#     #Alternate
# def create_empty_matrix(width, height):
#     result = []
#     for i in range(height):
#         result.append([])
#         for j in range(width):
#             result[i].append(0)
#     return result

# def matrix_add2(matrix1, matrix2):
#     width = len(matrix1)
#     height = len(matrix1[0])
#     matrix_total = create_empty_matrix(width, height)
#     for i in range(height):
#         for j in range(width):
#             total = matrix1[i][j] + matrix2[i][j]
#             matrix_total[i] += total
#     print matrix_total
#     return matrix_total
# matrix_add2(matrix1, matrix2)

# De-dup
test_lst = [1, 2, 1, "hi", "hi", "hello"]
def de_dup(lst):
    de_dup_list = []
    for i in lst:
        if i not in de_dup_list:
            de_dup_list.append(i)
    print de_dup_list
    return de_dup_list
de_dup(test_lst)

# Matrix Multiplication
matrix1 = [ [1, 2,],
    [3,4] ]
matrix2 = [[5,6],
    [7,8] ]
def matrix_multiply(mat1, mat2):
    mat_product = [[0], [0]]
    for i in range(len(mat_product)):
        for j in mat_product[i]:
            for k in range(len(mat_product)):
                product1 = mat1[i][k] * mat2[k][j]
                mat_product[i][j] += product1
    print mat_product
    return mat_product
mat_mult(matrix1, matrix2)

#Alternate
matrix1 = [ [1, 2],
    [3,4] ]
matrix2 = [[5,6],
    [7,8]]
mat_product = []
for i in range(len(matrix1)):
    mat_product.append([])
    for j in range(len(mat_product)):
        mat_product[i].append(0)
        for k in range(len(mat_product)):
            product = matrix1[i][k] * matrix2[k][j]
            mat_product[i][j] += product
    print mat_product



    


   






    





   


