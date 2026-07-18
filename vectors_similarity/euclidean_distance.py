v1 = [2,3, 4]
v2 = [4,5, 2]

def calculate_squared_sum(v1,v2):
    """
    calculate squared sum of two vectors i.e: { (v2[0] - v1[0])**2 + (v2[1] - v1[1])**2 + ... (v2[n] - v1[n])**2 }
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension.")
    
    total = 0
    for i in range(len(v1)):
        total += (v2[i] - v1[i]) ** 2

    return total 


def calculate_euclidean_distance(v1, v2):
    return round((calculate_squared_sum(v1,v2) ** 0.5), 2)


if __name__ == '__main__':
    print(calculate_euclidean_distance(v1, v2))
    # print(calculate_squared_sum(v1,v2))
