matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix[0][1]=10
matrix[1][1]=20
matrix[2][1]=30
for row in matrix:
    for col in matrix:
        print(col)
    print()
    break