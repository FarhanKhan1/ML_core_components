v1= [3,1]
v2 = [-1,3]

def pairwise_product(v1, v2):
    result = [v1[i]*v2[i] for i in range(len(v1))]
    return result

def dot_product(v1,v2):
    return sum(pairwise_product(v1,v2))

print(dot_product(v1, v2))