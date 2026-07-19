v1 = [3,2]
v2 = [1,4]
v3 = [4,5,2]
v4 = [3,1,3]

A = [v1,v2]
B = [v3, v4]

def dot_prod(v1, v2):
    total = 0
    for i in range(len(v1)):
        total+= v1[i] * v2[i]
    return total

num_rows_A = len(A)
num_col_B = len(B[0])
num_rows_B = len(B)


final_result = []
for row in A:
    temp = []
    
    for j in range(num_col_B):
        col = []
        for k in range(num_rows_B):
            col.append(B[k][j])
        temp.append(dot_prod(row,col))
    final_result.append(temp)

print(final_result)
