def matrixElementsSum(matrix):
    total=sum(matrix[0])
    for i in range(1,len(matrix)): # row index
        for j in range(len(matrix[i])): # col index
            if matrix[i-1][j] !=0:
                total+=matrix[i][j]
    return total


matrix=[[0,1,1,2],
        [0,5,0,0],
        [2,0,3,3]]


print(matrixElementsSum(matrix))
