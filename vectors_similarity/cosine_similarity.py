a = [1,2,3] #vector 1
b = [4,5,6]  #vector 2

"""
cosine_similarity = (v1.v2) / (||v1|| ||v2||)
"""

def dot(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension.")
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    # print(total)
    return total


def magnitude(v):
    """
        This function takes a vector as input and
        calculates its magnitude.
    """
    return dot(v,v) ** 0.5

def cosine_similarity(a,b):
    a_magnitude=magnitude(a)
    b_magnitude=magnitude(b)
    
    if a_magnitude == 0 or b_magnitude == 0:
        print("Cannot compute cosine similarity with a zero vector.")
    else:
        cosine_similarity = (dot(a,b)/(a_magnitude*b_magnitude))
        return round(cosine_similarity,3)

if __name__ == "__main__":
    print(cosine_similarity(a,b))    
    # dot(a,b)



"""
1. Compute the dot product of the two vectors.
2. Compute the magnitude of each vector.
3. Check for zero vectors (to avoid division by zero).
4. Compute the cosine similarity using the formula.
5. Return the cosine similarity.
"""

