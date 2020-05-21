#2D Lists #matrix
#each item in list is another list
# 1 2 3
# 4 5 6
# 7 8 9
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print("___________________")
for items in matrix:
    print(items)
print("___________________")
print(matrix[0])#[1,2,3] zeroth index of matrix
print(matrix[0][0]) #1 Zeroth index of the element present at the zeroth index of matrix
matrix[0][0]=9 #replacing value
print((matrix[0][0]))